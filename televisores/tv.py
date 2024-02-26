class TV:
    _numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        TV._numTV=TV._numTV+1
    def getNumTV():
        return TV._numTV
    def setNumTV(n):
        TV._numTV=n
    def canalUp(self):
        self.setCanal(self._canal+1)
    def canalDown(self):
        self.setCanal(self._canal-1)
    def volumenUp(self):
        self.setVolumen(self._volumen+1)
    def volumenDown(self):
        self.setVolumen(self._volumen-1)
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def getEstado(self):
        return self._estado
    def getMarca(self):
        return self._marca
    def setMarca(self,marca):
        self._marca=marca
    def getCanal(self):
        return self._canal
    def setCanal(self,canal):
        if (canal<1 or canal>120 or self._estado==False):
            pass
        else:
            self._canal=canal
    def getVolumen(self):
        return self._volumen
    def setVolumen(self,volumen):
        if (volumen<0 or volumen>7 or self._estado==False): 
            pass
        else:
            self._volumen=volumen
    def getControl(self):
        return self._control
    def setControl(self,control):
        self._control=control
    def getPrecio(self):
        return self._precio
    def setPrecio(self,precio):
        self._precio=precio
