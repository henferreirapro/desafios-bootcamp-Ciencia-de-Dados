# menu
def menu():
    menu = """
=============== Menu ===============
Escolha Uma das Opções Abaixo:
  [1] Depósito.
  [2] Saque.
  [3] Extrato.
  [4] Nova Conta.
  [5] Listas Contas.
  [6] Novo Usuário.
  [0] Sair.\n
Digite o Número da Opção Desejada:
  => """
    return int(input(menu))