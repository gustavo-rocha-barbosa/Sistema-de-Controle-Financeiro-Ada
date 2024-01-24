# -*- coding: utf-8 -*-
"""Projeto_LPII.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TFy4v7PL8u1MiYhj3H8kZDf8NNIuWmk5

# 💸 Projeto Final | Sistema de Controle Financeiro

Deverá ser desenvolvido um sistema para controle financeiro que receba as movimentações e as armazena em um arquivo csv ou json.

O sistema deverá ser capaz de realizar as seguintes operações:

- **Criar** novos registros e identificar a data que o registro foi feito, qual tipo de movimentação, valor.

  - Os tipos podem ser:
    - Receita: o valor deve ser tratado como numérico e armazenado normalmente.
    - Despesas: o valor deve ser recebido como positivo, mas armazenado como negativo
    - Investimento: deve ter uma informação a mais de 'Montante', em que será calculado quanto o dinheiro rendeu desde o dia que foi investido.
    Para essa finalidade utilize a seguinte formula: $M = C * (1 + i)^t$ ([Saiba mais](https://matematicafinanceira.org/juros-compostos/)), considere tudo em dias.
- **Ler** registros: Deverá ser possível consultar os registros por data, tipo ou valor.
- **Atualizar** registros: No caso de atualização, pode-se atualizar o valor, o tipo e a data deverá ser a de atualização do registro.
- **Deletar**: Deverá ser possível deletar o registro (caso necessário, considere o indice do elemento como ID)

Outras funcionalidades:
- Crie uma função ```atualiza_rendimento``` que atualize os valores de rendimento sempre que chamada.
- Crie uma função ```exportar_relatorio```, que seja possível exportar um relatorio final em csv ou json.
- Crie pelo menos uma função de agrupamento, que seja capaz de mostrar o total de valor baseado em alguma informação (mes, tipo...)
- Crie valores separados para identificar a data (dia, mes, ano)

---

👩‍💻 **O que vai ser avaliado**:

- Se as funções e operações cuprem o seu objetivo
- Reprodutibilidade do código: vou executar!

👉🏻 **Envio do projeto**:
- Via LMS **individualmente.** <br>
  Apesar de ser em grupo, cada um de vocês precisa submeter o projeto.
- Formato: arquivo .py ou .ipynb.
- 📅 29/01, até as 23h59.

⚠️ **Atenção**:
- Não utilize a biblioteca pandas para resolução desse exercício
"""

'''from datetime import date
modelo_dados = {
    "lancamentos":[
        {
          "tipo":"receita", #receita,despesas,investimento
          "valor": 0.0,
          "data_cadastro": date.today().strftime('%d/%m/%Y'),
        },
        {
          "tipo":"investimento", #receita,despesas,investimento
          "valor": 0.0, #capital
          "data": date.today(),
          "taxa": 0.1,
          "data_investimento": date.today(),
          "valor_atualizado": 0.0,
          "data_atualizacao": date.today(),
        }
      ]
    }

modelo_dados["lancamentos"]'''

from datetime import date, datetime
dados = {
    "lancamentos":[
      ]
    }

dados



"""# Exportar relatorio/dados"""

#Crie uma função exportar_relatorio, que seja possível exportar um relatorio final em csv ou json.
def exportar_relatorio():
  nome_file = 'database.json'
  f = open(nome_file, "w")
  f.writelines(str(dados))
  f.close()
  print('\n\n')
  print('****** Registros exportados. Nome do arquivo: ', nome_file, ' ******')
  print('\n\n')

"""# Carregar Dados"""

def carregarDados(nomefile):
  f = open(nomefile, "r")
  arq = f.read()
  f.close()
  dados2 = eval(arq)
  return dados2

"""#Inserir Registro

"""

