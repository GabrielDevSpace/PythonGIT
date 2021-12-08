import random
print("**************************************************")
print("Jogo de forca para aplicar o aprendizado de python")
print("**************************************************")

palavras_secreta = ['banana','carro','legumes','submarino','aviador','sorte']
quantidade_palavras_secreta = len(palavras_secreta) - 1
identificador = random.randint(0,quantidade_palavras_secreta)
palavra_escolhida = (palavras_secreta[identificador])
print(palavra_escolhida)

falhou = False
acertou = False

while (not falhou and not acertou):
    chute = input("Digite uma LETRA: ")
    print("Jogando...")