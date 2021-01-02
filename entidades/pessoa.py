class Pessoa:
    def __init__(self, id=0, nome='', idade=0):
        self.id    = id
        self.nome  = nome
        self.idade = idade
    
    def serializar(self):
        return {
            'id'   : self.id,
            'nome' : self.nome,
            'idade': self.idade}
    
    def serializarArray(self, pessoasArrayObj):
        pessoasSerializadas = []
        for pessoa in pessoasArrayObj:
            pessoasSerializadas.append(pessoa.serializar())
        return pessoasSerializadas