def inserirRegistro(tipo):
  print(f'*** Cadastro de {tipo} ***')
  if tipo != 'investimento':
    valor = float(input(f'** Informe o valor a ser inserido (somente numeros, ex: 1.5): '))
    data = input('** Informe a data de lançamento (dd/mm/yyyy): ') #date.today()
    dict_novo = {"tipo": tipo, "valor": valor, "data_cadastro": data}
    dados["lancamentos"].append(dict_novo)
  else:
    capital = float(input('** Informe o Capital Inicial do investimento (somente numeros, ex: 1.5): '))
    # solicito a taxa ao mes e divido por 30 porque quero o valor da taxa diariamente
    # irei utilizar esse valor no calculo do rendimento por dia
    taxa = float(input('** Informe a Taxa de juros ao mês do investimento  (somente numero, ex: 1.5): '))
    taxa_diaria = taxa / 30
    data_investimento = input('** Informe a data do investimento (dd/mm/yyyy): ')

    data_cadastro =  datetime.now()
    tempo_investimento = (data_cadastro - datetime.strptime(data_investimento, '%d/%m/%Y') ).days

    if tempo_investimento <= 0:
       tempo_investimento = 1

    montante_atualizado = capital * (1 + taxa_diaria)**tempo_investimento

    dict_novo = {
          "tipo":"investimento", #receita,despesas,investimento
          "valor": capital, #capital
          "data_cadastro": data_cadastro.strftime("%d/%m/%Y"),
          "taxa": taxa,
          "data_investimento": data_investimento,
          "valor_atualizado": round(montante_atualizado,2),
          "data_atualizacao": data_cadastro.strftime("%d/%m/%Y"),
        }
    dados["lancamentos"].append(dict_novo)
  print("***** Registro Inserido com Sucesso! ****** ")
  print("\n\n")
  return True

"""# Listar todos os registros"""

def listar_todos_registros():
  for i in range(len(dados["lancamentos"])):
    print(f'| Indice {i}')
    for chave, valor in (dados["lancamentos"][i].items()):
      print(f'| {chave} -> {valor}')
    print('-------------------------')

  print("\n\n")
  return True

"""#Atualizar um registro"""

