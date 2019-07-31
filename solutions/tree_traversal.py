#! /usr/bin/env python

r"""Tree traversal

https://rosettacode.org/wiki/Tree_traversal

Implement a binary tree where each node carries an integer,   and implement:
pre-order, in-order, post-order, level-order traversal.

Use those traversals to output the following tree:

         1
        / \
       /   \
      /     \
     2       3
    / \     /
   4   5   6
  /       / \
 7       8   9

The correct output should look like this:

preorder:    1 2 4 7 5 3 6 8 9
inorder:     7 4 2 5 1 8 6 9 3
postorder:   7 4 5 2 8 9 6 3 1
level-order: 1 2 3 4 5 6 7 8 9

"""


class Node():
    """A Node is a binary tree element
    :param: content
    :param: (ref to a Node object)
    :param: (ref to a Node object)
    """

    def __init__(self, content, left=None, right=None):
        self._content = content
        self._left = left
        self._right = right

    @property
    def left(self):
        """getter for the left child Node"""
        return self._left

    @property
    def right(self):
        """getter for the right child Node"""
        return self._right

    def __str__(self):
        """implement the str()"""
        return str(self._content) + ' '

    def dump(self):
        """print this node's state"""
        print("Node {0} {1} <-> {2}".format(
            str(self._content), str(self.left), str(self.right)))

    def preorder(self):
        """Traverse the tree in preorder"""
        if self is not None:
            print(str(self), end='')
            Node.preorder(self.left)
            Node.preorder(self.right)

    def postorder(self):
        """Traverse the tree in postorder"""
        if self is not None:
            Node.postorder(self.left)
            Node.postorder(self.right)
            print(str(self), end='')


def make_tree():
    r"""
         1
        / \
       /   \
      /     \
     2       3
    / \     /
   4   5   6
  /       / \
 7       8   9
    """

    root = Node(
        1,
        left=Node(
            2,
            left=Node(
                4,
                left=Node(7)
            ),
            right=Node(5)
        ),
        right=Node(
            3,
            left=Node(
                6,
                left=Node(8),
                right=Node(9)
            )
        )
    )
    return root


def main():
    """main"""
    tree = make_tree()
    tree.preorder()
    print("")
    tree.postorder()
    print("")


if __name__ == '__main__':
    main()
