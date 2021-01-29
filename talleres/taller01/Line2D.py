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

class Line2D():

    def __init__(self, punto1, punto2):
        self.initial = punto1
        self.final = punto2
        if(punto1.x == punto2.x):
            self.slope = 0
        else:
            self.slope = (punto1.y-punto2.y)/(punto1.x-punto2.x)
        self.b = (punto1.x*-1*self.slope)+punto1.y

    def slope(self):
       return self.slope

    def getFormula(self):
        sign = "-"
        if self.b>=0:
            sign = "+"
        return "y=" + str(self.slope) + "x" + sign + str(self.b)

    def generatePoints(self):
        if self.slope == 0:
            output = "Points: [ "
            miny = min(self.initial.y, self.final.y)
            maxy = max(self.initial.y, self.final.y)
            for i in range (miny, maxy+1):
                output = output + "(0," + str(i) + ") "
            output = output + "]"
            return output
        elif self.initial.x > self.final.x:
            output = "Points: [ "
            for i in range (self.final.x, self.initial.x+1):
                y = self.slope*i + self.b
                output = output + "(" + str(i) + "," + str(y) + ") "
            output = output + "]"
            return output
        else:
            output = "Points: [ "
            for i in range (self.initial.x, self.final.x+1):
                y = self.slope*i + self.b
                output = output + "(" + str(i) + "," + str(y) + ") "
            output = output + "]"
            return output
             

class main():
    punto1 = Punto2D(0,0)
    punto2 = Punto2D(3,3)

    linea1 = Line2D(punto1, punto2)
    print(linea1.slope)
    print(linea1.getFormula())
    print(linea1.generatePoints())
