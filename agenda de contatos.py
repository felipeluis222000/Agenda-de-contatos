# Dicionário que ira guardar nossos dados
AGENDA = {}

# Utilizado para a saida do programa ser mais bonita
def Linhas_Formatacao():
    print("------------------------------------------------------------------------------------------")
    return

# Mostra as opçoes de escolha do usuario por meio do print
def Menu():
    print("0-Parar de usar\n1-Buscar contato"
                                 "\n2-Adicionar contato\n3-Apagar contato\n4-Importar contato"
                                 "\n5-Exportar contato\n6-Mostrar contatos\n7-Editar contato\n")

# Utiliza a ideia de "se o contato está na agenda" ele retorna 1 para quando outras
# funções chamarem ela, elas saibam como responder corretamente
def Checar_Contato(contato):
    global AGENDA

    # if usado para checar se o contato está ou não na agenda
    if contato in AGENDA:
        return 1

    else:
        return None

# Chama a função anterior para analizar se o contato existe, caso exista ele ira imprimir na tela
# os dados desse contato
def Mostrar_Contato(contato):

    # A variavel "consulta" irá armazenar a resposta da função "Checar_Contato"
    consulta = Checar_Contato(contato)

    # Apos a variavel "consulta" obter seu valor esse if checa se ela é "1", sendo "1" ele imprime
    # os dados do contato, se não ele imprime que o contato não existe
    if consulta == 1:
        Linhas_Formatacao()
        print("contato: {}".format(contato))
        for dados in AGENDA[contato]:
            print("{}: {}".format(dados, AGENDA[contato][dados]))
    else:
        Linhas_Formatacao()
        print("Contato inexistente!!!")

# A ideia desse metodo é basicamente adicionar ou modificar algo no dicionario "AGENDA"
# ele não faz nada além disso, é auxiliar para as opções de adicionar e de editar algum contato
def Adicionar_Ou_Editar_Contato(contato):
    nome_completo = input("digite o nome completo do contato:\n")
    while True:

        # A ideia desse "try" é limitar o que o usario digita a 11 numeros e apenas a numeros
        try:
            numero = int(input("DDD e numero do contato (apenas numeros)\n"))
            numero = str(numero)
            if len(numero) > 11 or len(numero) < 11:
                print("apenas 11 digitos")
            else:
                break
        except:
            print("apenas 11 digitos")
    # Aqui ele basicamente adiciona as variaveis "nome_completo" e "numero"
    # (a formatacao do numero no dicionario é (99) 99999-9999)
    AGENDA[contato] = {
        "nome completo": nome_completo,
        "numero": "({}{}) {}{}{}{}{}-{}{}{}{}".format(numero[0],numero[1],numero[2],
                                                     numero[3],numero[4],numero[5],numero[6],
                                                     numero[7],numero[8], numero[9],numero[10])
    }

# Como o proprio nome sugere esse metodo apaga algum contato da "AGENDA" e se limita a isso
def Apagar_Contato(contato):
    AGENDA.pop(contato)

# Esse metodo utiliza da ideia de abrir um arquivo .css e salvar os dados na "AGENDA"
def Importar_Contato(arquivo):

    # "try" utilizado para se ocorrer algum erro na hora de abrir o arquivo o
    # programa não crachar
    try:
        with open(arquivo+".css", "r") as importar:

            # A ideia aqui é que como o CSS é dividido por virgulas e em cada linha é um
            # dado de outra pessoa, ele formata esses dados para poder encaixar na "AGENDA"
            for contatos in importar.readlines():

                # .strip() para remover o "\n" e .split(",") para criar uma lista com os
                # dados separados por virgolas
                contatos = contatos.strip().split(",")

                # Adiciona os dados formatados a agenda
                AGENDA[contatos[0]] = {
                        "nome completo": contatos[1],
                        "numero": contatos[2]
                    }
        return 1

    except:
        Linhas_Formatacao()
        print("Erro ao importar arquivos!!!")

# Esse metodo basicamente passa por todos os dados de cada contato na "AGENDA" e escreve formatado para
# css num arquivo .css com nome de arquivo a escolha do usuario
def Exportar_Contato(arquivo):

    # "try" para evitar o programa de crachar se não houver arquivo
    try:
        with open(arquivo+".css", "w") as exportar:

            # "for" simples para gravar as variaveis e depois escrever na formatacao correta do .css
            for contatos in AGENDA:
                nome_completo = AGENDA[contatos]["nome completo"]
                numero = AGENDA[contatos]["numero"]
                exportar.write("{},{},{}\n".format(contatos,nome_completo,numero))
        return 1
    except:
        print("Erro ao exportar contato!!!")

