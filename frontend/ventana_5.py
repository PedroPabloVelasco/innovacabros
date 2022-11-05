# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventanas/ventana_5.ui")

class Ventana5(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_4 = pyqtSignal()
    senal_ventana_6 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana 5")
        self.volver_ventana_5.clicked.connect(self.anterior_ventana)
        self.siguiente_ventana_5.clicked.connect(self.siguiente_ventana)
        

    def siguiente_ventana(self):
        self.senal_ventana_6.emit()
        self.hide()

    def anterior_ventana(self):
        self.senal_ventana_4.emit()
        self.hide()

    def mostrar_ventana(self):
        self.show()
