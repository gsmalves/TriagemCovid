
from flask import Flask, request,  jsonify
import os

#Utilizando o miniframework Flask
app = Flask(__name__)


# Base de dados da aplicação
tabelaDados = {
    'pacientes': [
        
    ]
}

#Classe responsável pela atualização, criação e e leitura de dados do paciente
class CrudPaciente():

    #Função que retorna todos pacientes 
    def getTodosPacientes(self)->dict:
        return tabelaDados['pacientes']
    # Função que retorna um paciente específico, comparando o cpf
    def getPacienteByCPF(self, cpf: int)->dict:
        tabela= tabelaDados['pacientes']
        for x in tabela:
            if(x['cpf']==cpf):
                return x
        return None
    # Função que adiciona um paciente na base de dados
    def add(self, paciente: dict):
        tabelaDados['pacientes'].append(paciente)


    #Função de atualizar os dados do paciente,
    #procurando pelo cpf passado como parâmetro na lista de pacientes
    #se achar, passa os novos dados para a tabela de base de dados
    def updatePaciente(self, cpf: int, dados: dict) -> bool:
        i= None
        aux = 0
        tabela = tabelaDados['pacientes']
        for p in tabela:
            if(p['cpf']==cpf):
                i = aux #aqui pega o index do paciente em questão
            aux = aux+1
        if i!=None:
            tabela[i]['temp'] = dados['temp']
            tabela[i]['freq'] = dados['freq']
            tabela[i]['pressao'] = dados['pressao']
            tabela[i]['saturacao'] = dados['saturacao']
            return True
        else:
            return False


    #Função de atualizar apenas o status de saúde do paciente,
    #procurando pelo cpf passado como parâmetro na lista de pacientes
    #se achar, passa o novo status  para a tabela de base de dados
    def reportPaciente(self, cpf: int, dados: dict) -> bool:
            i= None
            aux = 0
            tabela = tabelaDados['pacientes']
            for p in tabela:
                if(p['cpf']==cpf):
                    i = aux #aqui pega o index do paciente em questão
                aux = aux+1
            if i!=None:
                tabela[i]['statusSaude'] = dados['statusSaude']
                return True
            else:
                return False

dados = CrudPaciente()

#Rota GET, para listar todos pacientes ,utilizando o app.route do Flask
@app.route('/paciente', methods=['GET'])
def listaTodos():
  
    return jsonify(dados.getTodosPacientes()), 200

#Rota PUT, para atualizar o statusSaude do paciente, utilizando o app.route do Flask
@app.route('/paciente/status/<int:cpf>', methods=['PUT'])
def reportStatus(cpf: int):
    dataUpdate = request.json
    if dados.reportPaciente(cpf, dataUpdate):
        return jsonify({'status': 'Sucess'}), 200
    else:
        return jsonify({'status': 'Paciente não encontrado'}), 404

#Rota PUT, para atualizar todos os dados do paciente, utilizando o app.route do Flask
@app.route('/paciente/<int:cpf>', methods=['PUT'])
def update(cpf: int):
    dataUpdate = request.json
    if dados.updatePaciente(cpf, dataUpdate):
        return jsonify({'status': 'Sucess'}), 200
    else:
        return jsonify({'status': 'Paciente não encontrado'}), 404

#Rota GET, para listar o paciente específico através do seu cpf ,utilizando o app.route do Flask
@app.route('/paciente/<int:cpf>', methods=['GET'])
def get(cpf: int):
    if dados.getPacienteByCPF(cpf):
        return jsonify(dados.getPacienteByCPF(cpf)), 200
    else:
        return jsonify({'status': 'Paciente não encontrado'}), 404

#Rota POST, para criar um paciente ,utilizando o app.route do Flask
@app.route('/paciente/criar', methods=['POST'])
def criar():
    paciente = request.json
    dados.add(paciente)
 
    return jsonify({'status': 'Sucess'}), 200
   
#Conexão de porta do flask com o servidor Heroku
port = int(os.environ.get("PORT", 5000))
app.run(debug=True ,host='0.0.0.0', port=port)


