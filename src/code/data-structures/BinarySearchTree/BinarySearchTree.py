class BinarySearchTree:
    class _Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.__node_count = 0
        self.__root = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__node_count

    def add(self, val):
        if self.contains(val):
            return False
        self.__root = self.__add_node(self.__root, val)
        self.__node_count += 1
        return True

    def __add_node(self, node, val):
        if not node:
            node = self.__Node(val)
        else:
            if node.val > val:
                node.left = self.__add_node(node.left, val)
            else:
                node.right = self.__add_node(node.right, val)
        return node

    def remove(self, val):
        if not self.contains(val):
            return False

        self.__root = self.__remove_node(self.__root, val)
        self.__node_count -= 1
        return True

    def __remove_node(self, node, val):
        if not node:
            return None

        if node.val > val:
            node.left = self.__remove_node(node.left, val)
        elif node.val < val:
            node.right = self.__remove_node(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp_node = self.__find_min(node.right)
                node.val = temp_node.val
                node.right = self.__remove_node(node.right, temp_node.val)

                # We can find the maximum node on the left subtree
                # temp_node = self.__find_max(node.left)
                # node.val = temp_node.val
                # node.left = self.__remove_node(node.left, temp_node.val)
        return node

    def __find_min(self, node):
        while node.left:
            node = node.left
        return node

    def __find_max(self, node):
        while node.right:
            node = node.right
        return node

    def contains(self, val):
        return self.__contains(self.__root, val)

    def __contains(self, node, val):
        if not node:
            return False

        if node.val > val:
            self.__contains(node.left, val)
        elif node.val < val:
            self.__contains(node.right, val)
        else:
            return True

    def height(self):
        return self.__height(self.__root)

    def __height(self, node):
        if not node:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1
