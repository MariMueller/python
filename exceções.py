

def divisao(a,b):
	try:
		resultado = a/b
		print(resultado)

	except ZeroDivisionError:
	    print("Erro")
	except TypeError as e:
		print (f'erro: o tipo da divisão está errado. \n Detalhes: {e}')
	else:
		print('sem exceções')

divisao(10,2)