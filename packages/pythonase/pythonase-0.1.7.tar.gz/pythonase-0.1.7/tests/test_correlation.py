#!/usr/bin/env python
# coding=utf-8

#  Copyright (c) Li Yao 2021. No unauthorized redistribution allowed.

# Created by: Li Yao (yaoli.gm@gmail.com)
# Created on: 2021-08-28
import unittest

from pythonase.stats.correlation import compare_two_cors_ind, _fisher_z_transform


class FisherZTransformCase(unittest.TestCase):
    # test cases from https://www.statisticshowto.com/fisher-z/
    def test_zval_R0(self):
        R = 0.0
        exp = 0.0
        self.assertEqual(_fisher_z_transform(R), exp, msg="Calculated Fisher's Z doesn't meet expectation")

    def test_zval_R006(self):
        R = 0.06
        exp = 0.0601
        self.assertAlmostEqual(_fisher_z_transform(R), exp, places=4,
                               msg="Calculated Fisher's Z doesn't meet expectation")

    def test_zval_R02(self):
        R = 0.2
        exp = 0.2027
        self.assertAlmostEqual(_fisher_z_transform(R), exp, places=4,
                               msg="Calculated Fisher's Z doesn't meet expectation")

    def test_zval_R039(self):
        R = 0.39
        exp = 0.4118
        self.assertAlmostEqual(_fisher_z_transform(R), exp, places=4,
                               msg="Calculated Fisher's Z doesn't meet expectation")


class CompareTwoIndependentCorsCase(unittest.TestCase):
    def test_less(self):
        # test case from z-value and p-value from
        # http://comparingcorrelations.org/
        ra = 0.38
        na = 1200
        rb = 0.31
        nb = 980
        expected_z = 1.84
        expected_pval = 0.9674
        z, pval = compare_two_cors_ind(r_a=ra, n_a=na, r_b=rb, n_b=nb, alternative="less")
        self.assertAlmostEqual(z, expected_z, places=2, msg="Calculated z-value is not close enough to expectation")
        self.assertAlmostEqual(pval, expected_pval, places=2, msg="Calculated pval is not close enough to expectation")

    def test_greater(self):
        # test case from z-value and p-value from
        # http://vassarstats.net/rdiff.html
        ra = 0.38
        na = 1200
        rb = 0.31
        nb = 980
        expected_z = 1.84
        expected_pval = 0.0329
        z, pval = compare_two_cors_ind(r_a=ra, n_a=na, r_b=rb, n_b=nb, alternative="greater")
        self.assertAlmostEqual(z, expected_z, places=2, msg="Calculated z-value is not close enough to expectation")
        self.assertAlmostEqual(pval, expected_pval, places=2, msg="Calculated pval is not close enough to expectation")

    def test_twosided(self):
        # test case from z-value and p-value from
        # http://vassarstats.net/rdiff.html
        ra = 0.38
        na = 1200
        rb = 0.31
        nb = 980
        expected_z = 1.84
        expected_pval = 0.0658
        z, pval = compare_two_cors_ind(r_a=ra, n_a=na, r_b=rb, n_b=nb, alternative="two-sided")
        self.assertAlmostEqual(z, expected_z, places=2, msg="Calculated z-value is not close enough to expectation")
        self.assertAlmostEqual(pval, expected_pval, places=2, msg="Calculated pval is not close enough to expectation")


if __name__ == '__main__':
    unittest.main()
