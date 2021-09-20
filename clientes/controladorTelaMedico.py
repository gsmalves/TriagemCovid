# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medico.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests, time, json

# Esse arquivo é responsável por controlar as funcionalidades
# da tela do médico e este arquivo.py foi gerado através da conversão
#de um arquivo .ui do PyQt5

#Link do Heroku, onde está hospedada a api na internet
link = 'https://server-api-covid.herokuapp.com'

#Classe responsável por setar as propriedades dos componentes da tela e inicializá-los
class Ui_janelaMedico(QtCore.QObject):
    def setupUi(self, janelaMedico):
        janelaMedico.setObjectName("janelaMedico")
        janelaMedico.resize(766, 507)
        janelaMedico.setStyleSheet("background-color:rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(janelaMedico)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(300, 0, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelTitulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo_2.setGeometry(QtCore.QRect(30, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo_2.setFont(font)
        self.labelTitulo_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelTitulo_2.setObjectName("labelTitulo_2")
        self.labelTitulo_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo_3.setGeometry(QtCore.QRect(430, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo_3.setFont(font)
        self.labelTitulo_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.labelTitulo_3.setObjectName("labelTitulo_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 320, 751, 16))
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget_Pacientes = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Pacientes.setGeometry(QtCore.QRect(30, 80, 301, 192))
        self.listWidget_Pacientes.setObjectName("listWidget_Pacientes")
        self.listWidget_Pacientes_graves = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Pacientes_graves.setGeometry(QtCore.QRect(430, 80, 301, 192))
        self.listWidget_Pacientes_graves.setObjectName("listWidget_Pacientes_graves")
        self.container_dados_pacientes = QtWidgets.QLabel(self.centralwidget)
        self.container_dados_pacientes.setGeometry(QtCore.QRect(16, 342, 741, 121))
        self.container_dados_pacientes.setText("")
        self.container_dados_pacientes.setObjectName("container_dados_pacientes")
        self.label_titulo_temperatura = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_temperatura.setGeometry(QtCore.QRect(20, 370, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_temperatura.setFont(font)
        self.label_titulo_temperatura.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_titulo_temperatura.setObjectName("label_titulo_temperatura")
        self.label_titulo_freq = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_freq.setGeometry(QtCore.QRect(290, 370, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_freq.setFont(font)
        self.label_titulo_freq.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_titulo_freq.setObjectName("label_titulo_freq")
        self.label_titulo_saturacao = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_saturacao.setGeometry(QtCore.QRect(20, 440, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_saturacao.setFont(font)
        self.label_titulo_saturacao.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_titulo_saturacao.setObjectName("label_titulo_saturacao")
        self.label_titulo_pressao = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_pressao.setGeometry(QtCore.QRect(290, 440, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_pressao.setFont(font)
        self.label_titulo_pressao.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_titulo_pressao.setObjectName("label_titulo_pressao")
        self.label_temperatura = QtWidgets.QLabel(self.centralwidget)
        self.label_temperatura.setGeometry(QtCore.QRect(130, 370, 91, 21))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_temperatura.setFont(font)             
        self.label_temperatura.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_temperatura.setText("")
        self.label_temperatura.setObjectName("label_temperatura")
        self.label_frequencia = QtWidgets.QLabel(self.centralwidget)
        self.label_frequencia.setGeometry(QtCore.QRect(400, 370, 111, 21))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_frequencia.setFont(font)              
        self.label_frequencia.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_frequencia.setText("")
        self.label_frequencia.setObjectName("label_frequencia")
        self.label_saturacao = QtWidgets.QLabel(self.centralwidget)
        self.label_saturacao.setGeometry(QtCore.QRect(130, 440, 91, 21))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_saturacao.setFont(font)              
        self.label_saturacao.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_saturacao.setText("")
        self.label_saturacao.setObjectName("label_saturacao")
        self.label_pressao = QtWidgets.QLabel(self.centralwidget)
        self.label_pressao.setGeometry(QtCore.QRect(390, 430, 111, 31))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pressao.setFont(font)          
        self.label_pressao.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_pressao.setText("")
        self.label_pressao.setObjectName("label_pressao")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(530, 340, 16, 141))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_titulo_temperatura_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_temperatura_2.setGeometry(QtCore.QRect(620, 350, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_temperatura_2.setFont(font)
        self.label_titulo_temperatura_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_titulo_temperatura_2.setObjectName("label_titulo_temperatura_2")
        self.radioButton_leve = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_leve.setGeometry(QtCore.QRect(580, 380, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_leve.setFont(font)
        self.radioButton_leve.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_leve.setObjectName("radioButton_leve")
        self.radioButton_grave = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_grave.setGeometry(QtCore.QRect(580, 420, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_grave.setFont(font)
        self.radioButton_grave.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_grave.setObjectName("radioButton_grave")
        self.label_nome_paciente_select = QtWidgets.QLabel(self.centralwidget)
        self.label_nome_paciente_select.setGeometry(QtCore.QRect(80, 340, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_nome_paciente_select.setFont(font)
        self.label_nome_paciente_select.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_nome_paciente_select.setText("")
        self.label_nome_paciente_select.setObjectName("label_nome_paciente_select")
        self.label_paciente = QtWidgets.QLabel(self.centralwidget)
        self.label_paciente.setGeometry(QtCore.QRect(20, 340, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_paciente.setFont(font)
        self.label_paciente.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_paciente.setObjectName("label_paciente")
        janelaMedico.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(janelaMedico)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName("menubar")
        janelaMedico.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(janelaMedico)
        self.statusbar.setObjectName("statusbar")
        janelaMedico.setStatusBar(self.statusbar)

        self.carregaTela(janelaMedico)
        QtCore.QMetaObject.connectSlotsByName(janelaMedico)
        self.listWidget_Pacientes.itemClicked.connect(self.paciente_selecionado)
        self.listWidget_Pacientes_graves.itemClicked.connect(self.paciente_selecionado_graves)
        self.radioButton_grave.clicked.connect(self.atualiza_paciente)
        self.radioButton_leve.clicked.connect(self.atualiza_paciente)
    
    #Função responsável por inicar o paciente selecionado no listwidjet de pacientes de modo geral
    #pegando o indice da linha que foi selecionada, e mostrando nas labels da tela
    def paciente_selecionado(self, item):
        i = self.listWidget_Pacientes.row(item)
        self.label_nome_paciente_select.setText(str(self.leve[i]['nome']))
        self.label_frequencia.setText(str(self.leve[i]['freq']))
        self.label_pressao.setText(str(self.leve[i]['pressao'])) 
        self.label_saturacao.setText(str(self.leve[i]['saturacao']))
        self.label_temperatura.setText(str(self.leve[i]['temp']))
        self.saveCpfPaciente = self.leve[i]['cpf'] #guarda o cpf do paciente selecionado para uma posterior atualização de status da saúde
        
    #Função responsável por inicar o paciente selecionado no listwidjet de pacientes graves 
    #pegando o indice da linha que foi selecionada, e mostrando nas labels da tela
    def paciente_selecionado_graves(self, item):
        i = self.listWidget_Pacientes_graves.row(item)
        self.label_nome_paciente_select.setText(str(self.grave[i]['nome']))
        self.label_frequencia.setText(str(self.grave[i]['freq']))
        self.label_pressao.setText(str(self.grave[i]['pressao'])) 
        self.label_saturacao.setText(str(self.grave[i]['saturacao']))
        self.label_temperatura.setText(str(self.grave[i]['temp']))
        self.saveCpfPaciente = self.grave[i]['cpf']#guarda o cpf do paciente selecionado para uma posterior atualização de status da saúde
 
    #Função responsável por realizar a requisição de atualizar o statusSaúde do paciente selecionado, 
    #essa atualização é feita através do click dos radioButton
    def atualiza_paciente(self):
        
        try:
                requests.put(
                url=f'{link}/paciente/status/{int(self.saveCpfPaciente)}', json=self.respondePaciente())

        except:
                print('error')
        

    #Função responsável por carregar a janela completa e setar as informações
    def carregaTela(self, janelaMedico):
        _translate = QtCore.QCoreApplication.translate
        janelaMedico.setWindowTitle(_translate("janelaMedico", "MainWindow"))
        self.labelTitulo.setText(_translate("janelaMedico", "Triagem Covid 19"))
        self.labelTitulo_2.setText(_translate("janelaMedico", "Lista de pacientes"))
        self.labelTitulo_3.setText(_translate("janelaMedico", "Emergente-Imediato"))
        self.label_titulo_temperatura.setText(_translate("janelaMedico", "Temperatura (°C):"))
        self.label_titulo_freq.setText(_translate("janelaMedico", "Frequencia(bpm):"))
        self.label_titulo_saturacao.setText(_translate("janelaMedico", "Saturação(SpO2):"))
        self.label_titulo_pressao.setText(_translate("janelaMedico", "Pressão(mmHg):"))
        self.label_titulo_temperatura_2.setText(_translate("janelaMedico", "Situação"))
        self.radioButton_leve.setText(_translate("janelaMedico", "Leve"))
        self.radioButton_grave.setText(_translate("janelaMedico", "Emergente"))
        self.label_paciente.setText(_translate("janelaMedico", "Paciente: "))
        
        #instancia da thread criada para enviar o sinal ou dados para a função de manipular a lista de pacientes
        self.thread_start = minhaThread()
        self.thread_start.enviaSinal.connect(self.manipula_lista)        
        self.thread_start.start()

     #Esta função é responsável por fazer a inserção de um paciente no listWidjet específico
     #podemos enteder melhor mais abaixo como funciona a separação dos listwidjet.
    def manipula_lista(self,sinal):

        _translate = QtCore.QCoreApplication.translate
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setText(_translate("MainWindow",sinal['nome'])) 
        
        #Nessa condição podemos definir qual a lista que o paciente irá se manter ou ser transferido
        #se seu status for setado como Grave, este, irá ser transferido para a lista de emergentes no front
        #bem como no back, pois assim passamos a ter controle da posição correta de cada paciente
        #em ambas as listas. Se seu status não for grave, ele se mantém na lista geral ou volta para a mesma se assim for
        #necessário
        if sinal['statusSaude'] == 'Grave':
                self.grave.append(sinal)
                self.listWidget_Pacientes_graves.addItem(item)
        else:
                self.leve.append(sinal)
                self.listWidget_Pacientes.addItem(item)    
        
    #Função que retorna ao paciente a resposta sobre seu estado de saúde , se leve ou grave
    def respondePaciente(self)->dict:
            if self.radioButton_leve.isChecked():
                return {
                        'statusSaude': 'Leve'
                }
            if self.radioButton_grave.isChecked():
                return {
                        'statusSaude': 'Grave'
                }


     #Função que retorna a lista de pacientes presentes na base de dados da api
    def lista_pacientes(self)->dict:
        self.response = requests.get(url=f'{link}/paciente').json()
        return self.response



# Essa thread serve para realizar um serviço em paralelo de ficar enviando o sinal, que neste caso
#  é objeto paciente, para a função de manipular a lista a cada segundos 1.8s, através da requisição GET.
#As listas tanto do front como do back são limpadas a cada novo ciclo para que o proceso de atualização seja
#feito de maniera correta , sem perdas ou duplicação de dados.

class minhaThread(QtCore.QThread):
    enviaSinal = QtCore.pyqtSignal(object)
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):
        
        while True:
            ui.listWidget_Pacientes.clear()
            ui.listWidget_Pacientes_graves.clear()
            
            ui.leve.clear()
            ui.grave.clear()
            time.sleep(1.8)    
            response = ui.lista_pacientes()
            
            for x in range(len(response)):
   
                self.enviaSinal.emit(response[x])


#Inicialização do arquivo
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaMedico = QtWidgets.QMainWindow()
    ui = Ui_janelaMedico()
    ui.grave =[]#lista de pacientes graves
    ui.leve=[]#lista de pacientes leves ou de maneira geral
    ui.setupUi(janelaMedico)
    janelaMedico.show()
    sys.exit(app.exec_())