#Atualizar registros: No caso de atualização, pode-se atualizar o valor, o tipo e a data deverá ser a de atualização do registro.
def atualizar_registro(index):
  if index < len(dados['lancamentos']):
    flag = 0
    while flag == 0:
      print("Qual dado deseja alterar?")
      if dados['lancamentos'][index]['tipo'] == 'investimento':
        print(" 1 - Tipo")
        print(" 2 - Valor")
        print(" 3 - Data de cadastro")
        print(" 4 - Taxa")
        print(" 5 - Data do Investimento")

        escolha = input(": ")
        if escolha in ['1','2','3','4','5']:
          flag = 1
          if escolha == '1': #atualização do tipo
            valor_alterado = input("Informe o novo tipo: ")
            if valor_alterado in ['receita','despesa']:
              dados['lancamentos'][index]['tipo'] = valor_alterado
              dados['lancamentos'][index].pop('taxa')
              dados['lancamentos'][index].pop('data_investimento')
              dados['lancamentos'][index].pop('valor_atualizado')
              dados['lancamentos'][index].pop('data_atualizacao')

          elif escolha == '2': #atualização do valor
            valor_alterado = float(input("Informe o novo valor: "))
            dados['lancamentos'][index]['valor'] = valor_alterado

          elif escolha == '3': # atualização da data de cadastro
            valor_alterado = input("Informe a nova data de cadastro(dd/mm/yyyy): ")
            dados['lancamentos'][index]['data_cadastro'] = valor_alterado

          elif escolha == '4': # atualização da taxa
            valor_alterado = float(input("Informe a nova Taxa de juros ao mês do investimento  (somente numero, ex: 1.5): "))
            dados['lancamentos'][index]['taxa'] = valor_alterado

          elif escolha == '5': # atualização da data investimento
            valor_alterado = input("Informe a nova data do investimento (dd/mm/yyyy): ")
            dados['lancamentos'][index]['data_investimento'] = valor_alterado

          if escolha in ['2','3','4','5'] :
            dados['lancamentos'][index] = atualiza_rendimento_unico(dados['lancamentos'][index])

        else:
          flag = 0
          print('--------> Opção Invalida! <--------')
          print('\n\n')
          continue

      else:
        print(" 1 - Tipo")
        print(" 2 - Valor")
        print(" 3 - Data")
        escolha = input(": ")
        if escolha in ['1','2','3']:
          flag = 1
          if escolha == '1':
            valor_alterado = input("Informe o novo tipo: ")
            if valor_alterado == 'investimento' and valor_alterado != dados['lancamentos'][index]['tipo']:

              taxa = float(input('** Informe a Taxa de juros do investimento (somente numero, ex: 1.5): '))
              taxa_diaria = taxa / 30
              data_investimento = input('** Informe a data do investimento (dd/MM/yyyy): ')
              #data_cadastro =  date.today()
              data_cadastro = datetime.strptime(dados['lancamento'][index]["data_cadastro"], '%d/%m/%Y')

              #tempo_investimento = data_cadastro - data_investimento
              if (data_cadastro - datetime.strptime(data_investimento, '%d/%m/%Y') ).days <= 0:
                tempo_investimento = 1
              else:
                tempo_investimento = int( (data_cadastro - datetime.strptime(data_investimento, '%d/%m/%Y') ).days / 30 )

              capital = float(dados['lancamentos'][index]["valor"])

              montante_atualizado = capital * (1 + taxa_diaria)**tempo_investimento

              dados['lancamentos'][index]["data_cadastro"] = data_cadastro
              dados['lancamentos'][index]["taxa"] = taxa
              dados['lancamentos'][index]["data_investimento"]= data_investimento
              dados['lancamentos'][index]["valor_atualizado"] = round(montante_atualizado,2)
              dados['lancamentos'][index]["data_atualizacao"] = data_cadastro.strftime("%d/%m/%Y")

            dados['lancamentos'][index]['tipo'] = valor_alterado

          elif escolha == '2':
            valor_alterado = float(input("Informe o novo valor: "))
            dados['lancamentos'][index]['valor'] = valor_alterado
          elif escolha == '3':
            valor_alterado = input("Informe o novo data (dd/mm/yyyy): ")
            dados['lancamentos'][index]['data'] = datetime.strptime(valor_alterado, '%d/%m/%Y')

        else:
          flag = 0
          print('--------> Opção Invalida! <--------')
          print('\n\n')
          continue

  print("---------> Registro atualizado com sucesso! <---------")
  print("\n\n")

"""#Ler Registro / Lista um Registro"""

def ler_registro(filtro, valor_filtro):
  #Ler registros: Deverá ser possível consultar os registros por data, tipo ou valor.
  lista = []
  for i in range(len(dados["lancamentos"])):
    if dados["lancamentos"][i][filtro] == valor_filtro:
      dict_out = {'indice': i}
      for chave, valor in (dados["lancamentos"][i].items()):
        dict_out[chave] = valor
      lista.append(dict_out)
        #print(f'| {chave} -> {valor}')

  for i in lista:
    print('\n--------------------\n')
    for chave, valor in (i.items()):
      print(f'| {chave} -> {valor}')

  print('-------------------------')
  print("\n\n")

#Crie pelo menos uma função de agrupamento, que seja capaz de mostrar o total de valor baseado em alguma informação (mes, tipo...)

#Crie valores separados para identificar a data (dia, mes, ano)

"""#Deletar um registro"""

#Deletar: Deverá ser possível deletar o registro (caso necessário, considere o indice do elemento como ID)
def deletar_registro(index):
  if index < len(dados['lancamentos']):
    dados['lancamentos'].pop(index)
    print("---------> Registro deletado com sucesso! <---------")
  else:
    print("---------> Registro não Encontrado! <---------")
  print("\n\n")

"""#Atualizar Rendimento Unico"""

#função que atualiza um dicionario
def atualiza_rendimento_unico(dict_selecionado : dict):
  if dict_selecionado['tipo'] == 'investimento':
    taxa = float(dict_selecionado["taxa"])
    taxa_diaria = taxa / 30
    data_investimento = datetime.strptime(dict_selecionado["data_investimento"], '%d/%m/%Y')
    data_agora =  datetime.now()
    tempo_investimento = (data_agora - data_investimento ).days
    if tempo_investimento <= 0:
      tempo_investimento = 1

    capital = float(dict_selecionado["valor"])

    montante_atualizado = capital * (1 + taxa_diaria)**tempo_investimento

    dict_selecionado["valor_atualizado"] = round(montante_atualizado, 2)
    dict_selecionado["data_atualizacao"] = data_agora.strftime("%d/%m/%Y")
    return dict_selecionado

