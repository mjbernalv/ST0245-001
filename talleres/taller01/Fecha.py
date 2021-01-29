class fecha():
    
    def __init__(self,dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
      
    def dia(self):
        return self.dia
      
    def mes(self):
        return self.mes
          
    def año(self):
        return self.año

    #-1: la fecha es anterior a la ingresada, 1: la fecha es posterior a la ingresada, 0: las fechas son iguales     
    def comparar(self, other):
        if self.año > other.año:
            return 1
        elif self.año < other.año:
            return -1
        if self.mes > other.mes:
            return 1
        elif self.mes < other.mes:
            return -1
        if self.dia > other.dia:
            return 1
        elif self.dia < other.dia:
            return -1
        return 0
          
    def toString(self): 
        return str(self.dia) + "/" + str(self.mes) + "/" + str(self.año)

"""class Main():
    fecha1 = fecha(1,3,2017)
    fecha2 = fecha(29,2,2018)
    fecha3 = fecha(14,3,2017)
    fecha4 = fecha(1,3,2017)

    print(fecha1.dia)
    print(fecha1.mes)
    print(fecha1.año)
    print(fecha1.toString())
    print(fecha1.comparar(fecha2))
    print(fecha1.comparar(fecha3))
    print(fecha1.comparar(fecha4))"""
