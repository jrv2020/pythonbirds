class Pessoa():
    olhos=2

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
        ronaldo.olhos = 1
        del ronaldo.olhos
        print(ronaldo.__dict__)
        print(yaya.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(ronaldo.olhos)
        print(yaya.olhos)
        print(id(Pessoa.olhos), id(ronaldo.olhos), id(yaya.olhos))