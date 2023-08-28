import menu
import depositar
import sacar
import exibir_extrato

def main():
  saldo = 0
  extrato = ""
  numeros_saque = 0
  LIMITE = 500
  LIMITE_SAQUE = 3

  while True:
    opcao = menu.menu()

    # DEPÓSITO
    if opcao == 1:
      valor_deposito = float(input("\nQuanto Deseja Depositar?\n => "))

      saldo, extrato = depositar.depositar(valor_deposito, saldo, extrato)
    
    # SACAR
    elif opcao == 2:
      if numeros_saque < LIMITE_SAQUE:
        valor_saque = float(input("Digite o Valor do Saque:\n "))
        numeros_saque += 1
      
      else:
        print("Seu limite de Saque Diário foi excedido. \nPor favor, tente novamente amanhã!")
        
      saldo, extrato = sacar.sacar(
        saldo=saldo, 
        valor_saque=valor_saque, 
        extrato=extrato, 
        limite=LIMITE, 
        )
  
    # EXTRATO
    elif opcao == 3:
      exibir_extrato.extrato(saldo, extrato=extrato)

    elif opcao == 4
      

main()