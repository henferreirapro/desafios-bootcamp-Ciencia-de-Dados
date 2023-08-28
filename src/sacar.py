import mensagens

def sacar(*, saldo, valor_saque, extrato, limite):
  # vericando se existe saldo e se é maior que 0.
  if valor_saque <= saldo and valor_saque > 0 and valor_saque <= limite:
    mensagens.msg_transacao(valor_saque, transacao="Saque")

    # retirando valor de saque de saldo
    saldo -= valor_saque
    
    # add saque em extrato
    extrato += f"   Saque de R$ {valor_saque:.2f}.\n"

  # Caso seja um saldo negativo. 
  elif valor_saque < 0:
    print("Não é possivel sacar valores negativos, por favor tente novamente!")   
  
  elif valor_saque > limite:
    print(f"Saque não altorizado! \nO limite por saque é de R$ {limite:.2f}.")

  else:
    print("Saldo insuficiente. Por Favor, faça um deposito antes de tentar sacar.")

  return saldo, extrato
