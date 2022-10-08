# pylint: disable=W0622
# pylint: disable=E0611
# pylint: disable=E0401
# pylint: disable=E1120

import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_1 import Ventana1
from frontend.ventana_2 import Ventana2
from frontend.ventana_3 import Ventana3
from frontend.ventana_4 import Ventana4
from frontend.ventana_5 import Ventana5
from frontend.ventana_6 import Ventana6

if __name__ == '__main__':
    def hook(type, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Llamar ventanas
    ventana_1 = Ventana1()
    ventana_2 = Ventana2()
    ventana_3 = Ventana3()
    ventana_4 = Ventana4()
    ventana_5 = Ventana5()
    ventana_6 = Ventana6()


# # Conectar señales

# Siguiente
ventana_1.senal_ventana_2.connect(ventana_2.mostrar_ventana)
ventana_2.senal_ventana_3.connect(ventana_3.mostrar_ventana)
ventana_3.senal_ventana_4.connect(ventana_4.mostrar_ventana)
ventana_4.senal_ventana_5.connect(ventana_5.mostrar_ventana)
ventana_5.senal_ventana_6.connect(ventana_6.mostrar_ventana)

# Volver
ventana_2.senal_ventana_1.connect(ventana_1.mostrar_ventana)
ventana_3.senal_ventana_2.connect(ventana_2.mostrar_ventana)
ventana_4.senal_ventana_3.connect(ventana_3.mostrar_ventana)
ventana_5.senal_ventana_4.connect(ventana_4.mostrar_ventana)


ventana_1.show()
app.exec()
