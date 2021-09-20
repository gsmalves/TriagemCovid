from PyQt5 import uic, QtWidgets
import requests,time,threading


# Esse arquivo é responsável por controlar o fluxo de tela e
# funcionalidades das telas do paciente(login e cadastro).

#Link do Heroku, onde está hospedada a api na internet
link =  'https://server-api-covid.herokuapp.com'



# Função que retorna um json com sinais vitais inseridos pelo paciente

def atualizar_paciente() -> dict:
    return {
        'freq': tela_cadastro.lineEdit_freq.text(),
        'pressao': tela_cadastro.lineEdit_press.text(),
        'saturacao': tela_cadastro.lineEdit_satu.text(),
        'temp': tela_cadastro.lineEdit_temp.text()
    }


# Função que realiza o PUT dos dados de um paciente,
# conta com um sleep ligado a thread que realiza esta requisição
# a cada 1.5s

def atualizar():
    while(True):
        time.sleep(1.5)
        try:
            requests.put(
                url=f'{link}/paciente/{int(tela_login.lineEdit_cpf.text())}', json=atualizar_paciente())
            
        except:
            print('error')


# Função que cria um paciente na telalogin, a partir
# do seu cpf e nome, posteriormente os outros dados são inseridos 
# e atualizados.

def criar_paciente() -> dict:
    return {
        'cpf': int(tela_login.lineEdit_cpf.text()),
        'freq': '',
        'nome': tela_login.lineEdit_nome.text(),
        'pressao': '',
        'saturacao': '',
        'temp': '',
        'statusSaude':'Aguardando'
    }

# Função que realiza a requisição de buscar o status da saúde
# de um paciente, em sua tela, a espera da resposta do médico.
# A requisição é feita a cada 2s

def atualiza_status():
    while(True):
        time.sleep(2.0)
        user=get_paciente_id()
        tela_cadastro.label_situacao_paciente.setText(user['statusSaude'])


# Função que apresnta a tela de cadastro com o nome
# do paciente logado e inicia as duas threads presentes na 
# tela de cadastro, de atualizar os dados inseridos pelo paciente a cada instante 
# e a de atualizar a resposta do seu status enviada pelo médico

def abre_cadastro():
    
    user = get_paciente_id()
    tela_cadastro.label_nome_paciente.setText(user['nome'])
    tela_cadastro.show()
    t2=threading.Thread(target=atualizar)
    t2.start()
    # tela_cadastro.botao_ligar.clicked.connect(atualizar)
    t1=threading.Thread(target=atualiza_status)
    t1.start()

#Função que faz a requisição do paciente específico pelo seu cpf
def get_paciente_id() ->dict:
    return requests.get(url=f'{link}/paciente/{int(tela_login.lineEdit_cpf.text())}').json()

#Função responsável pelo login e criação inicial de um paciente no sistema
def entrar():
    try:
        requests.post(url=f'{link}/paciente/criar', json=criar_paciente())
       
        abre_cadastro()
    except:
        print('error login')


app = QtWidgets.QApplication([])

#importando e carregando os arquivos .ui gerados pelo qtDesing do pyqt
tela_login = uic.loadUi('login.ui')
tela_cadastro = uic.loadUi('cadastro.ui')

tela_login.botao_login.clicked.connect(entrar)
tela_login.show()

app.exec()
