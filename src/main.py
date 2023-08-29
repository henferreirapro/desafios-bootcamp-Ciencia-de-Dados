import exibir_menu
import exibir_deposito
import exibir_saque
import exibir_extrato
import criar_usuario
import criar_conta
import exibir_contas


def main():
  LIMITE = 500
  LIMITE_SAQUE = 3
  AGENCIA = "0001"

  saldo = 0
  extrato = ""
  numeros_saque = 0
  usuarios = []
  contas = []

  while True:
    opcao = exibir_menu.menu()

    # DEPÓSITO
    if opcao == 1:
      valor_deposito = float(input("\nQuanto Deseja Depositar?\n => "))

      saldo, extrato = exibir_deposito.depositar(valor_deposito, saldo, extrato)
    
    # SACAR
    elif opcao == 2:
      if numeros_saque < LIMITE_SAQUE:
        valor_saque = float(input("Digite o Valor do Saque:\n "))
        numeros_saque += 1
      
      else:
        print("Seu limite de Saque Diário foi excedido. \nPor favor, tente novamente amanhã!")
        
      saldo, extrato = exibir_saque.sacar(
        saldo=saldo, 
        valor_saque=valor_saque, 
        extrato=extrato, 
        limite=LIMITE, 
        )
  
    # EXTRATO
    elif opcao == 3:
      exibir_extrato.extrato(saldo, extrato=extrato)

    # CRIAR USUARIO
    elif opcao == 4:
      criar_usuario.novo_usuario(usuarios)
    
    #CRIAR CONTA 
    elif opcao == 5:
      numero_conta = len(contas) + 1
      conta = criar_conta.nova_conta(AGENCIA, numero_conta, usuarios)
      
      if conta:
        contas.append(conta)

    # LISTAR CONTAS
    elif opcao == 6:
      exibir_contas.listar_conta(contas)
    
    # SAIR 
    elif opcao == 0:
      print("Saindo da sessão... \nMuito obrigado por usar o nosso sistema, volte sempre! :)")
      break

    # OPÇÃO INVALIDA.
    else:
      print("Opção invalida! :( \ntente novamente por favor!") 


main()