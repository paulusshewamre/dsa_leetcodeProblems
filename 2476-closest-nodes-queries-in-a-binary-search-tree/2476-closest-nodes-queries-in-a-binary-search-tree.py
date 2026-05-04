# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sortedValues = []

        def inorder(root):
            if root:
                inorder(root.left)
                sortedValues.append(root.val)
                inorder(root.right)
        
        inorder(root)

        answer = []

        for q in queries:
            index = bisect.bisect_left(sortedValues, q)

            if index < len(sortedValues) and sortedValues[index] == q:
                mini = q
            else:
                mini = sortedValues[index-1] if index > 0 else -1

            if index < len(sortedValues):
                maxi = sortedValues[index]
            else:
                maxi = -1

            answer.append([mini, maxi])
    
        return answer

