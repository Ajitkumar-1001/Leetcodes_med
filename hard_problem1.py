# median of two sorted arrays 

from typing import List 

class Median: 
    def __init__(self, nums1 : List[int], nums2: List[int]) -> float: 

        if not nums1 or not nums2:
            return float(0)
        
        final_array = [] 

        while nums1 and nums2:
            if nums1 not in final_array:
                final_array.append(nums1)
            if nums2 not in final_array:
                final_array.append(nums2)

        # lets use two pointers to find the median 
        l = 0 
        r = len(final_array)-1 
        while l <= r:
            mid = (l+r)//2
            if final_array[mid] == target:
                return mid
            elif final_array[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        return final_array[mid]






