#estabelecendo variáveis
Saldo = 0
num_saq = 0
LIMITE_SAQ = 3
Extrato = ""

#menu
while True:
  print(
    "Escolha uma opção abaixo: \n 1-Depósito \n 2-Saque \n 3-Extrato \n 4-Sair")
  opção = int(input("Digite a opção desejada:"))

  #opção de depósito
  if opção == 1:
    dep = int(input("Insira o valor a ser depositado:"))
    if dep > 0:
      Saldo += dep
      Extrato += f"Depósito de {dep :.2f} reais \n"
      print(f'Depósito realizado com sucesso, seu novo saldo é de {Saldo} reais')
    elif dep <= 0:
      print("Valor inválido, tente novamente")
  #opção de saque
  elif opção == 2:
    saq = int(input("Digite o valor a ser sacado:"))
    if saq > Saldo:
      Print("Saldo Insuficiente")
    elif saq > 500:
      print("Valor acima do limite permitido")
    elif num_saq > LIMITE_SAQ:
      print("Operação negada, limite diário de saques excedido")
    elif saq < 500 and num_saq < LIMITE_SAQ and saq <= 500:
      Saldo -= saq
      num_saq += 1
      Extrato += f"Saque de {saq :.2f} reais\n"
      print(f"Saque realizado com sucesso, seu novo saldo é de {Saldo} reais")

#opção de extrato
  elif opção == 3:
    print(Extrato)
    print((f'Seu saldo atual é de {Saldo} reais'))

  #opção de saída
  elif opção == 4:
    print("Obrigado pela preferência")
    break

#opções inválidas
  else:
    print("Opção inexistente")
    break
