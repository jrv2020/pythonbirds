class Pessoa():
    def __init__(self, nome = None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f' Olá, id={id(self)}'


if __name__ == '__main__':
        p = Pessoa('ronaldo')
        print(Pessoa.cumprimentar(p))
        print(id(p))
        print(p.cumprimentar())
        print(p.nome)
        p.nome = 'jose'
        p.idade=51
        print(p.nome)
        print(p.idade)
