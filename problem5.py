## Three sum closest

## 16 

from typing import List  

class ThreeSumClosest:
    def __init__(self, nums:List[int],target:int) -> int:

        ## this problem is mostly with the same logic of two pointer binary search with distance calculation 

        nums.sort()
        n = len(nums)

        #edge case if the array has only three elements then return their sum 
        if n == 3:
            return sum(nums)

        min_sum = sum(nums[:3])
        max_sum = sum(nums[-3:])

        ## checks for the closest sum with the naive approach checks 
        if min_sum >= target:
            return min_sum 
        if max_sum <= target:
            return max_sum 

        ## the reason for the above code block is to check whether the target has the initial sum ,  so we can skip this pointer methods 

        
        three_sum_close = None # declared the final return variable 
        interval = float("inf") # placeholder interval will update based on the loop fix 

        for i in range(n-1):
            l = i+1 
            r = n-1 

            while l < r: 

                total = nums[i] + nums[l] + nums[r]
                pointer_interval = abs(total-target)

                if pointer_interval < interval:
                    interval = pointer_interval  #gradient descent minimization approach 
                    three_sum_close = total 
                
                if total == target:
                    return target 
                
                if total < target:
                    l += 1 
                
                else:
                    r -= 1 
                
        
        return three_sum_close 
        




