print("****************************")
print("Laços com FOR RANGE")
print("****************************")
numero_secreto = 46
total_de_tentativas = 3


for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  #("String {localvalor1} {localvalor2}".format(valor1,valor2)

    chute_str = input("Digite o seu número de 1 ate 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Atenção... Digite um numero de 1 ate 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


print("Fim do jogo")