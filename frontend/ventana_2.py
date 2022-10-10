# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventanas/ventana_2.ui")

class Ventana2(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_XX = pyqtSignal()
    senal_ventana_3 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana 2")

        self.siguiente_ventana_2.clicked.connect(self.siguiente_ventana)
        self.volver_ventana_2.clicked.connect(self.anterior_ventana)

    def siguiente_ventana(self):
        self.senal_ventana_3.emit()
        self.hide()

    def anterior_ventana(self):
        self.senal_ventana_XX.emit()
        self.hide()
    
    def mostrar_ventana(self):
        self.show()