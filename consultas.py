
medicos = [
    {"id": 1, "nome": "Dr. Carlos", "especialidade": "Clínico Geral"},
    {"id": 2, "nome": "Dra. Ana", "especialidade": "Cardiologista"},
    {"id": 3, "nome": "Dr. Pedro", "especialidade": "Dermatologista"}
]

consultas = []

def mostrar_medicos():
    print("\n===== MÉDICOS =====")

    for medico in medicos:
        print(
            medico["id"],
            "-",
            medico["nome"],
            "-",
            medico["especialidade"]
        )


def contar_consultas_paciente(paciente):
    contador = 0

    for consulta in consultas:
        if consulta["paciente"] == paciente:
            contador += 1

    return contador


def horario_disponivel(medico, data, horario):

    for consulta in consultas:

        if (
            consulta["medico"] == medico
            and consulta["data"] == data
            and consulta["horario"] == horario
        ):
            return False

    return True


def sugerir_horarios(medico, data):

    horarios = [
        "08:00",
        "09:00",
        "10:00",
        "14:00",
        "15:00",
        "16:00"
    ]

    print("\nHorários disponíveis:")

    encontrou = False

    for horario in horarios:

        if horario_disponivel(medico, data, horario):
            print("-", horario)
            encontrou = True

    if not encontrou:
        print("Nenhum horário disponível nessa data.")


def agendar_consulta():

    print("\n===== AGENDAR CONSULTA =====")

    paciente = input("Nome do paciente: ")

    if contar_consultas_paciente(paciente) >= 3:
        print("\nERRO: O paciente já possui 3 consultas futuras.")
        return

    mostrar_medicos()

    escolha = int(input("Escolha o médico: "))

    medico_escolhido = None

    for medico in medicos:

        if medico["id"] == escolha:
            medico_escolhido = medico

    if medico_escolhido is None:
        print("Médico não encontrado.")
        return

    data = input("Digite a data (DD/MM/AAAA): ")

    sugerir_horarios(medico_escolhido["nome"], data)

    horario = input("Escolha o horário: ")

    if not horario_disponivel(
        medico_escolhido["nome"],
        data,
        horario
    ):

        print("\nERRO: Esse horário já está ocupado.")

        print("Escolha outro horário:")

        sugerir_horarios(
            medico_escolhido["nome"],
            data
        )

        return

    consulta = {
        "paciente": paciente,
        "medico": medico_escolhido["nome"],
        "especialidade": medico_escolhido["especialidade"],
        "data": data,
        "horario": horario
    }

    consultas.append(consulta)

    print("\n================================")
    print("CONSULTA AGENDADA COM SUCESSO!")
    print("================================")

    print("Paciente:", paciente)
    print("Médico:", medico_escolhido["nome"])
    print("Especialidade:", medico_escolhido["especialidade"])
    print("Data:", data)
    print("Horário:", horario)


def mostrar_consultas():

    print("\n===== CONSULTAS AGENDADAS =====")

    if len(consultas) == 0:
        print("Nenhuma consulta agendada.")
        return

    for i, consulta in enumerate(consultas):

        print("\nConsulta", i + 1)

        print("Paciente:", consulta["paciente"])
        print("Médico:", consulta["medico"])
        print("Especialidade:", consulta["especialidade"])
        print("Data:", consulta["data"])
        print("Horário:", consulta["horario"])


while True:

    print("\n")
    print("==============================")
    print(" SISTEMA DE AGENDAMENTO")
    print("==============================")
    print("1 - Agendar consulta")
    print("2 - Mostrar consultas")
    print("3 - Mostrar médicos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        agendar_consulta()

    elif opcao == "2":

        mostrar_consultas()

    elif opcao == "3":

        mostrar_medicos()

    elif opcao == "4":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida.")
