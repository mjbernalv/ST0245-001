class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maternalGrandmother(node):
    if(node.left!=None):
        if(node.left.left!=None):
            return node.left.left.data
        else:
            return None
    else:
        return None

root = Node("Martin")
root.left = Node("Catalina")
root.right = Node("Mauricio")
root.left.left = Node("Marta")
root.left.right = Node("Jorge")
root.right.left = Node("Berta")
root.right.right = Node("Jairo")
root.left.left.left = Node("Margarita")
root.left.left.right = Node("Roberto")
root.left.right.left = Node("Marta")
root.left.right.right = Node("Humberto")
root.right.left.left = Node("Berta")
root.right.left.right = Node("Jaime")
root.right.right.left = Node("Angelina")
root.right.right.right = Node("Manuel")

print("Martin's maternal grandmother is" , maternalGrandmother(root))
print("Mauricio's maternal grandmother is" , maternalGrandmother(root.right))
print("Manuel's maternal grandmother is" , maternalGrandmother(root.right.right.right))
print("")

root2 = Node("Maria José")
root2.left = Node("Catalina")
root2.right = Node("Mauricio")
root2.left.left = Node("Luz Stella")
root2.left.right = Node("Iván")
root2.right.left = Node("Luz Stella")
root2.right.right = Node("Mauricio")
root2.left.left.left = Node("Blanca")
root2.left.left.right = Node("Pablo")
root2.left.right.left = Node("Tulia")
root2.left.right.right = Node("Francisco")
root2.right.left.left = Node("Margarita")
root2.right.left.right = Node("Alberto")
root2.right.right.left = Node("Lucrecia")
root2.right.right.right = Node("José María")

print("Maria José's maternal grandmother is" , maternalGrandmother(root2))
print("Mauricio's maternal grandmother is" , maternalGrandmother(root2.right))
print("José María's maternal grandmother is" , maternalGrandmother(root2.right.right.right))
