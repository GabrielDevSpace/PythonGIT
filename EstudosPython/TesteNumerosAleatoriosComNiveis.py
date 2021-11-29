import random

print("************************************")
print("Testes Numeros Aleatorios com Niveis")
print("************************************")

numero_secreto = random.randint(1,100) #função random
total_de_tentativas = 3
rodada = 1

print("Niveis de Dificuldade: (1) Facil (2) Médio (3) Difícil")
nivel = int(input("Defina um Nivel: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  #("String {localvalor1} {localvalor2}".format(valor1,valor2)

    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")