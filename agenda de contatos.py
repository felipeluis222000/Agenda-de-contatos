AGENDA = {}

def Linhas_Formatacao():
    print("------------------------------------------------------------------------------------------")
    return

def Menu():
    print("0-Parar de usar\n1-Buscar contato"
                                 "\n2-Adicionar contato\n3-Apagar contato\n4-Importar contato"
                                 "\n5-Exportar contato\n6-Mostrar contatos\n7-Editar contato\n")

def Checar_Contato(contato):
    global AGENDA
    if contato in AGENDA:
        return 1
    else:
        return None

def Mostrar_Contato(contato):
    consulta = Checar_Contato(contato)
    if consulta == 1:
        Linhas_Formatacao()
        print("contato: {}".format(contato))
        for dados in AGENDA[contato]:
            print("{}: {}".format(dados, AGENDA[contato][dados]))
    else:
        Linhas_Formatacao()
        print("Contato inexistente!!!")

def Adicionar_Ou_Editar_Contato(contato):
    nome_completo = input("digite o nome completo do contato:\n")
    while True:
        try:
            numero = int(input("DDD e numero do contato (apenas numeros)\n"))
            numero = str(numero)
            if len(numero) > 11 or len(numero) < 11:
                print("apenas 11 digitos")
            else:
                break
        except:
            print("apenas 11 digitos")
    AGENDA[contato] = {
        "nome completo": nome_completo,
        "numero": "({}{}) {}{}{}{}{}-{}{}{}{}".format(numero[0],numero[1],numero[2],
                                                     numero[3],numero[4],numero[5],numero[6],
                                                     numero[7],numero[8], numero[9],numero[10])
    }

def Apagar_Contato(contato):
    AGENDA.pop(contato)

def Importar_Contato(arquivo):
    try:
        with open(arquivo+".css", "r") as importar:
            for contatos in importar.readlines():
                contatos = contatos.strip().split(",")
                AGENDA[contatos[0]] = {
                        "nome completo": contatos[1],
                        "numero": contatos[2]
                    }
        return 1
    except:
        Linhas_Formatacao()
        print("Erro ao importar arquivos!!!")

def Exportar_Contato(arquivo):
    try:
        with open(arquivo+".css", "w") as exportar:
            for contatos in AGENDA:
                nome_completo = AGENDA[contatos]["nome completo"]
                numero = AGENDA[contatos]["numero"]
                exportar.write("{},{},{}\n".format(contatos,nome_completo,numero))
        return 1
    except:
        print("Erro ao exportar contato!!!")

def Mostrar_Contatos():
    global AGENDA
    if AGENDA:
        print("Contatos salvos")
        for i in AGENDA:
            Mostrar_Contato(i)
    else:
        print("Nenhum contato encontrado!!!")

def Salvar():
    Exportar_Contato("dbs")

Linhas_Formatacao()
Importar_Contato("dbs")
Menu()
while True:
    while True:
        Linhas_Formatacao()
        try:
            opcoes = float(input("o que deseja? (digite 8 para mostrar o menu)\n"))
            Linhas_Formatacao()
            break
        except:
            Linhas_Formatacao()
            print("utilizar apenas as opcoes dadas no menu")
            Linhas_Formatacao()
            opcoes = Menu()

    if opcoes == 1:
        contato = input("Qual contato deseja buscar?\n")
        Mostrar_Contato(contato)

    elif opcoes == 2:
        contato = input("Quem deseja adicionar?\n")
        consulta = Checar_Contato(contato)
        if consulta == 1:
            Linhas_Formatacao()
            print("contato já existente!")
            Mostrar_Contato(contato)
        else:
            Adicionar_Ou_Editar_Contato(contato)
            Linhas_Formatacao()
            print("Contato {} adicionado com sucesso!!!!!".format(contato))
            Salvar()

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

    elif opcoes == 4:
        funcionou = Importar_Contato(input("Qual o nome do arquivo que deseja importar?\n"))
        if funcionou == 1:
            Linhas_Formatacao()
            print("Contatos importados com sucesso!!!")
        else:
            pass

    elif opcoes == 5:
        funcionou = Exportar_Contato(input("Digite o camingiho do arquivo:\n"))
        if funcionou == 1:
            Linhas_Formatacao()
            print("Contato exportado com sucesso!!!")
        else:
            pass

    elif opcoes == 6:
        Mostrar_Contatos()

    elif opcoes == 7:
        contato = input("qual contato deseja editar?\n")
        consulta = Checar_Contato(contato)
        if not consulta:
            Linhas_Formatacao()
            print("Contato inexistente!!!!")
        else:
            Adicionar_Ou_Editar_Contato(contato)
            Linhas_Formatacao()
            print("Contato {} editado com sucesso!!!".format(contato))
            Salvar()


    elif opcoes == 8:
        Menu()

    elif opcoes == 0:
        print("Salvando agenda!!!")
        Salvar()
        Linhas_Formatacao()
        break

    else:
        print("Utilizar apenas as opcoes dadas no menu!!!")
        Linhas_Formatacao()
        opcoes = Menu()