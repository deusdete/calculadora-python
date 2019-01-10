def soma (x,y): 
	result = x + y
	return print("A soma é igual: ", result)

def sub (x,y): 
	result = x - y
	return print("A subtração é igual: ", result)

def mul (x,y): 
	result = int(x * y)
	return print("A multiplicação é igual: ", result)

def div (x,y): 
	result = x / y
	return print("A soma é igual: ", result)

cont = 0

while cont ==0:

	print("\n\n\n\nCalcuradora em Python\n\n")
	print("Por favor, escolha uma das opições abaixo:\n")
	print("1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divição (/)")

	opicao = int(input("Qual operação você quer fazer? "))
	if (opicao >=1) and (opicao <=4):
		x = float(input("Digite o primeiro numero: "))
		y = float(input("Digite o segundo numero: "))
	else: print("Você não quer fazer nenhuma operação, thau!")

	if opicao == 1:
		soma(x,y)
	elif opicao == 2:
		sub(x,y)
	elif opicao == 3:
		mul(x,y)
	elif opicao == 4:
		div(x,y)

	conf = 3
	while (conf < 0) or ( conf > 2): 
		resp = int(input("Deseja continuar (0) - SIM, 1 -(NÃO): "))
		if resp == 0:
			print("Vamos lá")
			conf = resp
		elif resp == 1:
			print("Você não quer fazer nenhuma operação, thau!")
			conf = resp
			cont = 1
		else:
			print("Opição invalida!")


