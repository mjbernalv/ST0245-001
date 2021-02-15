import csv
import numpy as np

class Proyecto():
    
    def __init__(self):
        self.matrix = []
        
    def matrix(self):
        return self.matrix
        
    def loadcsv(self, filename):
        try:
            picture = csv.reader(open(filename), delimiter=",")
            x = list(picture)
            array = np.array(x).astype("int")
            self.matrix = array
            return self.matrix
        except:
            print("File not found")

class principal():
    file = str(input("Ingrese nombre del archivo: "))
    imagen = Proyecto()
    imagen.loadcsv(file)
    print(imagen.matrix)