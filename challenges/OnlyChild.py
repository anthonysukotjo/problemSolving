'''
    Given a binary tree root, return the number of nodes that are an only child. A node n is an only child if its parent has exactly one child (n)

    Constraints
    n <= 100,000 where n is the number of nodes in root

    Example

    root = 0
          / \
         4   2
            /
           1
          /
         3

    Output > 2

    Since 1 and 3 are both only the only children of their parent nodes

    Problem link
    https://binarysearch.com/problems/Only-Child

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mySolve(root):
    if root is None:
        return 0

    if root.left != None and root.right != None:
        return mySolve(root.left) + mySolve(root.right)

    elif root.left != None and root.right == None:
        return 1 + mySolve(root.left)

    elif root.left == None and root.right != None:
        return 1 + mySolve(root.right)

    else:
        return 0


# Not sure why this one doesnt work??
def solve(root):
    if root is None:
        return 0
    if root.left and root.right:
        return solve(root.right) + solve(root.left)

    #TODO add missing lines

    elif root.left and root.right is None:
        return 1 + solve(root.left) 

    elif root.left is None and root.right:
        return 1 + solve( root.right) 
    else:
        return 0
