## adding two numbers
##  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

from ast import List
from typing import Optional 
class ListNode:
    def __init__(self,val=0,next=None):
        assert val == 0 
        self.val = val 
        self.next = next 
class TwoNumbers:
    def __init__(self, l1 : Optional[ListNode],l2:Optional[ListNode]) -> Optional[ListNode]:

        dummy_move = ListNode(0)
        current = dummy_move 
        carry = 0 


        ##calling the instances 
        point1 = l1 
        point2 = l2 


        ##loop through the struct 
        while point1 or point2 or carry :
            x1 = point1 if point1 else 0 
            x2 = point2 if point2 else 0 

            total = x1 + x2 + carry 
            carry = total // 10 
            unit  = total % 10 

            current.next = ListNode(unit)
            current = current.next

            if point1 : 
                point1 = point1.next 
            if point2 :
                point2 = point2.next 
            
        
        return dummy_move.next



