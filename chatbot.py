#classe Chatbot
class Chatbot :
    conversa = []
    arquivo = 'conversa.txt'

    f = open(arquivo, 'r')
    x = f.read()
    conversa = x.split(';')
    f.close()

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
        resp = input("{}: Vamos começar? ".format(self.nome))
        return resp
    
    def conversar(self) :
        r = input("Você: ")

        if r == '.sair' :
            return r

        if r.lower() in self.conversa :
            i = self.conversa.index(r.lower())
            print(self.nome + ": " + self.conversa[i+1].capitalize())
        else :
            self.conversa.append(r.lower())
            f = open(self.arquivo, 'a')
            f.write(';' + r.lower())
            print(self.nome + ": Não sei responder!")
            c = input(self.nome + ": Qual seria a resposta para essa pergunta? ")
            self.conversa.append(c.lower())
            f.write(';' + c.lower())
            f.close()
        return r
            
    def tchau(self) :
        print("{}: Tchau".format(self.nome))

    