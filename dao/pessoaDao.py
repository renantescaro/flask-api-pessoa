from entidades.pessoa import Pessoa

class PessoaDao:
    def __init__(self):
        self.pessoas = [
            Pessoa(1, 'Renan', 24),
            Pessoa(2, 'Ana', 22),
            Pessoa(3, 'Luana', 23)
        ]

    def selecionarTudo(self):
        pessoa = Pessoa()
        return pessoa.serializarArray(self.pessoas)

    def selecionarPorId(self, idPessoa):
        for pessoa in self.pessoas:
            if int(pessoa.id) == int(idPessoa):
                return pessoa.serializar()