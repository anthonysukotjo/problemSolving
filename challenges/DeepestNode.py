'''
    Given a binary tree (root), find the value of the deepest node. If there is more than one deepest node, then return the leftmost one.

    Restraints
    n <= 100,000 where n is the number of nodes in the tree

    Example

        0
       / \
      5   9
         / \
        1   3
       / \
      4   2

> 4

    Explanation
    The nodes 2 and 4 have the same depth in the tree, so 4 is returned because it is leftmost between the two nodes.

    Before diving into the code, it may be helpful to
    - consider the problem, what is needed to determine the solution?
    - draw up your own potential solution

    Problem Link
    https://binarysearch.com/problems/Leftmost-Deepest-Tree-Node

'''

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# How did the author intend for the solution to work?

# def personalSolution(root):
#     if root is None:
#         return None
#     else reccur(root, 0)


# # finds max depth but doesnt return value
# def reccur(root, depth):
#     depth += 1
#     if root.left == None and root.right == None:
#         return depth
#     elif root.left = None:
#         return reccur(root.right, depth)
#     elif root.right = None:
#         return reccur(root.left, depth)

#     else:
#         return max(root.right, root.left)







#TODO fill in ???, find and repair any logical errors.
def solve(root):
    if root is None:
        return None
    def helper(root: TreeNode, depth):
        if root.left is None and root.right is  None:
            return (root.val, depth)
        l, r = (-1,-1) , (-1,-1)  
        if root.left is not None:
            l = helper(root.left, depth + 1)
        if root.right is not None:
            r = helper(root.right, depth + 1)

                        # looking at the depth
        if l[1] != -1 and l[1] >= r[1]:
            return l

        # either left doesnt exists or right is deeper than left
        elif r[1] != -1 :
            return r



# dont care about the value until the end
    return helper(root, 0)[0]






