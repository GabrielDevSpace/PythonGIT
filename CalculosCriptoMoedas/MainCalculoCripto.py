import CalculoCripto

print("************************")
print("Opções de Calculos Crito")
print("************************")
print("DIGITE:")
print("(1) para calcular o PREÇO baseado em SUPLY e MARKETCAP")
print("(2) para calcular o MARKETCAP baseado em PREÇO e SUPLY")
calculo = int(input("Digite o calulo Pretendido:"))

if(calculo == 1):
    CalculoCripto.calculo_cripto_price()
elif(calculo == 2):
    CalculoCripto.calculo_cripto_marketcap()