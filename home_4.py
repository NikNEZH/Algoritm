import random


class RedBlackTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.color = 'RED'

    def __init__(self):
        self.root = None

    def find(self, value): 
        cur = self.root
        while cur:
            if cur.value == value:
                return True
            if cur.value < value:
                cur = cur.right
            else:
                cur = cur.left
        return False

    def print_tree(self):
        self._print_tree(self.root, '')

    def _print_tree(self, node, prefix):
        if node is None:
            return
        print(prefix + str(node.value))
        if node.left:
            print(prefix + 'L:', node.left.value)
        if node.right:
            print(prefix + 'R:', node.right.value)
        self._print_tree(node.left, prefix + '  ')
        self._print_tree(node.right, prefix + '  ')

    def insert(self, value):
        new_node = self.Node(value)
        new_node.color = 'RED'
        if self.root is None:
            new_node.color = 'BLACK'
            self.root = new_node
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.right
            self.fix_inserted_node(new_node)

    def fix_inserted_node(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'BLACK'

    def left_rotate(self, node):
        new_node = node.right
        node.right = new_node.left
        if new_node.left is not None:
            new_node.left.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        new_node.left = node
        node.parent = new_node

    def right_rotate(self, node):
        new_node = node.left
        node.left = new_node.right
        if new_node.right is not None:
            new_node.rig
            ht.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        new_node.right = node
        node.parent = new_node


tree = RedBlackTree()
n = 5
numbers = []
for i in range(n):
    random_number = random.randint(5, 100)
    numbers.append(random_number)
for i in numbers:
    tree.insert(i)

tree.print_tree()