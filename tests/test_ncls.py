import struct

from ncls import NCLS

import numpy as np


import struct
# 64 bit architecture?
if struct.calcsize("P") * 8 == 64:

    starts = np.array([5, 9_223_372_036_854_775_805], dtype=np.int64)

    ends = np.array([6, 9_223_372_036_854_775_807], dtype=np.int64)

    ids = np.array([2147483647, 3], dtype=np.int64)

    def test_ncls():
        # ids = starts

        print(starts, ends, ids)

        ncls = NCLS(starts, ends, ids)
        print(ncls)
        print(ncls.intervals())

        assert list(ncls.find_overlap(0, 2)) == []
        print("aaa", list(ncls.find_overlap(9_223_372_036_854_775_805, 9_223_372_036_854_775_806)))
        assert list(ncls.find_overlap(0, 9_223_372_036_854_775_806)) == [(5, 6, 2147483647), (9223372036854775805, 9223372036854775807, 3)]

        r, l = ncls.all_overlaps_both(starts, ends, ids)
        assert list(r) == [2147483647, 3]
        assert list(l) == [2147483647, 3]

    def test_all_containments_both():

        starts = np.array([1291845632, 3002335232], dtype=np.int64)
        ends = np.array([1292894207, 3002597375], dtype=np.int64)
        ids = np.array([0, 1], dtype=np.int64)

        ncls = NCLS(starts, ends, ids)
        subs, covers = ncls.all_containments_both(starts, ends, ids)

        print(ncls.intervals())

        assert list(subs) == [0, 1] == list(covers)

else:
    
    starts = np.array([5, 2_147_483_645], dtype=np.int32)

    ends = np.array([6, 2_147_483_646], dtype=np.int32)

    ids = np.array([0, 3], dtype=np.int32)

    def test_ncls():
        # ids = starts

        print(starts, ends, ids)

        ncls = NCLS(starts, ends, ids)
        print(ncls)
        print(ncls.intervals())

        assert list(ncls.find_overlap(0, 2)) == []
        assert list(ncls.find_overlap(0, 2_147_483_647)) == [(5, 6, 0), (2_147_483_645, 2_147_483_646, 3)]

        r, l = ncls.all_overlaps_both(starts, ends, ids)
        assert list(r) == [0, 3]
        assert list(l) == [0, 3]

    def test_all_containments_both():

        starts = np.array([5, 10], dtype=np.int32)
        ends = np.array([6, 50], dtype=np.int32)
        ids = np.array([0, 1], dtype=np.int32)

        ncls = NCLS(starts, ends, ids)
        subs, covers = ncls.all_containments_both(starts, ends, ids)

        print(ncls.intervals())

        assert list(subs) == [0, 1] == list(covers)
