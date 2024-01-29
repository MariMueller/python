def soma(num1,num2): 

	calculo = num1+num2 

	print(f'O resultado da soma é: {calculo}')

def multiplicacao(num1,num2): 

	calculo = num1*num2

	print(f'O resultado da multiplicacao é: {calculo}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1,num2)
multiplicacao(num1,num2)

# open
# escrita
# leitura
#print(f'O resultado da multiplicacao é: {calculo}')

file = 'arquivo.txt'

#open somente para leitura

arquivo_leitura = open(file, "r") #open somente para leitura

#abertura para escrita

arquivo_escrita = open(file, "w") #open somente para escrita

#abertura de arquivos binarios

arquivo_binario = open(file, "wb")

