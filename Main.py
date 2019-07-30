# -*-coding: utf-8 -*-

from chatterbot.trainers import ListTrainer  # Treinador
from chatterbot import ChatBot  # Chatbot
from random import randint
import os  # SO
from time import sleep


def main():

    global bot
    global nome
    global cod

    bot = ChatBot('Friday')
    op = input('Sua primeira vez aqui?')
    op = op.lower()  # Deixar resposta minuscula

    if op == 'nao' or op == 'não':
        cod = str(lobby())
        arq = open('Pessoas/' + cod, "r")
        nome = arq.readline()
        arq.close()

    elif op == 'sim':
        cod = str(cadastro())
        parq = open('Pessoas/' + cod, "r+")
        texto = parq.readlines()
        nome = (str(input('Qual seu nome:')))
        texto.append(nome)
        parq.writelines(texto)
        parq.close()

    else:
        print('Error')
        print('Digite sim ou não')
        sleep(2)
        main()

    nome = nome.title()
    cod = str(cod)
    treinador()
    bott = escolhe_pessoa()
    bott = str(bott.title())
    nome = nome.rstrip('\n')
    bott = bott.rstrip('\n')
    bot_respost(str(bott), str(nome), str(cod))

    return 0


def treinador():
    bot.set_trainer(ListTrainer)
    for Base in os.listdir('Base'):  # Ler os aquivos e as linhas
        chats = open('Base/' + Base, "r").readlines()
        bot.train(chats)




def bot_respost(bott, name, iden):  # bott nome do cara,nome nome da pessoa,inden numero d identificação
    print('Para sair digite "exit"')
    print(str('{}:Oi'.format(bott)))
    sarquivo = open('Pessoas/' + iden, "r+")
    arqp = sarquivo.readlines()
    while True:  # ler e responder as questões
        pessoa = input('{}:'.format(name))
        pessoa = pessoa.title()  # Deixar Primeiras letras maiusculas
        if pessoa == 'Exit':
            sarquivo.writelines(arqp)
            sarquivo.close()
            saidera(name)
            return 0

        resp = str(bot.get_response(pessoa))
        resp = resp.rstrip('\n')
        if resp ==  "Filho D Puta":
            resp = "Olha só"
        print('{}:'.format(bott) + str(resp))
        arqp.append("\n"+pessoa)


def lobby():  # resposta nao
    pas = input(str('Qual era seu numero de identificação:'))
    print("Estamos carregando seus dados")
    pas = str('P' + pas + '.txt')
    sleep(3)
    return str(pas)


def saidera(name):
    print('Agradeçemos {} por sua paciencia!!'.format(name))
    print('Volte sempre!!')
    print('Desenvolvedores:Luis Ricardo e Paulo Henrique')
    op = input(str('Deseja fazer algum comentario?(Responda com sim ou não)'))
    op = op.title()
    if op == 'Sim':
        parq = open('Base/' + 'Comentarios.txt', "r+")
        texto = parq.readlines()
        coment = (str(input('Qual seu comentario:')))
        coment = (coment + "\n")
        texto.append(coment)
        parq.writelines(texto)
        parq.close()
    else:
        print('Tmj Quebrada!')


def cadastro():  # resposta sim
    cont = os.listdir('Pessoas')
    cont = len(cont)
    ind = int(cont) + 1
    inde = str(ind)
    inde = str('P' + inde + '.txt')
    criar_arquivo(str(inde))
    print('Seu numero de indentificacao e:{}'.format(ind))
    return inde


def criar_arquivo(num):
    arq = open('Pessoas/' + num, "w+")
    arq.close()


if __name__ == '__main__':
    main()