"""#Atualizar rendimento de todos os investimentos"""

#Crie uma função atualiza_rendimento que atualize os valores de rendimento sempre que chamada.
def atualiza_rendimento(index=None, out=True):
  #o parametro index é pra ser utilizando quando quero usar essa função pra atualizar apenas um registro
  # Então quando o index é None é porque iremos atualizar todos os registros
  # Quando o index tem um valor ele atualiza um registro
  if index == None:
    for x in dados['lancamentos']:
      if x['tipo'] == 'investimento':
        x = atualiza_rendimento_unico(x)
    print("---------> Registros atualizados com sucesso! <---------")
  else:
    if dados['lancamentos'][index]['tipo'] == 'investimento':
      dados['lancamentos'][index] = atualiza_rendimento_unico(dados['lancamentos'][index])


      if out:
        print("---------> Registro atualizado com sucesso! <---------")
  print("\n\n")











"""#Main"""

opcao  = '1'
while opcao != '0':
  print('|***********************|\n|   Escolha uma opção   |')
  print(' -> 1 - Inserir uma Receita.')
  print(' -> 2 - Inserir uma Despesa.')
  print(' -> 3 - Inserir um Investimento.')
  print(' -> 4 - Atualizar um registro.')
  print(' -> 5 - Deletar um registro.')
  print(' -> 6 - Listar registros por data, tipo ou valor.')
  print(' -> 7 - Listar Todos os registros.')
  print(' -> 8 - Exportar Dados')
  print(' -> 9 - Deseja carregar dados armazenados?')
  print(' -> 0 Finalizar.')
  print('|***********************|')

  opcao = input("Escolha uma opção: ")
  if opcao == '1': #1 - Inserir uma Receita.
    inserirRegistro('receita')

  elif opcao == '2': #2 - Inserir uma Despesa.
    inserirRegistro('despesa')

  elif opcao == '3': #3 - Inserir um Investimento.
    inserirRegistro('investimento')

  elif opcao == '4': #4 - Atualizar um registro.
    print(" -> Informe o indice do registro que deseja atualizar: ")
    listar_todos_registros()
    indice = int(input("Indice: "))
    atualizar_registro(indice)

  elif opcao == '5': #5 - Deletar um registro.
    print(" -> Informe o indice do registro que deseja deletar: ")
    listar_todos_registros()
    indice = int(input("Indice: "))
    deletar_registro(indice)

  elif opcao == '6': #6 - Listar registros por data, tipo ou valor.
    print(' -> Deseja pequisar os registros por: ')
    print(' 1 -  Data')
    print(' 2 -  Tipo')
    print(' 3 -  Valor')
    filtro = input("Escolha um item: ")
    if filtro == '1':
      filtro = 'data_cadastro'
      valor = input("Informe a data que deseja pesquisar (dd/mm/yyyy): ")
    elif filtro == '2':
      filtro = 'tipo'
      valor = input("Informe o tipo do lançamento que deseja pesquisar: ")
    elif filtro == '3':
      filtro = 'valor'
      valor = float(input("Informe o valor que deseja pesquisar: ")  )
    else:
      print('--------> Opção Invalida! <--------')

      continue
    ler_registro(filtro, valor)

  elif opcao == '7': #7 - Listar Todos os registros.
    listar_todos_registros()
  elif opcao == '8': #8 - Exportar Dados
    exportar_relatorio()
  elif opcao == '9': #9 -Deseja carregar dados armazenados?
    dados = carregarDados("database.json")

  elif opcao == '0':
    print('--------> Encerrando.... <--------')
  else:
    print('--------> Opção Invalida! <--------')

dados

atualiza_rendimento(index=None, out=True)

