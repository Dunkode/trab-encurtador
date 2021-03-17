import os
from encurtador import *
import time

u = Encurtador()
while True:
    print("{:=^50}".format("ENCURTADOR"))
    print("Selecione a ação desejada:\n"+ 
          "(1) - Encurtar URL\n"+
          "(2) - Conversão de inteiro para string\n"+
          "(3) - Conversão de string para inteiro\n"+
          "(4) - Mostrar Hash\n"+
          "(5) - Salvar tabelas\n"+
          "(6) - Carregar arquivo salvo\n"+
          "(0) - Fechar programa :C ")
    escolha = int(input())
    os.system("cls")


    if escolha == 1:
        url = input("Digite a URL (COM HTTPS://): ")
        print(u.encurtar(url))
        time.sleep(2)
        os.system("cls")

    
    elif escolha == 2:
        inteiro = int(input("a: "))
        print(u.toBase(inteiro))
    
   
    elif escolha == 3:
        inteiro = input("b: ")
        print(u.to10(inteiro))

    elif escolha == 4:
        u.listar_urls()

    elif escolha == 5:
        u.save_dic()

    elif escolha == 6:
        u.load_dic()


    elif escolha == 0:
        break