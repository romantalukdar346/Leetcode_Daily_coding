def findMedianSortedArrays(self, nums1, nums2):
        import statistics as st
        return st.median(sorted(nums1 + nums2))