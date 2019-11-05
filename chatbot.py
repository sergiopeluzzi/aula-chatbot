#classe Chatbot
from fileHandler import FileHandler

class Chatbot :
    fh = FileHandler('newconversa.txt')

    def __init__(self, nome) :
        self.nome = nome
        resp = self.intro()
        if resp.upper() == 'S' :
            while self.conversar().lower() != '.sair' :
                self.conversar()            
        else :
            self.tchau()
   
    def intro(self) :
        print("{}: Olá meu nome é {}".format(self.nome, self.nome))
        print("{}: Eu sou uma I.A. que irá aprender com você".format(self.nome))
        resp = input("{}: Vamos começar? (S/N): ".format(self.nome))
        return resp
    
    def conversar(self) :
        r = input("Você: ")

        if r == '.sair' :
            return r

        if self.fh.comunica(r) != 0 :
            print(self.nome + ": " + self.fh.comunica(r))
        else :
            self.aprender(r)
            
        return r

    def aprender(self, p) :
        print(self.nome + ": Não sei responder!")
        r = input(self.nome + ": Qual seria a resposta para essa pergunta? ")
        self.fh.gravarArquivo(p, r)

            
    def tchau(self) :
        print("{}: Tchau".format(self.nome))

    