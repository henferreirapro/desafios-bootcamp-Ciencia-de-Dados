def novo_usuario(usuarios):
  cpf = input("\nPor favor informe o CPF(somente números):\n => ")
  usuario = filtrar_usuario(cpf, usuarios)

  # Caso já exista o usuário cadastrado
  if usuario:
    print("\nCPF já cadastrado, você já possui cadastro no nosso banco!")
    return

  nome = input("\nPor favor informe seu nome completo:\n=> ")
  data_nascimento = input("\nInforme a sua data de nascimento (dd-mm-aaaa): \n => ")
  endereço = {
    "rua": input("\nDigite o nome da rua por favor:\n => "),
    "numero_rua": input("\nDigite o número do endereço:\n => "),"bairro": input("\nDigite o bairro por favor:\n => "),
    "cidade": input("Digite a cidade(Ex: São Paulo - SP):\n => ")
  }
  print(f"\nSeu cadastro foi criado com sucesso!\n")

  usuarios.append({
    "nome": nome, 
    "data_nascimento": data_nascimento,
    "cpf": cpf,
    "endereço": endereço
  })


# Filtrar se o usuario existe
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