# Esse metodo serve para imprimir na tela todos os contatos com um laço "for"
# simples e com o auxilio do metodo "Mostrar_Contato"
def Mostrar_Contatos():
    global AGENDA

    # "if" utilizado para ver se existe ou não numeros salvos na agenda
    if AGENDA:
        print("Contatos salvos")
        for contato in AGENDA:
            Mostrar_Contato(contato)
    else:
        print("Nenhum contato encontrado!!!")

# Cria um pequeno banco de dados chamado "dbs.css" para salvar os contatos
# e usa o auxilio da funcao "Exportar_Contatos"
def Salvar():
    Exportar_Contato("dbs")

Linhas_Formatacao()

# O metodo foi chamado para carregar os contatos ja salvos no dbs.css
Importar_Contato("dbs")

# Mostra as opcoes de uso para o usuario
Menu()

# Coracao do programa
while True:

    # "while" utilizado para limitar as respostas do usuario apenas ao que o menu pede
    while True:
        Linhas_Formatacao()

        # "try" utilizado para evitar que digitem letras, pois o programa
        # quebraria se usassem letras
        try:
            opcoes = float(input("o que deseja? (digite 8 para mostrar o menu)\n"))
            Linhas_Formatacao()
            break

        except:
            Linhas_Formatacao()
            print("utilizar apenas as opcoes dadas no menu")
            Linhas_Formatacao()
            opcoes = Menu()

    # Basicamente chama o "Mostrar_Contato" com uma variavel digitada
    # pelo usuario
    if opcoes == 1:
        contato = input("Qual contato deseja buscar?\n")
        Mostrar_Contato(contato)

    # Adiciona os contatos, mas antes ele faz uma verificacao se o contato ja existe
    # existindo ele fala que nao da para adicionar
    elif opcoes == 2:
        contato = input("Quem deseja adicionar?\n")
        consulta = Checar_Contato(contato)

        # "if" para checar a resposta do metodo "Checar_Contato", sendo "1"
        # significa que o contato existe e por tanto nao tem por que adicionar
        # e se nao existir ele adiciona normalmente
        if consulta == 1:
            Linhas_Formatacao()
            print("contato já existente!")
            Mostrar_Contato(contato)

        else:
            Adicionar_Ou_Editar_Contato(contato)
            Linhas_Formatacao()
            print("Contato {} adicionado com sucesso!!!!!".format(contato))
            Salvar()

    # Utiliza da mesma logica da "opcoes == 2" mas dessa vez para apagar
    # se o contato existir
    elif opcoes == 3:
        contato = input("Qual contato deseja apagar?\n")
        consulta = Checar_Contato(contato)
        if not consulta:
            Linhas_Formatacao()
            print("Contato inexistente!!!")
        else:
            Apagar_Contato(contato)
            Linhas_Formatacao()
            print("Contato {} apagado com sucesso!!!".format(contato))
            Salvar()
    # Basicamente serve para importar os contatos para a "AGENDA" por meio do metodo
    # "Importar_Contato"
    elif opcoes == 4:
        funcionou = Importar_Contato(input("Qual o nome do arquivo que deseja importar?\n"))

        # "if" utilizado apenas para dar um retorno se o programa importou ou não o contato
        # caso de algum erro o proprio metodo "Importar_Contato" imprime a mensagem de erro
        if funcionou == 1:
            Linhas_Formatacao()
            print("Contatos importados com sucesso!!!")

        else:
            pass

    # Tenta exportar o contato pelo metodo "Exportar_Contato"
    elif opcoes == 5:
        funcionou = Exportar_Contato(input("Digite o camingiho do arquivo:\n"))
        # "if" serve para o mesmo proposito do "if" da "opcao == 4"
        if funcionou == 1:
            Linhas_Formatacao()
            print("Contato exportado com sucesso!!!")

        else:
            pass

    # Apenas mostra os contatos pelo metodo "Mostrar_Contatos"
    elif opcoes == 6:
        Mostrar_Contatos()

    # A ideia é editar algum contato já existente
    # esse bloco basicamente ceca se o contato existe
    # por meio da variavel "consulta" e o metodo "Checar_Contato"
    # e existindo ele edita, se não existir ele imprime que o
    # contato não existe
    elif opcoes == 7:
        contato = input("qual contato deseja editar?\n")
        consulta = Checar_Contato(contato)

        # "if" de consulta
        if not consulta:
            Linhas_Formatacao()
            print("Contato inexistente!!!!")

        else:
            Adicionar_Ou_Editar_Contato(contato)
            Linhas_Formatacao()
            print("Contato {} editado com sucesso!!!".format(contato))
            Salvar()

    # Mostra o menu
    elif opcoes == 8:
        Menu()

    # Ele finaliza o programa mas antes salva
    elif opcoes == 0:
        print("Salvando agenda!!!")
        Salvar()
        Linhas_Formatacao()
        exit()

    # Controla o que o usuario digita limitando as opcoes do menu
    else:
        print("Utilizar apenas as opcoes dadas no menu!!!")
        Linhas_Formatacao()
        opcoes = Menu()