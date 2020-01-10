class Pessoa():
    def __init__(self, *filhos, nome = None, idade=51):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f' Olá, id={id(self)}'


if __name__ == '__main__':
        yaya = Pessoa(nome='yaya')
        ronaldo = Pessoa(yaya, nome='ronaldo')
        print(Pessoa.cumprimentar(ronaldo))
        print(id(ronaldo))
        print(ronaldo.cumprimentar())
        print(ronaldo.nome)
        print(ronaldo.idade)
        for filho in ronaldo.filhos:
            print(filho.nome)
        ronaldo.sobrenome = 'vieira'
        del ronaldo.filhos
        print(ronaldo.__dict__)
        print(yaya.__dict__)
        