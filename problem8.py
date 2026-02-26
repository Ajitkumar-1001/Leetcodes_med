## 300
from typing import List 
from bisect import bisect_right,bisect_left

class LongestSequence:
    def __init__(self, nums:List[int])->List[int]:

        n = len(nums)

        track : List[int] =  []

        for i in nums: 
            x = bisect_left(track,i) 

            if x == len(track):
                track.append(x)
            else:
                track[x] = i 
            
        
        return track 