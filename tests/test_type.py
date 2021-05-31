"""Test if the typings agree.

Mypy should not complain for anything in this file.
"""
import gtsam

from typing import cast

import unittest

from gtsam import Pose3
from gtsam.noiseModel import Diagonal
from gtsam.symbol_shorthand import X
from gtsam.noiseModel import Unit, Constrained

import numpy as np


class TestTyping(unittest.TestCase):
    def test_values(self):
        v = gtsam.Values()
        v.insert(X(0), gtsam.Pose3())

        recovered = v.atPose3(X(0))
        self.assertEqual(recovered, Pose3())

    def test_noiseModel(self):
        """Constrained.Covariance should not return constrained

        because it's not overloaded.

        This is the current behavior, but super weird.
        """
        nm = cast(Unit, Constrained.Covariance(np.eye(3)))

        nmc = cast(Constrained, Diagonal.Sigmas(np.zeros((3, ))))

        nmc1 = Constrained.MixedPrecisions(np.zeros((3, )))
