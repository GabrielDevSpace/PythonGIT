import CalculoCripto
import TesteAdivinhação

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    CalculoCripto.calculo_cripto()
elif (jogo == 2):
    print("Jogando adivinhação")
    TesteAdivinhação.teste_adivinhacao()