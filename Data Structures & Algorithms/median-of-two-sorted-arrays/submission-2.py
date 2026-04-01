class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        l1,r1 = 0,len(nums1)-1
        while True:
            i = (l1+r1) // 2    # partition in nums1
            j = half - i - 2    # partition in nums2

            # this is to allow the code to run if the partition is in the edge of the array
            left1 = nums1[i] if i >= 0 else float("-infinity")
            right1 = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            left2 = nums2[j] if j >= 0 else float("-infinity")
            right2 = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            # check that the partition is good
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1,right2)   # odd case-return middle
                return (max(left1,left2)+min(right1,right2)) / 2    # even case-return average of 2 middles
            elif left1 > right2:    # remove element from left1's array and add element to right2's array
                r1 = i - 1
            else:   # remove element from from left2's array and add element to right1's array
                l1 = i + 1