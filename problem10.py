## XOR After Range Multiplication Queries I
from typing import List

class XorMul:
    def __init__(self,  nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)
        q = len(queries)

        for i in range(q):
            l = queries[i][0]
            r = queries[i][1]
            k = queries[i][2]
            v = queries[i][3]

            while l <= r and l < n:
                nums[l] = (nums[l] * v) % (10 ** 9 + 7)
                l += k 
            
        

        base = 0 
        for i in nums:
            base ^= i 
        

        return base 