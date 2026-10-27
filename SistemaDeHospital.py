import datetime

pacientes = []
agendamentos = []
consultas_realizadas = []

medicos = [{"id": 1, "nome": "Dr. Gioliano", "especialidade": "Clínico Geral"},
        {"id": 2, "nome": "Dra. Ana", "especialidade": "Psiquiatria"},
        {"id": 3, "nome": "Dra. Maria", "especialidade": "Pediatria"},
        {"id": 4, "nome": "Enfermeira Julia", "especialidade": "Enfermagem"},
        {"id": 5, "nome": "Dr. Pedro", "especialidade": "Cirurgia Geral"},
        {"id": 6, "nome": "Dr. João", "especialidade": "Cardiologia"}]
#lista de médicos pré definidos ja.

def gerar_senha(tipo, numero):
    return f"{tipo}{numero:03d}"
#gerador de senha.

def chamar_medicos():
    print("ESCOLHA O MÉDICO")
    for medico in medicos:
        print(medico["id"], "-", medico["nome"], "-", medico["especialidade"])

    escolha = int(input("Escolha: "))

    for medico in medicos:
        if escolha == medico["id"]:
            print("Médico Disponível:", medico["nome"])
            return medico

    print("Médico Indisponível.")

# função que chama o médico e da as opções na recepção la embaixo
def cadastrar_paciente(tipo, normal, prioritario, emergencia):
    nome = input("Digite seu Nome: ")
    data_nascimento = input("Digite sua Data de Nascimento: ")
    cpf = input("Digite seu CPF: ")
    plano = int(input("Possui Plano de Saúde? 1- Sim | 2- Não: "))
    confirmacao = int(input("Confirmar Cadastro? 1- Sim | 2- Não: "))

    if tipo == 1:
        normal = normal + 1
        senha = gerar_senha("N", normal)
    elif tipo == 2:
        prioritario = prioritario + 1
        senha = gerar_senha("P", prioritario)
    elif tipo == 3:
        emergencia = emergencia + 1
        senha = gerar_senha("E", emergencia)
    else:
        print("Tipo de atendimento inválido.")
        return normal, prioritario, emergencia

    paciente = {"nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "plano": plano,
        "tipo": tipo,
        "senha": senha}
    if confirmacao == 1:
        pacientes.append(paciente)

        print("\nDADOS CADASTRAIS")
        print("NOME:", nome)
        print("DATA DE NASCIMENTO:", data_nascimento)
        print("CPF:", cpf)

        if plano == 1:
            print("PLANO DE SAÚDE: Possui")
        elif plano == 2:
            print("PLANO DE SAÚDE: Não Possui")

        print("SUA SENHA É:", senha)
        print("Paciente Cadastrado com Sucesso!")
    else:
        print("Cadastro cancelado.")

    return normal, prioritario, emergencia

# função que cadastra os clientes na clínica e salva seus dados.
def encontrar_paciente():
    cpf = input("Digite o CPF do paciente: ")

    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            return paciente

    print("Paciente não encontrado.")

# função pra procurar os clientes que ja foram cadastrados. (se não foi cadastrado, não vai achar)
def agendar_consulta():
    print("AGENDAMENTO DE CONSULTA")

    paciente = encontrar_paciente()

    if paciente:
        medico = chamar_medicos()

        if medico:
            dia = int(input("Dia da Consulta: "))
            mes = int(input("Mês da Consulta: "))
            ano = int(input("Ano da Consulta: "))
            hora = int(input("Hora da Consulta: "))
            minuto = int(input("Minuto da Consulta: "))

            data_hora = datetime.datetime(ano, mes, dia, hora, minuto)

            horario_ocupado = 0

            for agendamento in agendamentos:
                if agendamento["medico"]["id"] == medico["id"]:
                    if agendamento["data_hora"] == data_hora:
                        horario_ocupado = 1

            if horario_ocupado == 1:
                print("Esse horário já está ocupado.")
            else:
                agendamento = {"paciente": paciente,
                    "medico": medico,
                    "data_hora": data_hora,
                    "status": "Agendada"}

                agendamentos.append(agendamento)

                print("Consulta agendada com sucesso!")
                print("Paciente:", paciente["nome"])
                print("Médico:", medico["nome"])
                print("Especialidade:", medico["especialidade"])
                print("Data:", data_hora.strftime("%d/%m/%Y"))
                print("Horário:", data_hora.strftime("%H:%M"))

