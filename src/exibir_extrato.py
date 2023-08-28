def extrato(saldo, /, *, extrato):
    if extrato == "":
      print("Você ainda não possui movimentações na conta!")
    else:
      print(f"""
=========== EXTRATO DA CONTA ===========
            
  {extrato}

     =============================

  Seu Saldo Atual é de: R$ {saldo:.2f}
========================================
""")
      
    return 