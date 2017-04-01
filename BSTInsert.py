class Node:
	def __init__(self):
		#print "Node object constructor called"
		self.lchild = None
		self.rchild = None
		self.val    = 0

root = None	
		
def makeTree(var,node):
	global root
	nextNode = node
	
	if var > 0:
		tempNode = Node()
		tempNode.val = var
		if nextNode != None:
			print "root is {0}".format(nextNode.val)
		while True:
			if node == None: #root null
				tempNode.val = var
				#print "Node inserted as root"
				root = tempNode
				return True
			else:
				if nextNode.val > var:
					if nextNode.lchild == None:
						nextNode.lchild = tempNode
						print "Node inserted as lchild of {0}".format(nextNode.val)
						return True
					else: 
						nextNode = nextNode.lchild
										
				elif nextNode.val < var:
					if nextNode.rchild == None:
						nextNode.rchild = tempNode
						print "Node inserted as rchild of {0}".format(nextNode.val)
						return True
					else:	
						nextNode = nextNode.rchild
											
				else:
					print "Duplicates not allowed.No insertion performed"
					return False
				
			
def inorder(node):
	if node == None:
		return
	inorder(node.lchild)
	print "Val is -> {0}".format(node.val)
	inorder(node.rchild)
		
		

if __name__ == "__main__":
	global root
	list = [100,45,789,12,34,567,9,5678,789]
	for var in list:
		if makeTree(var,root) == True:
			
			print "Cool"
		else:
			
			print "Not cool"
"
	inorder(root)

	

	