# função pra agendar a consulta usando datatime.
def cancelar_consulta():
    print("CANCELAMENTO DE CONSULTA")

    paciente = encontrar_paciente()

    if paciente:
        encontrou = 0

        for agendamento in agendamentos:
            if agendamento["paciente"]["cpf"] == paciente["cpf"]:
                if agendamento["status"] == "Agendada":
                    print("Médico:", agendamento["medico"]["nome"])
                    print("Data:", agendamento["data_hora"].strftime("%d/%m/%Y"))
                    print("Horário:", agendamento["data_hora"].strftime("%H:%M"))

                    confirmacao = int(input("Cancelar consulta? 1- Sim | 2- Não: "))

                    if confirmacao == 1:
                        agendamento["status"] = "Cancelada"
                        print("Consulta cancelada com sucesso.")

                    encontrou = 1

        if encontrou == 0:
            print("Nenhuma consulta agendada encontrada.")

# função pra cancelar a consulta que ja foi agendada anteriormente. (se não foi agendada antes, não terá nenhuma.)
def remarcar_consulta():
    print("\nREMARCAÇÃO DE CONSULTA")

    paciente = encontrar_paciente()

    if paciente:
        for agendamento in agendamentos:
            if agendamento["paciente"]["cpf"] == paciente["cpf"]:
                if agendamento["status"] == "Agendada":

                    print("Consulta atual:")
                    print("Médico:", agendamento["medico"]["nome"])
                    print("Data:", agendamento["data_hora"].strftime("%d/%m/%Y"))
                    print("Horário:", agendamento["data_hora"].strftime("%H:%M"))

                    dia = int(input("Novo dia: "))
                    mes = int(input("Novo mês: "))
                    ano = int(input("Novo ano: "))
                    hora = int(input("Nova hora: "))
                    minuto = int(input("Novo minuto: "))

                    nova_data = datetime.datetime(ano, mes, dia, hora, minuto)

                    agendamento["data_hora"] = nova_data

                    print("Consulta remarcada com sucesso.")
                    print("Nova data:", nova_data.strftime("%d/%m/%Y"))
                    print("Novo horário:", nova_data.strftime("%H:%M"))

                    return

        print("Consulta não encontrada.")

# função pra remarcar as consultas que ja foram canceladas anteriormente. (se não cancelou nenhuma, não terá nenhuma.)
def realizar_consulta():
    print("CONSULTA PRESENCIAL")

    paciente = encontrar_paciente()

    if paciente:
        for agendamento in agendamentos:
            if agendamento["paciente"]["cpf"] == paciente["cpf"]:
                if agendamento["status"] == "Agendada":

                    sintomas = input("Sintomas do paciente: ")
                    observacoes = input("Observações do médico: ")

                    consulta = {"paciente": paciente,
                        "medico": agendamento["medico"],
                        "data_hora": agendamento["data_hora"],
                        "sintomas": sintomas,
                        "observacoes": observacoes}

                    consultas_realizadas.append(consulta)
                    agendamento["status"] = "Realizada"

                    print("Consulta realizada com sucesso.")
                    return

        print("Nenhuma consulta agendada encontrada.")

# função pra consultar o paciente no mesmo dia, presencialmente. (Opção Mais usada.)
def relatorio():
    print("====== RELATÓRIO ======")

    print("PACIENTES CADASTRADOS:")

    contador = 0

    for paciente in pacientes:
        print(paciente["senha"], "-", paciente["nome"], "-", paciente["cpf"])
        contador = contador + 1

    print("Total de pacientes:", contador)

    print("====== AGENDAMENTOS ======")

    for agendamento in agendamentos:
        print(agendamento["paciente"]["nome"], "-", agendamento["medico"]["nome"], "-", agendamento["data_hora"].strftime("%d/%m/%Y %H:%M"), "-", agendamento["status"])

    contador = 0

    for consulta in consultas_realizadas:
        contador = contador + 1

    print("CONSULTAS REALIZADAS:", contador)

# função pra gerar o relatório dos pacientes Diários. (se não tiver pacientes, não vai ter nenhum relatório.)

def recepcao():
    normal = 0
    prioritario = 0
    emergencia = 0
    opcao = -1

    while opcao != 0:
        print("||====== Clínica Vida+ ======||")
        print("1 - Cadastro")
        print("2 - Agendamento")
        print("3 - Consulta")
        print("4 - Cancelar Consulta")
        print("5 - Remarcar Consulta")
        print("6 - Relatório")
        print("0 - Encerrar Sistema")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("TIPO DE ATENDIMENTO")
            print("1 - Atendimento Normal")
            print("2 - Atendimento Prioritário")
            print("3 - Atendimento Emergencial")

            tipo = int(input("Informe o Tipo de Urgência: "))

            normal, prioritario, emergencia = cadastrar_paciente(tipo, normal, prioritario, emergencia)

        elif opcao == 2:
            agendar_consulta()

        elif opcao == 3:
            realizar_consulta()

        elif opcao == 4:
            cancelar_consulta()

        elif opcao == 5:
            remarcar_consulta()

        elif opcao == 6:
            relatorio()

        elif opcao == 0:
            print("Sistema encerrado.")

        else:
            print("Opção inválida.")
# função de recepção que é a interface que o atendente vai manusear.
recepcao()