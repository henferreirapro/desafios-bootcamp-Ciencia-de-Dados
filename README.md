# desafios-bootcamp-Ciencia de Dados
 Repositorio para os desafios feitos no Bootcamp Potência Tech powered by iFood | Ciência de Dados com a Digital Innovation One - DIO.
<h1>Sistema Bancario em Python - v2</h1>

  - Nessa versão iremos refazer todas as funcionalidades ja existentes na versão 1 do sistema utilizando as funções do Python.

  - Alem de criarmos as funções saque, deposito extrato e sair e menu novamente, iremos acrescentar mais duas novas funções, cadastrar usuario e cadastrar conta corrente.

<h2>Regras Para Cada Função</h2>

<h3>Depósito:</h3>

  - A função depósito deve receber os argumentos apenas por posição(positional only), usando a barra **/** ao final dos argumentos.

  - Sugestão de argumentos: saldo, valor, extrado.
  
  - Sugestão de retorno: saldo e extrato.

___  
<h3>Saque:</h3>

  - A função saque deve receber os argumentos apenas por nome(keyword only), passado com * no começo, antes de declarar os argumentos.

  - Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.

  - Sugestão de retorno: saldo e extrato.

___
<h3>Extrato:</h3>

  - A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).

  - Sugestão de Argumentos posicionis: saldo.

  - Sugestão de Argumentos nomeados: extrato.

___
<h3>Criar Usuário:</h3>

  - O programa deve armazenas usuários em uma lista.

  - Dados do usuário devem conter: nome, data de nascimento, CPF e endereço.

  - O endereço deve conter: logradouro, número, bairro - sigla do estado.

  - Não pode ser cadastrado 2 usuários com mesmo CPF, então precisamos de um filtro para verificar se já existe um usuário com CPF informado.

  