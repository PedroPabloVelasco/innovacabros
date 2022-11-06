# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel

window_name, base_class = uic.loadUiType("ventanas/ventana_3.ui")

class Ventana3(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_2 = pyqtSignal()
    senal_ventana_4 = pyqtSignal(list)
    senal_sintomas = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.sintomas = []

    def init_gui(self):
        self.setWindowTitle("Ventana 3")
        self.siguiente_ventana_3.clicked.connect(self.siguiente_ventana)
        self.volver_ventana_3.clicked.connect(self.anterior_ventana)

    def siguiente_ventana(self):
        self.sintomas_seleccionados()
        if len(self.sintomas) == 1:
            if self.sintomas[0] == 'Malestar General':
                self.senal_ventana_4.emit(self.sintomas)
                self.hide()
        else:
            self.mensaje_error = QLabel('Debe seleccionar solo un metodo!', self)
            self.mensaje_error.setGeometry(144, 430, 191, 16)
            self.mensaje_error.setStyleSheet('background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);')
            self.mensaje_error.setVisible(True)

    def sintomas_seleccionados(self):
        self.sintomas = []
        if self.malestar.isChecked():
            self.sintomas.append(self.malestar.text())
        elif self.desmayo.isChecked():
            self.sintomas.append(self.desmayo.text())
        elif self.lesion.isChecked():
            self.sintomas.append(self.lesion.text())
        elif self.dolor_cuerpo.isChecked():
            self.sintomas.append(self.dolor_cuerpo.text())
        elif self.diabetes.isChecked():
            self.sintomas.append(self.diabetes.text())
        elif self.dificultad_respirar.isChecked():
            self.sintomas.append(self.dificultad_respirar.text())
        elif self.embarazo.isChecked():
            self.sintomas.append(self.embarazo.text())
        elif self.ets.isChecked():
            self.sintomas.append(self.ets.text())
        elif self.hemorragia.isChecked():
            self.sintomas.append(self.hemorragia.text())
        elif self.infeccion.isChecked():
            self.sintomas.append(self.infeccion.text())
        elif self.tronco_superior.isChecked():
            self.sintomas.append(self.tronco_superior.text())
        elif self.problemas_piel.isChecked():
            self.sintomas.append(self.problemas_piel.text())
        elif self.vomitos.isChecked():
            self.sintomas.append(self.vomitos.text())

    def anterior_ventana(self):
        self.senal_ventana_2.emit()
        self.hide()

    def mostrar_ventana(self):
        self.show()
