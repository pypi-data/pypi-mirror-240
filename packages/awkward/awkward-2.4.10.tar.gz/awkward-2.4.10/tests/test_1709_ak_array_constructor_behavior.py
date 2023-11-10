# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import pytest  # noqa: F401

import awkward as ak
from awkward._nplikes.numpy import Numpy

numpy = Numpy.instance()


class MyBehavior(ak.Array):
    ...


def test():
    behavior = {"MyBehavior": MyBehavior}
    array = ak.with_parameter([[1, 2, 3]], "__list__", "MyBehavior", behavior=behavior)
    assert isinstance(array, MyBehavior)

    shallow_copy = ak.Array(array)
    assert isinstance(shallow_copy, MyBehavior)
