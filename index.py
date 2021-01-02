from flask import Flask, jsonify, json
from dao.pessoaDao import PessoaDao
from entidades.pessoa import Pessoa

app  = Flask(__name__)
rota = '/api/v1/pessoa'
dao  = PessoaDao()

@app.route(rota+'/todas', methods=['GET'])
def index():
    pessoas = dao.selecionarTudo()
    return respostaJson(pessoas)

@app.route(rota+'/<id_pessoa>', methods=['GET'])
def porId(id_pessoa):
    pessoa = dao.selecionarPorId(id_pessoa)
    return respostaJson(pessoa)

def respostaJson(resposta):
    return app.response_class(
        response=json.dumps(resposta),
        status=200,
        mimetype='application/json')

app.run(host='0.0.0.0',port=80,debug=True)