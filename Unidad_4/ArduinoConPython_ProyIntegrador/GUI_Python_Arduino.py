import sys
import serial as conecta

import ClienteREST

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "GUI_Python_Arduino.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

        self.checkDecision = QtCore.QTimer()
        self.checkDecision.timeout.connect(self.revisaDecision)

        self.decision = 1 # 1 normal ,2 medio , 3 alta

    # Área de los Slots
    def accion(self):
        try:
            txt_btn = self.btn_accion.text()
            if txt_btn == "CONECTAR": ##arduino == None
                self.txt_estado.setText("CONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                puerto = self.txt_puerto.text()
                #puerto = "COM" + self.txt_puerto.text()
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)
                self.checkDecision.start(100)
            elif txt_btn == "DESCONECTAR":
                self.txt_estado.setText("DESCONECTADO")
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.checkDecision.stop()
                self.arduino.close()
            else: #RECONECTAR
                self.txt_estado.setText("RECONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                self.segundoPlano.start(100)
                self.checkDecision.start(100)

        except Exception as error:
            print(error)
        #self.arduino.isOpen()

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                #leer
                variable = self.arduino.readline().decode()
                variable = variable.replace("\r","")
                variable = variable.replace("\n","")
                if variable!="":
                    self.lw_datos.addItem(variable)
                    self.lw_datos.setCurrentRow(self.lw_datos.count() - 1)
                    print(variable)
                    if variable[0] == "V":
                        print("Velocidad:", variable[1:])
                        ClienteREST.insertRecord(2, int(variable[1:]))
                    elif variable[0] == "D":
                        print("Distancia:", variable[1:])
                        ClienteREST.insertRecord(1, int(variable[1:]))

    def revisaDecision(self):
        self.decision = ClienteREST.getLastDecision()
        self.decision = 1 ##solo para pruebas....
        print("Decision:" , self.decision)
        self.arduino.write(str(self.decision).encode())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
