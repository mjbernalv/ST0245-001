import math

class Punto2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
       return self.x

    def get_y(self):
       return self.y

    def radio_polar(self):
       return math.sqrt(self.x**2 + self.y**2)

    def angulo_polar(self):
        return math.atan(self.y/self.x)

    def dist_euclidiana(self, other):
        distx = self.x - other.x
        disty = self.y - other.y
        return math.sqrt(distx**2+disty**2)

"""class main():
    punto1 = Punto2D(10,20)
    punto2 = Punto2D(0,0)

    print(punto1.get_x())
    print(punto1.get_y())
    print(punto1.radio_polar())
    print(punto1.angulo_polar())
    print(punto1.dist_euclidiana(punto2))"""
