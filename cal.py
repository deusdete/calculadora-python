def soma (x, y): 
	return x + y

def subtracao (x, y): 
	return x - y

def multiplicacao (x, y): 
	return int(x * y)

def divisao (x, y): 
	return x / y

def calculadora (x, y, operacao):
	result = operacao(x, y)
	return print(f"A {operacao.__name__} é igual: {result}")

cont = 0

while cont ==0:

	print("\n\n\n\nCalculadora em Python\n\n")
	print("Por favor, escolha uma das opções abaixo:\n")
	print("1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)")

	opcao = int(input("Qual operação você quer fazer? "))
	if (opcao >=1) and (opcao <=4):
		x = float(input("Digite o primeiro número: "))
		y = float(input("Digite o segundo número: "))
	else: print("Você não quer fazer nenhuma operação, tchau!")

	if opcao == 1:
		calculadora(x, y, soma)
	elif opcao == 2:
		calculadora(x, y, subtracao)
	elif opcao == 3:
		calculadora(x, y, multiplicacao)
	elif opcao == 4:
		calculadora(x, y, divisao)

	conf = 3
	while (conf < 0) or ( conf > 2): 
		resp = int(input("Deseja continuar (0) - SIM, 1 -(NÃO): "))
		if resp == 0:
			print("Vamos lá")
			conf = resp
		elif resp == 1:
			print("Você não quer fazer nenhuma operação, tchau!")
			conf = resp
			cont = 1
		else:
			print("Opção inválida!")


