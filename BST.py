"""
This module was provided Professor Paul Allison at Queen's University
This is NOT my code. It is only used to aid in my Directory. Please
credit him if you decide to use this code. Thanks.
"""

"""
This module implements binary search trees.
The tree elements may be of any type.  Duplicates are not allowed.
"""

import random # used in deleteHelper and randTree
import math # used in averageHeight

# A BST node is a dict with three elements:
# 1. data: the value in the node
# 2. left: a reference to the left subtree
# 3. right: a reference to the right subtree

# creates an empty tree
def createEmptyTree():
    return None

# adds a value to a BST and returns a pointer to the modified BST
def add(tree, value):
    if tree == None:
        return {'data':value, 'left':None, 'right':None}
    elif value[0] < tree['data'][0]:
        tree['left'] = add(tree['left'],value)
        return tree
    elif value[0] > tree['data'][0]:
        tree['right'] = add(tree['right'],value)
        return tree
    else: # value == tree['data']
        return tree # ignore duplicate

# returns the height of a BST (length of maximum path from root to leaf).
# The height of an empty tree is 0.
def height(tree):
    if tree == None:
        return 0
    else:
        return 1 + max(height(tree['left']),height(tree['right']))
        

# searches a tree for a value and returns True if the
# value is in the tree
def search(tree, value):
    if tree == None:
        return False
    elif value == tree['data']:
        return True
    elif value < tree['data']:
        return search(tree['left'],value)
    else: # value > tree['data']
        return search(tree['right'],value)

# creates a list of the elements in the tree, in sorted order
def toList(tree):
    if tree == None:
        return []
    else:
        return toList(tree['left']) + [tree['data']] + toList(tree['right'])

# Prints an indented display of the tree -- useful for debugging.
# The output will look kind of like a sideways version of a drawing
# of the tree.
def display(tree, indent=0):
    if tree == None: # empty
        pass
    else:
        # right tree first (so it's on the right when you tilt your
        # head to the left to look at the display)
        display(tree['right'],indent+1)
        print("    "*indent + str(tree['data']))
        # now the left tree
        display(tree['left'],indent+1)



def randTree(size=10):
    """
    Helper for testing: creates a tree with random integers.
    The parameter gives the number of integers to put into
    the tree.
    """
    tree = None
    # Put the numbers 1-size into a list and shuffle it into random order.
    nums = range(1,size+1)
    random.shuffle(nums)
    for n in nums:
        tree = add(tree,n)
    return tree

    

def main():
    myTree = createEmptyTree()  #create an empty tree
    #Create a tree with the nodes [20, 2, 25, 14, 75, 93]
    #Note that the add function always returns the root of the BST!
    myTree = add(myTree, [5,6,7,8])
    myTree = add(myTree, [8,7,5,3])
    myTree = add(myTree, [12.1,43,55,22])
    myTree = add(myTree, [8,8,8,8])
    myTree = add(myTree, [75,65,5,4])
    myTree = add(myTree, [2,3,4,5])
    myTree = add(myTree, [1,2,3,4])
    #display the tree -- awkward -- you need to look at it sideways -- sorry :-)
    display(myTree)
    
    
    
main()


        
    
        
