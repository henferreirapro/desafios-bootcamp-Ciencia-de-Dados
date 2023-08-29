def listar_conta(contas):
  for conta in contas:
    listar_contas = f"""
=============== Sua Conta ===============

  Agencia: {conta["agencia"]}
  C. Corrente: {conta["numero_conta"]}
  Titular: {conta["usuario"]["nome"]}

========================================="""
    print(listar_contas)

