#("String {localvalor1} {localvalor2}".format(valor1,valor2)
print("*************************")
print("Exemplo Formatando Peços")
print("*************************")

#https://docs.python.org/3/library/string.html#formatexamples

print("R$ 132.23 = R$ {}".format(132.32))
print("R$ 132.23 = R$ {:f}".format(132.32)) # :f transforma em float porem sem formatação de casas decimais
print("R$ 132.23 = R$ {:2f}".format(132.32)) # :2f exibe apenas 2 casas decimais

#exemplo de Alinhamento de string para os valores sairem alinhados de acordo com as casa decimais
print("SEM ALINHAMENTO")
print("R$ 132.23  = R$ {:.2f}".format(132.32))
print("R$ 1450.23 = R$ {:.2f}".format(1450.2))

print("COM ALINHAMENTO")
print("R$ 132.23  = R$ {:7.2f}".format(132.32)) #acrecenta o numero de espaços necessario na frente do valor para se tornar 7 caracteres
print("R$ 1450.23 = R$ {:.2f}".format(1450.2))

print("ALINHAMENTO COM PREENCHIMENTO ESPECIFICO")
print("R$ 132.23  = R$ {:07.2f}".format(132.32)) #acrecenta o 0 (ZERO) na frente do valor para se tornar 7 caracteres
print("R$ 1450.23 = R$ {:.2f}".format(1450.2))

print("DATA")
print("R$ 132.23  = R$ {:07.2f}".format(132.32)) #acrecenta o 0 (ZERO) na frente do valor para se tornar 7 caracteres
print("HOJE é DIA 01/11/2021 = {}/{}/{} ".format(1,11,2021)+"Sem Preenchimento")
print("HOJE é DIA 01/11/2021 = {:02d}/{}/{} ".format(1,11,2021)+"Com Preenchimento")
print("HOJE é DIA 01/03/2021 = {:02d}/{:02d}/{} ".format(1,3,2021)+"Com Preenchimento")