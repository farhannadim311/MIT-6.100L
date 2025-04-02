# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 =  Node(8, Node(2,Node(1), Node(6)), Node(10))
tree2 =  Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 =  Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    if (tree.get_left_child() == None and tree.get_right_child() == None):
        return 0
    elif (tree.get_left_child() is not None and tree.get_right_child() is not None):
        height =  max(find_tree_height(tree.get_left_child()), find_tree_height(tree.get_right_child()))
        return height + 1
    elif (tree.get_left_child() is not None and tree.get_right_child() is None):
        height = find_tree_height(tree.get_left_child())
        return height + 1
    else:
        height = find_tree_height(tree.get_right_child())
        return height + 1

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    tree_left = tree.get_left_child()
    tree_right = tree.get_right_child()
    tree_value = tree.get_value()
    if (tree_left == None and tree_right == None):
        return True
    elif (tree_left == None and tree_right is not None):
        tree_right_value = tree_right.get_value()
        if (compare_func(tree_right_value, tree_value) == False):
            return False
        else:
            return is_heap(tree_right, compare_func)
    elif (tree_left is not None and tree_right is None):
        tree_left_value = tree_left.get_value()
        if (compare_func(tree_left_value, tree_value) == False):
            return False
        else:
            return is_heap(tree_left, compare_func)
    else:
        tree_right_value = tree_right.get_value()
        tree_left_value = tree_left.get_value()
        if(compare_func(tree_right_value, tree_value) == False or compare_func(tree_left_value, tree_value) == False):
            return False
        return is_heap(tree_left, compare_func) and is_heap(tree_right, compare_func)
        
  



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
