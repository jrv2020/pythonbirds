class Pessoa():
    olhos=2

    def __init__(self, *filhos, nome = None, idade=51):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f' Olá, id={id(self)}'

    @staticmethod
    def metodo_estatico():
        return 7*6

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}-olhos{cls.olhos}'
        return f'Meu nome é {self.nome}'


class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos=3

class Mulher(Pessoa):
    pass

if __name__ == '__main__':
        ronaldo = Mutante(nome='ronaldo')
        yaya = Mulher(nome='yaya')
        ronaldo = Mutante(yaya, nome='ronaldo')
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
        print(Pessoa.olhos)
        print(ronaldo.olhos)
        print(yaya.olhos)
        print(id(Pessoa.olhos), id(ronaldo.olhos), id(yaya.olhos))
        print(Pessoa.metodo_estatico(),'e', ronaldo.metodo_estatico())
        print(Pessoa.nome_e_atributos_de_classe(), 'e', ronaldo.nome_e_atributos_de_classe())
        pessoa=Pessoa('Anônimo')
        print(isinstance(pessoa, Pessoa))
        print(isinstance(pessoa, Homem))
        print(isinstance(ronaldo, Pessoa))
        print(isinstance(ronaldo, Homem))
        print(yaya.olhos)
        print('Digite uma palavra e pressione enter')
        input('-->')
        print(ronaldo.olhos)
        print(yaya.cumprimentar())
        print(ronaldo.cumprimentar())