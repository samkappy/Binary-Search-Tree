class TreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def _init_(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursively(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value > node.value:
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = TreeNode(value)
    
    def delete(self, value):
        self.root = self._delete_node(self.root, value)
    
    def _delete_node(self, node, value):
        if not node:
            return None
        
        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._find_min_node(node.right)
                node.value = min_node.value
                node.right = self._delete_node(node.right, min_node.value)
        return node
    
    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node
    
    def height(self):
        return self._calculate_height(self.root)
    
    def _calculate_height(self, node):
        if not node:
            return -1
        left_height = self._calculate_height(node.left)
        right_height = self._calculate_height(node.right)
        return max(left_height, right_height) + 1
 
    def print_level_and_height(self, value):
        node = self._find_node(self.root, value)
        if node:
            level = self._calculate_level(self.root, value)
            height = self._calculate_height(node)
            print(f"Level: {level}, Height: {height}")
        else:
            print("Node not found in the BST.")
    
    def _find_node(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._find_node(node.left, value)
        else:
            return self._find_node(node.right, value)
    
    def _calculate_level(self, node, value, level=0):
        if not node:
            return -1
        if node.value == value:
            return level
        if value < node.value:
            return self._calculate_level(node.left, value, level + 1)
        else:
            return self._calculate_level(node.right, value, level + 1)

# Create BST from the given array
arr = [30, 20, 40, 10, 25, 35, 45, 5, 15]
bst = BST()
for num in arr:
    bst.insert(num)