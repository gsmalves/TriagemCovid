# TriagemCovid
Sistema de triagem covid através de sinais vitais de pacientes suspeitos
Onde o médico recebe estes sinais vitais de um ou mais pacientes e pode classificar 
como leve ou grave e a partir disso o paciente recebe a resposta da sua situação de saúde
se deve ou não procurar um atendimento hospitalar com urgência

### Execução com servidor Heroku

```bash
Originalmente o server encontra-se hospedado no Heroku, 
portanto para rodar o projeto, precisa apenas executar os arquivos de tela,
em ambos já estão o link para o servidor Heroku. 
```
### Pré-requisitos para execução das telas

```bash
#Instale a biblioteca PyQt5 referente a interface gráfica
$pip install PyQt5
#Para executar as telas acesse a pasta '\clientes' 
$python controladordeTelasPaciente.py
$python controladorTelaMedico.py

```

### Pré-requisitos para execução do server localmente
```bash
# Clone este repositório
$ git clone https://github.com/gsmalves/TriagemCovid.git
# Instale as dependências
$ pip install -r requirements.txt
# Versão do python utilizada: 3.9.4
# Para executar , acesse a pasta '\api' e execute o arquivo main
$ python main.py
# Obs: Nesse caso é necessário alterar o link nos arquivos controladorTelaMedico.py e 
# controladordeTelasPaciente.py que se encontram na pasta '\clientes',
# para a url referente ao servidor local, assim as telas serão executadas localmente.
```

