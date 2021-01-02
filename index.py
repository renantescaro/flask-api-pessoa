from flask import Flask, jsonify, json

app = Flask(__name__)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade
    
    def serializar(self):
        return {
            'nome':self.nome,
            'idade':self.idade,
        }


@app.route('/api/v1/pessoa/todas', methods=['GET'])
def index():
    pessoas = [
        Pessoa('Renan',24).serializar(),
        Pessoa('Amanda',19).serializar(),
        Pessoa('Leticia',32).serializar()
    ]
    return app.response_class(
        response=json.dumps(pessoas),
        status=200,
        mimetype='application/json'
    )


app.run(host='0.0.0.0',port=80,debug=True)