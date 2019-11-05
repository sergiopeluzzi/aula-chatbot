class FileHandler :

    def __init__(self, arquivo) :
        self.arquivo = arquivo

    def lerArquivo(self) :
        f = open(self.arquivo, 'r')
        x = f.read()
        conversa = x.split(';')
        f.close()
        return conversa

    def comunica(self, pergunta) :
        conversa = self.lerArquivo()
        if (pergunta.lower() in conversa) :
            i = conversa.index(pergunta.lower())
            return conversa[i+1].capitalize()
        
        return 0
            

    def gravarArquivo(self, pergunta, resposta) :
        f = open(self.arquivo, 'a')
        f.write(';' + pergunta.lower())
        f.write(';' + resposta.lower())
        f.close()