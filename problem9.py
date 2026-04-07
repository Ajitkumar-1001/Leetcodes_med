
from typing import List

class ProductExceptSelf:
    def __init__(self, nums:List[int]) ->List[int]:

        n = len(nums)
        l = [0] * n 
        r = [0] * n 

        l[0] = 1 
        r[n-1] = 1 

        for i in range(1,n):
            l[i] = l[i-1] * nums[i-1] 
        
        for j in range(n-2,-1,-1):
            r[j] = r[j+1] * nums[j+1]
        
        ans = [0] * n 
        for i in range(n):
            ans[i] = l[i] * r[i] 
        
        return ans 
        


