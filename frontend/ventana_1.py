# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventanas/ventana_1.ui")

class Ventana1(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_2 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana 1")

        self.siguiente_ventana_1.clicked.connect(self.siguiente_ventana)

    def siguiente_ventana(self):
        self.senal_ventana_2.emit()
        self.hide()
    

    def mostrar_ventana(self):
        self.show()