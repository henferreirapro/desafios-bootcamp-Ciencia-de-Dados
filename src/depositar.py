import mensagens

def depositar(valor_deposito, saldo, extrato, /):
  if valor_deposito > 0:
    mensagens.msg_transacao(valor_deposito, transacao="Depósito")
    
    # add valor de deposito em saldo
    saldo += valor_deposito

    # add deposito em extrato
    extrato += f" Depósito de R$ {valor_deposito:.2f}.\n"
  else:
    print("Valor é Negativo, por favor adicione apenas Valores Positivos.")

  return saldo, extrato



   
