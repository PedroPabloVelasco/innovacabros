# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventanas/ventana_6.ui")

class Ventana6(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_5 = pyqtSignal()

    def __init__(self, categoria=None, numero=None):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana 6")

    def anterior_ventana(self):
        self.senal_ventana_5.emit()
        self.hide()

    def mostrar_ventana(self):
        self.show()