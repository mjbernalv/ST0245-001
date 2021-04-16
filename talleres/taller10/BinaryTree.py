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

    def search(self, element):
        return self.__searchAux(self.root, element)
   
    def __searchAux(self, node, element): #Complexity worst case: T(n)= T(n/2)+T(n/2)+c --> O(n) n=size of the tree
        if node == None:
            return False
        if element == node.data:
            return True
        if element<node.data:
            isLeft = self.__searchAux(node.left,element)
            return isLeft
        isRight = self.__searchAux(node.right,element)
        return isRight

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

    def print(self):
        self.__printAux(self.root)
        
    def __printAux(self, actual):
        if actual is not None:
            self.__printAux(actual.left)
            print(actual.data)
            self.__printAux(actual.right)

    def draw(self):
        return f'digraph G {"{"} \n {self.__drawAux(self.root)} \n{"}"}'
    
    def __drawAux(self, actual): #Complexity worst case: T(n)=T(n/2)+T(n/2)+c --> O(n) n=size of the tree
        if actual == None:
            return
        if actual.left != None and actual.right!=None:
            return f'{actual} -> {actual.left} \n {actual} -> {actual.right} \n {self.__drawAux(actual.left)} \n {self.__drawAux(actual.right)}'
        if actual.left != None:
            return f'{actual} -> {actual.left} \n {self.__drawAux(actual.left)}'
        if actual.right != None:
            return f'{actual} -> {actual.right} \n {self.__drawAux(actual.right)}'
        if actual.right == None and actual.left == None:
            return ""

if __name__ == '__main__':    
    tree = BinaryTreeMM()
    tree.add(1)
    tree.add(0)
    tree.add(2)
    tree.add(3)
    tree.add(3)
    print(tree.search(2))
    print(tree.search(4))
    tree.print()
    print(tree.draw())