class TV:
    numTV=None
    def __init__(self,marca,estado):
        self.marca=marca
        self.canal=1
        self.precio=500
        self.estado=estado
        self.volumen=1
        self.control=None
        numTV=numTV+1
    def canalUp(self):
        self.setCanal(self.canal+1)
    def canalDown(self):
        self.setCanal(self.canal-1)
    def volumenUp(self):
        self.setVolumen(self.volumen+1)
    def volumenDown(self):
        self.setvolumen(self.volumen-1)
    def turnOn(self):
        self.estado=True
    def turnOff(self):
        self.estado=False
    def getEstado(self):
        return self.estado
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    def getCanal(self):
        return self.canal
    def setCanal(self,canal):
        if (self.canal<1 or self.canal>120 or self.estado==False):
            pass
        else:
            self.canal=canal
    def getVolumen(self):
        return self.volumen
    def setVolumen(self,volumen):
        if (self.volumen<0 or self.volumen>7 or self.estado==False): 
            pass
        else:
            self.volumen=volumen
    def getControl(self):
        return self.control
    def setControl(self,control):
        self.control=control
    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio=precio
