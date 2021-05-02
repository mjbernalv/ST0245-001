class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
	    return f'{self.data}'

class BinaryTreeMM():
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__addAux(data, self.root)

    def __addAux(self, data, actual): #Complexity worst case: T(n)= T(n/2)+T(n/2)+c --> O(n) n=size of the tree
        new = Node(data)
        if data<actual.data:
            if actual.left == None:
                actual.left = new
            else:
                self.__addAux(data, actual.left)
        else:
            if actual.right == None:
                actual.right = new
            else:
                self.__addAux(data, actual.right)

    def posorden(self, root): #Complexity worst case: T(n)=T(n/2)+T(n/2)+c --> O(n)  n = size of the tree (number of nodes)
        if root != None:
            self.posorden(root.left)
            self.posorden(root.right)
            print(root.data)
        return

class main():
    tree = BinaryTreeMM()
    num = int(input("Number of elements of the tree: "))
    print("Enter the elements of the tree in inorder")
    for i in range (num):
        element = int(input())
        tree.add(element)

    print("\n" + "Tree in postorder")
    tree.posorden(tree.root)

#Example: 50 30 24 5 28 45 98 52 60
 #Complexity worst case: O(n^2)