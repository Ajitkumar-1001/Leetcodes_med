## Design a Food Rating System 

## Problem-2353
from typing import Optional,List
from collections import defaultdict
import heapq

class FoodRatingSystem:
    def __init__(self, foods:List[str],ratings:List[int],cuisine:List[str]):

        self.food_info = { } 
        self.cuisine_info = defaultdict(list)

        for food,rate,cuis in zip(foods,ratings,cuisine):
            self.food_info[food] = (cuis,rate)
            heapq.heappush(self.cuisine_info[cuis],(-rate,food)) ## here we use -rate because, the heapq returns the smallest of the element ,,  but we need the maximum number so


    
    def changeRating(self, food: str, newRating: int) -> None:
        # now we decouple the items 
        cuis, _rate = self.food_info[food]
        self.food_info[food] = (cuis,newRating)
        heapq.heappush(self.cuisine_info[cuis],(-newRating,food))

    
    def highestRated(self, cuisine: str) -> str:
        heap_structure  = self.cuisine_info[cuisine]

        while True:
            rating , food = heap_structure[0]
            _cuisine, _rating = self.food_info[food]

            # valid if rating matches the most recent rating
            if _cuisine == cuisine and rating == -_rating:
                return food

            # otherwise outdated entry, discard
            heapq.heappop(heap_structure)






