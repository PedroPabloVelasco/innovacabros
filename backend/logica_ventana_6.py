from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from random import randint

class LogicaVentana(QObject):
    senal_fila = pyqtSignal(str, int)

    def __init__(self, cantidad_sintomas):
        super().__init__()
        self.cantidad_sintomas = cantidad_sintomas
        self.revisar_sintomas()

    def revisar_sintomas(self):
        if self.cantidad_sintomas == 1:
            self.categoria = 'A'
        elif self.cantidad_sintomas == 2 or self.cantidad_sintomas == 3:
            self.categoria = 'B'
        elif self.cantidad_sintomas == 4 or self.cantidad_sintomas == 5:
            self.categoria = 'C'
        elif self.cantidad_sintomas == 6 or self.cantidad_sintomas == 7:
            self.categoria = 'D'
        elif self.cantidad_sintomas > 7:
            self.categoria = 'E'
        self.numero = randint(1, 100)
        self.senal_fila.emit(self.categoria, self.numero)
        
