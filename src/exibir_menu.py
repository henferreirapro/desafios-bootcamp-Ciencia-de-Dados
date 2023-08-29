# menu
def menu():
    menu = """
=============== Menu ===============
Escolha Uma das Opções Abaixo:
  [1] Depósito.
  [2] Saque.
  [3] Extrato.
  [4] Criar Usuário.
  [5] Criar Conta.
  [6] Listas Contas.
  [0] Sair.\n
Digite o Número da Opção Desejada:
  => """
    return int(input(menu))