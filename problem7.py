## Path sum 

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0 , left= None, right = None):
        self.val = val 
        self.right = right 
        self.left = left 


class PathSum:
    def __init__(self, root:TreeNode, targetSum:int) -> List[List[int]] :

        output : List[List[int]] = [ ]

        track : List[int] = [] 


        if not root: 
            return [] 
        

        def dfs(node:TreeNode, choice:List[int], total:int) -> None:

            if not node:
                return 
            
            total -= node.val 
            choice.append(node.val)

            if not node.right and not node.left:
                if total == 0:
                    output.append(choice.copy())
                
            else:
                dfs(node.left, choice, total)
                dfs(node.right, choice, total)
            
            choice.pop() 
            
        dfs(root,track,targetSum)

        return output 