saldo = 0
extrato = ""
numeros_saque = 0
LIMITE = 500
LIMITE_SAQUE = 3

menu = """
Escolha Uma das Opções Abaixo:
  [1] Depósito.
  [2] Saque.
  [3] Extrato.
  [0] Sair.
Digite o Número da Opção Desejada:
  """

while True:
    opcao = int(input(menu))
        
    # Deposito
    if opcao == 1:
        valor_deposito = float(input("Quanto Deseja Depositar?\n "))
        if valor_deposito > 0:
          
          # add valor de deposito em saldo
          saldo += valor_deposito

          # add deposito em extrato
          extrato += f"Depósito de R$ {valor_deposito:.2f}.\n"
        else:
          print("Valor é Negativo, por favor adicione apenas Valores Positivos")

    # Saque
    elif opcao == 2:
        # validando numeros de saque.
        if numeros_saque < LIMITE_SAQUE:
          valor_saque = float(input("Digite o Valor do Saque:\n "))
          numeros_saque += 1
        
          # vericando se existe saldo e se é maior que 0.
          if valor_saque <= saldo and valor_saque > 0 and valor_saque <= LIMITE:
            
            # retirando valor de saque de saldo
            saldo -= valor_saque
            
            # add saque em extrato
            extrato += f"Saque de R$ {valor_saque:.2f}.\n"

          # Caso seja um saldo negativo. 
          elif valor_saque < 0:
            print("Não é possivel sacar valores negativos, por favor tente novamente!")   
          
          elif valor_saque > LIMITE:
            print(f"Saque não altorizado! \nO limite por saque é de R$ {LIMITE:.2f}.")

          else:
            print("Saldo insuficiente. Por Favor, faça um deposito antes de tentar sacar.")
        
        else:
          print("Seu limite de Saque Diário foi excedido. \nPor favor, tente novamente amanhã!")
    
    # Extrato
    elif opcao == 3:
      if extrato == "":
          print("Você ainda não possui movimentações na conta!")
      else:
        print(extrato)
        print(f"Seu Saldo Atual é de:\n {saldo}")

    # Sair
    elif opcao == 0:
      print("Saindo da sessão... \nMuito obrigado por usar o nosso sistema, volte sempre! :)")
      break

    else:
      print("Opção invalida! :( \ntente novamente por favor!")

