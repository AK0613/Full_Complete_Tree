# Full & Complete Binary trees
# Given a complete binary tree, count the number of nodes
import queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None
        self.elements = 0

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            self.elements += 1
        else:
            q = queue.Queue()
            q.put(self.root)
            # Visit all nodes and append them to the queue if they have a value or insert the value into an empty node (Left then right)
            while queue:
                current = q.get()

                if current.left is not None:
                    q.put(current.left)
                else:
                    current.left = node
                    self.elements += 1
                    break
                if current.right is not None:
                    q.put(current.right)
                else:
                    current.right = node
                    self.elements += 1
                    break

    def count_nodes(self, node) -> int:
        # If the tree is empty then it is complete
        if self.root is None:
            return 0
        # Find the height to the left and right of the tree
        left_h = self.left_height(node)
        right_h = self.right_height(node)

        # If the heights match, then calculate the number of nodes using the formula 2^h - 1
        if left_h == right_h:
            return 2 ** left_h - 1
        else:
            return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def left_height(self, node):
        height = 0
        while node:
            node = node.left
            height += 1
        return height

    def right_height(self, node):
        height = 0
        while node:
            node = node.right
            height += 1
        return height


__name__ = "__main__"

bt = BinaryTree()
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)
bt.add(6)

print(bt.elements)
print(bt.count_nodes(bt.root))
