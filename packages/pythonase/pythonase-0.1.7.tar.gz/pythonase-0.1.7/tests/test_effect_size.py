#!/usr/bin/env python
# coding=utf-8

#  Copyright (c) Li Yao 2021. No unauthorized redistribution allowed.

# Created by: Li Yao (yaoli.gm@gmail.com)
# Created on: 2021-08-28
import unittest

from pythonase.stats.effect_size import cohens_q


class CohensQTestCase(unittest.TestCase):
    def test_same_sign(self):
        # test case from
        # Cohen, J. (1988). Statistical power analysis for the behavioral sciences.
        q_obtained_from_r1r2_table = 0.433
        q_obtained_from_r_z_table = 0.438
        cq = cohens_q(0.6, 0.25)
        self.assertGreaterEqual(cq, q_obtained_from_r1r2_table)
        self.assertLessEqual(cq, q_obtained_from_r_z_table)

    def test_different_sign(self):
        # test case from
        # Cohen, J. (1988). Statistical power analysis for the behavioral sciences.
        q_obtained_from_book = 0.948
        cq = cohens_q(0.6, -0.25)
        self.assertGreaterEqual(cq, q_obtained_from_book)
        self.assertAlmostEqual(q_obtained_from_book, q_obtained_from_book, places=3)


if __name__ == '__main__':
    unittest.main()
