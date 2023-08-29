import criar_usuario

def nova_conta(agencia, numero_conta, usuarios):
  cpf = input("Por favor informe o CPF do usuário:\n => ")
  usuario = criar_usuario.filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\nConta criada com sucesso!\n")
    return {
      "agencia": agencia,
      "numero_conta": numero_conta,
      "usuario": usuario  
    }

  print("\nFalha!!! Não encontramos uma conta com esse CPF.")
  