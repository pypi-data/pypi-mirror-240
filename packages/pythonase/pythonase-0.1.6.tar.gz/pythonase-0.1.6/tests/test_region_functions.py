#!/usr/bin/env python
# coding=utf-8

#  Copyright (c) Li Yao 2022. No unauthorized redistribution allowed.

# Created by: Li Yao (yaoli.gm@gmail.com)
# Created on: 2022-01-29
import os
import unittest

import numpy as np
import pybedtools

from pythonase.region import generate_gc_matched_random_regions, profile_regions_ref_point, build_upset_info
from pythonase.plot.meta import plot_meta_profiles


class GCMatchRandomRegionsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.fa = os.path.join(current_dir, "datasets/test.fa")
        self.test_size = os.path.join(current_dir, "test_size.txt")
        test_seq_len = 284123

        with open(self.test_size, "w") as fh:
            fh.write(f"chr22\t{test_seq_len}\n")

        # build 10 random regions with sizes between 100~1000
        self.test_region_file = os.path.join(current_dir, "test_regions.bed")
        region_sizes = np.random.randint(100, 1000, 10)
        regions_starts = np.random.randint(0, test_seq_len - 1000, 10)

        with open(self.test_region_file, "w") as fh:
            for size, start in zip(region_sizes, regions_starts):
                fh.write(f"chr22\t{start:d}\t{start + size:d}\n")

    def tearDown(self) -> None:
        os.remove(self.test_size)
        os.remove(self.test_region_file)

    def test_region_generation(self):
        acceptable_deviation = 0.05
        gcmr = generate_gc_matched_random_regions(input_region_file=self.test_region_file,
                                                  genome_size_file=self.test_size,
                                                  genome_fasta_file=self.fa,
                                                  acceptable_deviation=acceptable_deviation)
        gcmr = pybedtools.BedTool.from_dataframe(gcmr)

        n_sampled_regions = gcmr.count()
        # expectation: should return at least one sampled region
        self.assertTrue(n_sampled_regions > 0)
        # expectation: regions don't overlap with queries
        self.assertTrue(
            gcmr.intersect(
                pybedtools.BedTool(self.test_region_file), v=True
            ).count() == n_sampled_regions
        )
        # expectation: regions should fit the deviation constraints if possible
        self.assertTrue(gcmr.filter(lambda x: float(x[4]) <= acceptable_deviation).count() == n_sampled_regions)


class ProfileRefPointExtRegionsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_bw = os.path.join(
            current_dir,
            "datasets/test.bw")
        self.test_tss_file = os.path.join(
            current_dir,
            "datasets/test_tss.bed")
        self.test_full_file = os.path.join(
            current_dir,
            "datasets/test_full.bed")
        self.tss_test_bed = pybedtools.BedTool(self.test_tss_file)
        self.full_test_bed = pybedtools.BedTool(self.test_full_file)
        self.profiled_dfs = []

    def test_center_tss_consistency(self):
        score_dict = {"test_bw": self.test_bw}

        # test case 1: make sure the extension behavior is consistent
        for na_as_zero in (True, False):
            dfs = []
            for ext_type, bed_obj in zip(("center", "TSS"),
                                         (self.tss_test_bed, self.full_test_bed)):
                df = profile_regions_ref_point(region_lst=(bed_obj,),
                                               label_lst=(ext_type,),
                                               ref_point=ext_type,
                                               disable_bootstrap=True,
                                               score_bws=score_dict,
                                               chromosome_size="hg38",
                                               na_as_zero=na_as_zero,
                                               extension_left=300, extension_right=300,
                                               stats="mean", n_bins=100, n_workers=1)
                self.profiled_dfs.append(df)
                dfs.append(df)
            self.assertTrue(any(dfs[0].stats.values == dfs[1].stats.values))
            self.assertTrue(np.allclose(dfs[0].stats_u.values, dfs[1].stats_u.values, rtol=0.05))
            self.assertTrue(np.allclose(dfs[0].stats_l.values, dfs[1].stats_l.values, rtol=0.05))

        # test case 2: generate meta plot
        import seaborn as sns
        for df in self.profiled_dfs:
            g = plot_meta_profiles(df)
            # return should be instances sns.FacetGrid
            self.assertTrue(isinstance(g, sns.axisgrid.FacetGrid))
            # should have one col
            self.assertTrue(len(g.axes) == 1)
            # all subplots should have exactly one lines
            self.assertTrue(len(g.axes[0, 0].get_lines()) == 1)
            # should have one CI shadow (Polygon collection) on the plot
            self.assertTrue(len(g.axes[0, 0].collections) == 1)


class RegionOverlapProfilingTestCases(unittest.TestCase):
    def test_upset_core(self):
        import pandas as pd
        demo_chr = "chr1"
        max_size = 10000
        region_sizes = np.random.randint(100, max_size, 10)
        regions_start = np.random.randint(0, 2492406, 1)
        pool = []
        for i, size in enumerate(region_sizes):
            pool.append((demo_chr, int(regions_start * (i+1)), int(regions_start * (i+1) + size)))

        set_one = pybedtools.BedTool([pool[0], pool[1], pool[2], pool[3], pool[4]])
        set_two = pybedtools.BedTool([pool[3], pool[4], pool[5], pool[6], pool[7]])
        set_three = pybedtools.BedTool([pool[1], pool[6], pool[7], pool[8], pool[9]])

        idx = pd.MultiIndex.from_tuples([(False, False, False),
                                         (False, False, True),
                                         (False, True, False),
                                         (False, True, True),
                                         (True, False, False),
                                         (True, False, True),
                                         (True, True, False),
                                         (True, True, True)],
                                        names=("A", "B", "C"))
        expectation = pd.Series(data=(0, 2, 1, 2, 2, 1, 2, 0),
                                index=idx)
        actual = build_upset_info(region_files=(set_one, set_two, set_three),
                                  labels=("A", "B", "C"))
        self.assertTrue(expectation.equals(actual))


if __name__ == '__main__':
    unittest.main()
