# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# Copyright 2021 The NiPreps Developers <nipreps@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
"""Unit tests of the transform object."""
from subprocess import check_call
from itertools import product
import pytest
import nibabel as nb
import numpy as np
from skimage.morphology import ball
import scipy.ndimage as nd

from sdcflows import transform as tf
from sdcflows.interfaces.bspline import bspline_grid


def generate_oracle(
    coeff_file,
    rotation=(None, None, None),
    zooms=(2.0, 2.2, 1.5),
    flip=(False, False, False),
):
    """Generate an in-silico phantom, and a corresponding (aligned) B-Spline field."""
    data = ball(20)
    data[19:22, ...] = 0
    data = np.pad(data + nd.binary_erosion(data, ball(3)), 8)

    zooms = [z if not f else -z for z, f in zip(zooms, flip)]
    affine = np.diag(zooms + [1])
    affine[:3, 3] = -affine[:3, :3] @ ((np.array(data.shape) - 1) * 0.5)

    if any(rotation):
        R = nb.affines.from_matvec(
            nb.eulerangles.euler2mat(
                x=rotation[0],
                y=rotation[1],
                z=rotation[2],
            )
        )
        affine = R @ affine

    phantom_nii = nb.Nifti1Image(
        data.astype(np.uint8),
        affine,
        None,
    )

    # Generate the grid with our tools, but fill data with cached file
    coeff_data = nb.load(coeff_file).get_fdata(dtype="float32")
    coeff_nii = bspline_grid(
        phantom_nii,
        np.array(nb.load(coeff_file).header.get_zooms()),
    )
    coeff_nii = nb.Nifti1Image(
        coeff_data,
        coeff_nii.affine,
        coeff_nii.header,
    )
    return phantom_nii, coeff_nii


@pytest.mark.parametrize("pe_dir", ["j", "j-", "i", "i-", "k", "k-"])
@pytest.mark.parametrize("rotation", [(None, None, None), (0.2, None, None)])
@pytest.mark.parametrize("flip", list(product(*[(False, True)] * 3)))
def test_displacements_field(tmpdir, testdata_dir, outdir, pe_dir, rotation, flip):
    """Check the generated displacements fields."""
    tmpdir.chdir()

    # Generate test oracle
    phantom_nii, coeff_nii = generate_oracle(
        testdata_dir / "field-coeff-tests.nii.gz",
        rotation=rotation,
    )

    b0 = tf.B0FieldTransform(coeffs=coeff_nii)
    assert b0.fit(phantom_nii) is True
    assert b0.fit(phantom_nii) is False

    b0.apply(
        phantom_nii,
        pe_dir=pe_dir,
        ro_time=0.2,
        output_dtype="float32",
    ).to_filename("warped-sdcflows.nii.gz")
    b0.to_displacements(
        ro_time=0.2,
        pe_dir=pe_dir,
    ).to_filename("itk-displacements.nii.gz")

    phantom_nii.to_filename("phantom.nii.gz")
    # Run antsApplyTransform
    exit_code = check_call(
        [
            "antsApplyTransforms -d 3 -r phantom.nii.gz -i phantom.nii.gz "
            "-o warped-ants.nii.gz -n BSpline -t itk-displacements.nii.gz"
        ],
        shell=True,
    )
    assert exit_code == 0

    ours = np.asanyarray(nb.load("warped-sdcflows.nii.gz").dataobj)
    theirs = np.asanyarray(nb.load("warped-ants.nii.gz").dataobj)
    assert np.all((np.sqrt(((ours - theirs) ** 2).sum()) / ours.size) < 1e-1)

    if outdir:
        from niworkflows.interfaces.reportlets.registration import (
            SimpleBeforeAfterRPT as SimpleBeforeAfter,
        )

        orientation = "".join([ax[bool(f)] for ax, f in zip(("RL", "AP", "SI"), flip)])

        SimpleBeforeAfter(
            after_label="Theirs (ANTs)",
            before_label="Ours (SDCFlows)",
            after="warped-ants.nii.gz",
            before="warped-sdcflows.nii.gz",
            out_report=str(
                outdir / f"xfm_pe-{pe_dir}_flip-{orientation}_x-{rotation[0] or 0}"
                f"_y-{rotation[1] or 0}_z-{rotation[2] or 0}.svg"
            ),
        ).run()


@pytest.mark.parametrize("pe_dir", ["j", "j-", "i", "i-", "k", "k-"])
def test_conversions(tmpdir, testdata_dir, pe_dir):
    """Check inverse functions."""
    tmpdir.chdir()

    fmap_nii = nb.load(testdata_dir / "topup-field.nii.gz")
    new_nii = tf.disp_to_fmap(
        tf.fmap_to_disp(
            fmap_nii,
            ro_time=0.2,
            pe_dir=pe_dir,
        ),
        ro_time=0.2,
        pe_dir=pe_dir,
    )

    new_nii.to_filename("test.nii.gz")
    assert np.allclose(
        fmap_nii.get_fdata(dtype="float32"),
        new_nii.get_fdata(dtype="float32"),
    )


def test_grid_bspline_weights():
    target_shape = (10, 10, 10)
    target_aff = [[1, 0, 0, -5], [0, 1, 0, -5], [0, 0, 1, -5], [0, 0, 0, 1]]
    ctrl_shape = (4, 4, 4)
    ctrl_aff = [[3, 0, 0, -6], [0, 3, 0, -6], [0, 0, 3, -6], [0, 0, 0, 1]]

    weights = tf.grid_bspline_weights(
        nb.Nifti1Image(np.zeros(target_shape), target_aff),
        nb.Nifti1Image(np.zeros(ctrl_shape), ctrl_aff),
    ).tocsr()
    assert weights.shape == (64, 1000)
    # Empirically determined numbers intended to indicate that something
    # significant has changed. If it turns out we've been doing this wrong,
    # these numbers will probably change.
    assert np.isclose(weights[0, 0], 0.18919244)
    assert np.isclose(weights[-1, -1], 0.18919244)
    assert np.isclose(weights.sum(axis=1).max(), 26.833675)
    assert np.isclose(weights.sum(axis=1).min(), 1.5879614)
