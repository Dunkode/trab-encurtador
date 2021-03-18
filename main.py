import os
from encurtador import *
import time

u = Encurtador()
while True:
    print("{:=^50}".format("ENCURTADOR"))
    print(
          "[ 1 ] - Encurtar URL\n"+
          "[ 2 ] - Conversão de inteiro para string\n"+
          "[ 3 ] - Conversão de string para inteiro\n"+
          "[ 4 ] - Mostrar Hash\n"+
          "[ 5 ] - Salvar tabelas\n"+
          "[ 6 ] - Carregar arquivo salvo\n"+
          "[ 0 ] - Fechar programa\n"+
          "Selecione a ação desejada: ",end="")
    escolha = int(input())
    os.system("cls")


    if escolha == 1:
        url = input("Digite a URL: ")
        time.sleep(1)
        print("Encurtando URL...")
        time.sleep(2)
        small = u.encurtar(url)
        print("Concluído!!")
        time.sleep(2)
        print(f"Nova URL: {u.takeInitiURL(url,small)}")
        time.sleep(2)
        print()
    
    elif escolha == 2:
        inteiro = int(input("Insira o Inteiro: "))
        time.sleep(1)
        print("O número", inteiro, "para string fica:", u.toBase(inteiro))
        time.sleep(2)
        print()
   
    elif escolha == 3:
        string = input("Insira a String: ")
        time.sleep(1)
        print("A string", string, "para número fica:", u.to10(string))
        time.sleep(2)
        print()

    elif escolha == 4:
        print("No momento o hash está assim: ")
        time.sleep(0.5)
        u.listar_urls()
        time.sleep(2)
        print()

    elif escolha == 5:
        u.save_dic()
        time.sleep(1)
        print("Tabelas salvas no arquivo urls.dat!!")
        time.sleep(2)
        print()

    elif escolha == 6:
        u.load_dic()
        time.sleep(1)
        print("Arquivo urls.dat salvado no dicionário interno do programa!")
        time.sleep(2)
        print()

    elif escolha == 0:
        print('Já vai? :\'(')
        time.sleep(1)
        break