# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel

window_name, base_class = uic.loadUiType("ventanas/ventana_XX.ui")

class VentanaXX(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_1 = pyqtSignal()
    senal_ventana_2 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana 2")

        self.siguiente_ventana_XX.clicked.connect(self.siguiente_ventana)
        self.volver_ventana_XX.clicked.connect(self.anterior_ventana)

    def siguiente_ventana(self):
        if self.Edad.text() != '' or self.Sexo.text() != '': 
            self.senal_ventana_2.emit()
            self.hide()
        else:
            self.mensaje_error = QLabel('Error al ingresar edad y/o sexo!', self)
            self.mensaje_error.setGeometry(115, 275, 270, 21)
            self.mensaje_error.setStyleSheet('background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);')
            self.mensaje_error.setVisible(True)

    def anterior_ventana(self):
        self.senal_ventana_1.emit()
        self.hide()
    
    def mostrar_ventana(self):
        self.show()