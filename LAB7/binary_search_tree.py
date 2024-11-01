class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

class BinarySearchTree:
    # ... (previous code)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

class BinarySearchTree:
    # ... (previous code)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# Test search
print(bst.search(4))  # Should return a Node
print(bst.search(9))  # Should return None


class BinarySearchTree:
    # ... (previous code)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

# Test traversals
print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())


class BinarySearchTree:
    # ... (previous code)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())


# Exercises


#1. Implementing a method to find the maximum value in the BST

class BinarySearchTree:

    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.value if current else None

# Example usage:
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)
print("Maximum value:", bst.find_max())


#2. Adding a method to count the total number of nodes in the BST

class BinarySearchTree:

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

# Example usage:
print("Total nodes:", bst.count_nodes()) 


#3. Implementing a level-order traversal (Breadth-First Search) for the BST

from collections import deque

class BinarySearchTree:

    def level_order_traversal(self):
        result = []
        if not self.root:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# Example usage:
print("Level-order traversal:", bst.level_order_traversal())


#4. Creating a method to find the Height of the BST

class BinarySearchTree:
    

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node:
            return -1  # or 0, depending on whether height of a single node is considered 0 or 1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

# Example usage:
print("Height of BST:", bst.height())


#5. Implementing a method to check if the Tree is a Valid BST

class BinarySearchTree:
    

    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))

# Example usage:
print("Is valid BST:", bst.is_valid_bst())
