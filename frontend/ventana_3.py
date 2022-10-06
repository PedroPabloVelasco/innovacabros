# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventanas/ventana_3.ui")

class Ventana3(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_2 = pyqtSignal()
    senal_ventana_4 = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.sintomas = list()

    def init_gui(self):
        self.setWindowTitle("Ventana 3")
        self.siguiente_ventana_3.clicked.connect(self.siguiente_ventana)
        self.volver_ventana_3.clicked.connect(self.anterior_ventana)

    def siguiente_ventana(self):
        self.sintomas_seleccionados()
        self.senal_ventana_4.emit(self.sintomas)
        self.hide()

    def sintomas_seleccionados(self):
        if self.sintoma_1.isChecked():
            self.sintomas.append(self.sintoma_1.text())
        if self.sintoma_2.isChecked():
            self.sintomas.append(self.sintoma_2.text())
        if self.sintoma_3.isChecked():
            self.sintomas.append(self.sintoma_3.text())
        if self.sintoma_4.isChecked():
            self.sintomas.append(self.sintoma_4.text())
        if self.sintoma_5.isChecked():
            self.sintomas.append(self.sintoma_5.text())
        if self.sintoma_6.isChecked():
            self.sintomas.append(self.sintoma_6.text())
        if self.sintoma_7.isChecked():
            self.sintomas.append(self.sintoma_7.text())
        if self.sintoma_8.isChecked():
            self.sintomas.append(self.sintoma_8.text())
        if self.sintoma_9.isChecked():
            self.sintomas.append(self.sintoma_9.text())
        if self.sintoma_10.isChecked():
            self.sintomas.append(self.sintoma_otro_respuesta.text())

    def anterior_ventana(self):
        self.senal_ventana_2.emit()
        self.hide()

    def mostrar_ventana(self):
        self.show()
