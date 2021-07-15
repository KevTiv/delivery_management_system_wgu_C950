# Name : Kevin Tivert
# Student ID: 001372496

# O(1)
class BinarySearchTreeNode: 
    # Constructor
    # O(1)
    # This function initialize the BSTNode object
    def __init__(self, data, parent, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


    # O(1)
    # This function counts the number of node present in the tree.
    def count(self):      
        leftCount = 0
        rightCount = 0
        if self.left != None:
            leftCount = self.left.count()
        if self.right != None:
            rightCount = self.right.count()
        return 1 + leftCount + rightCount

    # O(n)
    # This function from a given node looks for the succesor of the node in the tree
    def get_successor(self):     
         # Successor in right subtree, if present
        if self.right != None:
            successor = self.right
            while successor.left != None:
                successor = successor.left
            return successor

        # or else the successor is up the tree
        # loop through the tree until a parent is found from the left
        node = self
        while node.parent != None and node == node.parent.right:
            node = node.parent
        return node.parent


    # O(1)
    # This function replace the value of a node given the 
    # condition present in the code below
    def replace_child(self, current_child, new_child):    
        if current_child is self.left:
            self.left = new_child
            if self.left:
                self.left.parent = self
        elif current_child is self.right:
            self.right = new_child
            if self.right:
                self.right.parent = self


# O(1)
class BinarySearchTreeIterator:
    # Constructor
    # O(1)
    # This function initialize the BSTInterator object
    def __init__(self, node):     
        self.node = node

    # For Python versions >= 3
    # O(1)
    # Overloaded next function 
    def __next__(self):
        return self.next()

    # For Python versions < 3
    # O(1)
    # Overloaded next function 
    def next(self):
        if self.node == None:
            raise StopIteration
        else:
            current = self.node.data
            self.node = self.node.get_successor()
            return current
   

# O(n)
class Set:
    # Constructor
    # O(1)
    # This function initialize the set object
    def __init__(self, get_key_function=None):
        self.storage_root = None
        if get_key_function == None:
           # By default, the key is itself
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function

    # O(n)
    # This function interates through the tree looking for the key (self)
    def __iter__(self):
        if self.storage_root == None:
            return BinarySearchTreeIterator(None)
        minNode = self.storage_root
        while minNode.left != None:
            minNode = minNode.left
        return BinarySearchTreeIterator(minNode)

    # O(n)
    # This function a new element to the tree
    def add(self, new_element):
        new_elementKey = self.get_key(new_element)
        if self.node_search(new_elementKey) != None:
            return False

        newNode = BinarySearchTreeNode(new_element, None)
        if self.storage_root == None:
            self.storage_root = newNode
        else:
            node = self.storage_root
            while node != None:
                if new_elementKey < self.get_key(node.data):
                    # Go left
                    if node.left:
                        node = node.left
                    else:
                        node.left = newNode
                        newNode.parent = node
                        return True
                else:
                    # Go right
                    if node.right:
                        node = node.right
                    else:
                        node.right = newNode
                        newNode.parent = node
                        return True

    # O(n)
    # This function loop through the tree looking for a given set object
    # if nothing is found add() is called with the set key (self)
    def difference(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) == None:
                result.add(element)
        return result

    # O(n)
    # This function returns the truth value of the condition: Is self in the set.
    # If not in set, add() is called.
    def filter(self, predicate):
        result = Set(self.get_key)
        for element in self:
            if predicate(element):
                result.add(element)
        return result

    # O(n)
    # This function returns the truth value of the condition: Is self in the other set elements.
    # If yes, add() is called.
    def intersection(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) != None:
                result.add(element)
        return result

    # O(1)
    # This function determines the size of tree
    def __len__(self):
        if self.storage_root == None:
            return 0
        return self.storage_root.count()

    # O(n)
    # This function returns a map list of a set.
    def map(self, map_function):
        result = Set(self.get_key)
        for element in self:
            new_element = map_function(element)
            result.add(new_element)
        return result

    # O(n)
    # This function search the tree for a given node.
     # This function is called by the function remove.
    def node_search(self, key):
        # Search the BST
        node = self.storage_root
        while (node != None):
            # Get the node's key
            node_key = self.get_key(node.data)

            # Compare against search key
            if node_key == key:
                return node
            elif key > node_key:
                node = node.right
            else:
                node = node.left
        return node

    # O(1)
    # This function remove a node from the tree.
    # This function is called by the function remove.
    def remove_node(self, node_to_remove):
        if node_to_remove != None:
            # Internal node with 2 children
            if node_to_remove.left != None and node_to_remove.right != None:
                successor = node_to_remove.get_successor()

                # Copy value from the successor
                dataCopy = successor.data

                # Remove successor
                self.remove_node(successor)

                # Replace node_to_remove with successor 
                node_to_remove.data = dataCopy

            # Root node (with 1 or 0 children)
            elif node_to_remove is self.storage_root:
                if node_to_remove.left != None:
                    self.storage_root = node_to_remove.left
                else:
                    self.storage_root = node_to_remove.right

                if self.storage_root:
                    self.storage_root.parent = None

            # Internal node with left child only
            elif node_to_remove.left != None:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left)

            # Case 4: Internal node with right child only, or leaf node
            else:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.right)

    
    # O(n)
    # This function remove a node from the tree.
    # This function calls node_search() and remove_node() to accomplish its task.
    def remove(self, key):
        self.remove_node(self.node_search(key))
    
    # O(n)
    # This function search a node from the tree.
    # This function calls node_search()to accomplish its task.
    def search(self, key):
        # Search the BST
        node = self.node_search(key)
        if node != None:
            return node.data
        return None

    # O(n)
    # this function add nodes in both set.
    # This function calls add() to accomplish its task.
    def union(self, other_set):
        result = Set(self.get_key)
        for element in self:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result