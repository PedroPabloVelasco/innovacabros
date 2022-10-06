# pylint: disable=E0611
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=import-error

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal



window_name, base_class = uic.loadUiType("ventanas/ventana_4.ui")

class Ventana4(window_name, base_class):  # pylint: disable=E0602
    senal_ventana_3 = pyqtSignal()
    senal_ventana_5 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana 4")

        self.siguiente_ventana_4.clicked.connect(self.siguiente_ventana)
        self.volver_ventana_4.clicked.connect(self.anterior_ventana)

    def siguiente_ventana(self):
        self.senal_ventana_5.emit()
        dolor = self.barra_dolor.value()
        print(f'El dolor seleccionado es:  {dolor}')
        self.hide()

    def anterior_ventana(self):
        self.senal_ventana_3.emit()
        self.hide()

    def mostrar_ventana(self, sintomas):
        self.show()
        self.calculo_triage(sintomas)

# Esta funcion tenemos que hacer la ponderacion
    def calculo_triage(self, sintomas):
        for elemento in sintomas:
            print(f'El sintoma seleccionado es {elemento}')
