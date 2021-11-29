
def calculo_cripto_price():
    print("**************************************************************************************")
    print("Calculadora para encontrar PREÇO de uma Cripto Baseado em um futuro Suply e Market Cap")
    print("**************************************************************************************")

    #Usando o TOKEM da SHIBAINU como exemplo
    #Abaixo os dados atuais do toke na data de hoje 27/11/2021
    # PRICE = $0.00003934
    # MARKET CAP = $21.600.175.588 21600175588
    # SUPLY = 549.055.950.000.000 549055950000000
    # Calculo Basico para se chegar no PRICE = MC / SUPLY
    # 21.600.175.588 / 549.055.950.000.000 = $0.00003934

    mc = float(input("Digite o Market Cap: ")) #Digitar sem os pontos ou virgulas
    suply = float(input("Digite o Suply: ")) #Digitar sem os pontos ou virgulas
    resultado = mc /suply
    print("o Preço é: ${:10.9f} ".format(resultado)) #Para aumentar o numero de casas decimais altere na função {:10.9f} para {:15.12f} por exemplo

def calculo_cripto_marketcap():
    print("**************************************************************************************")
    print("Calculadora para encontrar o MARKETCAP de uma Cripto Baseado em um futuro Suply e Preço")
    print("**************************************************************************************")

    #Usando o TOKEM da SHIBAINU como exemplo
    #Abaixo os dados atuais do toke na data de hoje 27/11/2021
    # PRICE = $1 preço alvo que pretende chegar
    # MARKET CAP = queremos identicar qual seria o MC para atingir o preço sugerido
    # SUPLY = 549.055.950.000.000 549055950000000
    # Calculo Basico para se chegar no MARKETCAP = PRICE * SUPLY

    price = float(input("Digite o Preço Alvo: ")) #Digitar sem os pontos ou virgulas
    suply = float(input("Digite o Suply: ")) #Digitar sem os pontos ou virgulas
    resultado = price * suply
    print("o Market Cap necessário é: ${:.2f} ".format(resultado)) #Para aumentar o numero de casas decimais altere na função {:10.9f} para {:15.12f} por exemplo

