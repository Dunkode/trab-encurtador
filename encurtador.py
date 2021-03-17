from pickle import dump, load 
from math import floor
from os import path, getcwd

class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = str(getcwd() + "/urls.dat")
        self.load_dic()
        self.indice = 1000 + len(self.dic)

    def load_dic(self):
        if path.exists(self.nome_arq):
            print(self.nome_arq)
            arq = open(self.nome_arq, "rb")
            self.dic = load(arq)
            arq.close()
        else:
            arq = open(self.nome_arq, "wb").close()


    def save_dic(self):
        with open(self.nome_arq, "wb") as arq:
            dump(self.dic, arq)

    def toBase(self, num, b = 62):
        if b <= 0 or b > 62:
            return 0
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        r = num % b
        res = base[r];
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def to10(self, num, b = 62):
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        ##url = url[url.find("/", 8)+1:]
        
        url_encurtada = self.toBase(self.indice)
        print(url_encurtada)

        self.dic[self.indice] = (url_encurtada, url)
        self.indice += 1
        self.save_dic()

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1]

    def listar_urls(self):
        print(self.dic)
   