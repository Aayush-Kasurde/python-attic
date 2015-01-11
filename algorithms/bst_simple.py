class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Btree():
    def __init__(self):
        self.root = None

    def insertNode(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.addNode(self.root, val)

    def addNode(self, node, val):
        if val <= node.val:
            if node.left:
                self.addNode(node.left, val)
            else:
                node.left = Node(val)
        elif val > node.val:
            if node.right:
                self.addNode(node.right, val)
            else:
                node.right = Node(val)
                
    def printNode(self, node = None):
        if node is None:
            node = self.root
        
        if node.left is not None:
            self.printNode(node.left)

        print node.val,
        
        if node.right is not None:
            self.printNode(node.right)

    def exists(self, val):
        return self.existsNode(val, self.root)
    
    def existsNode(self, val, node=None):        
        if node.val == val:
            return True
        elif val < node.val:
            print "%d is less than %d" %(val, node.val)
            if node.left:
                self.existsNode(val, node.left)
        elif val > node.val:
            print "%d is more than %d" %(val, node.val)
            if node.right:
                self.existsNode(val, node.right)

            

def main():
	btree = Btree()
	alist = [10, 9, 12, 6, 2, 1231, 123]

	for i in alist:
		print i,
		btree.insertNode(i)
	print "\n"
	btree.printNode()

	print "True" if btree.exists(10) else "False"

if __name__ == "__main__":
	main()