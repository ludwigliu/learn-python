import random

class BinarySearchTree:
    '''Implementation of BinarySearchTree '''
    def __init__(self):
        self.root = None
    
    def put(self, key, value):
        self.root = self.put2(self.root, key, value)
    def put2(self, node, key, value):
        if node == None:
            return Node(key, value)
        
        cmp = key - node.key
        if cmp < 0:
            node.left = self.put2(node.left, key, value)
        elif cmp > 0:
            node.right = self.put2(node.right, key, value)
        else:
            node.value = value
        return node

    def get(self, key):
        return self.get2(self.root, key)
    def get2(self, node, key):
        if node == None:
            return None

        cmp = key - node.key
        if cmp < 0:
            return self.get2(node.left, key)
        elif cmp > 0:
            return self.get2(node.right, key)
        else:
            return node.value
    
    def min(self):
        return self.min2(self.root)
    def min2(self, node):
        if node.left == None:
            return node
        else :
            return self.min2(node.left)
    
    def max(self):
        return self.max2(self.root)
    def max2(self, node):
        if node.right == None:
            return node
        else :
            return self.max2(node.right)
    
    def delete(self, key):
        return self.delete2(self.root, key)
    def delete2(self, node, key):
        if node == None:
            return None
        
        cmp = key - node.key
        if cmp < 0:
            # remember to return the value, else left is gone
            node.left = self.delete2(node.left, key)
        elif cmp > 0:
            # remember to return the value, else right is gone
            node.right = self.delete2(node.right, key)
        else:
            # found the node that will be removed 
            if node.right == None: return node.left
            if node.left == None: return node.right
            # both left and right node are not empty
            temp = node
            # 后继结点
            node = self.min2(node.right)
            # 右子树删除后继结点后的子树
            node.right = self.deleteMin2(temp.right)
            node.left = temp.left
        # here the value returned includes each if condition
        return node

    def deleteMin(self):
        return self.deleteMin2(self.root)
    def deleteMin2(self, node):
        if node.left == None:
            return node.right
        else :
            node.left = self.deleteMin2(node.left)
            return node
    # print all node with preorder sequence
    def print(self):
        print()
        print("Print all key value in preorder")
        self.print2(self.root)
    def print2(self, node):
        if node == None:
            return None
        if node.left != None:
            self.print2(node.left)
            print("{0} -> {1}".format(node.key, node.value))
            self.print2(node.right)
        elif node.right != None:
            print("{0} -> {1}".format(node.key, node.value))
            self.print2(node.right)
        else:
            print("{0} -> {1}".format(node.key, node.value))

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def main():
    words = "The Decadents of the late 19th century and the Modernists of the early 20th looked to continental European individuals and movements for inspiration Nor was attraction toward European intellectualism dead in the late 20th century for by the mid 1980s the approach known as structuralism a phenomenon predominantly French and German in origin infused the very study of English literature itself in a host of published critical studies and university departments"
    root = BinarySearchTree()
    key = None
    for word in words.split():
        key = random.randint(1, 100)
        print("{0} -> {1}".format(key, word))
        root.put(key, word)
    
    root.print()
    print("min key {0} value {1}".format(root.min().key, root.min().value))
    print("max key {0} value {1}".format(root.max().key, root.max().value))
 
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.delete(root.min().key)
    root.print()
 
if __name__ == "__main__":
    main()