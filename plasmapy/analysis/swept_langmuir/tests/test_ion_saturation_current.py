"""
Tests for functionality contained in
`plasmapy.analysis.swept_langmuir.ion_saturation_current`.
"""

import numpy as np
import pytest

from unittest import mock

from plasmapy.analysis import fit_functions as ffuncs
from plasmapy.analysis import swept_langmuir as _sl
from plasmapy.analysis.swept_langmuir.ion_saturation_current import (
    find_ion_saturation_current,
    find_isat_,
    ISatExtras,
)


def test_ion_saturation_current_namedtuple():
    """
    Test structure of the namedtuple used to return the computed ion saturation
    current data.
    """

    assert issubclass(ISatExtras, tuple)
    assert hasattr(ISatExtras, "_fields")
    assert ISatExtras._fields == (
        "rsq",
        "fitted_func",
        "fitted_indices",
    )
    assert hasattr(ISatExtras, "_field_defaults")
    assert ISatExtras._field_defaults == {}


class TestFindIonSaturationCurrent:
    """
    Tests for function
    `~plasmapy.analysis.swept_langmuir.ion_saturation_current.find_ion_saturation_current`.
    """

    def test_alias(self):
        """Test the associated alias(es) is(are) defined correctly."""
        assert find_isat_ is find_ion_saturation_current
