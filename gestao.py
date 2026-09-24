
disciplinas = [
    {
        "id": 1,
        "nome": "Lógica de Programação",
        "creditos": 4,
        "pre_requisito": None,
        "vagas": 3
    },
    {
        "id": 2,
        "nome": "Programação em Python",
        "creditos": 4,
        "pre_requisito": 1,
        "vagas": 3
    },
    {
        "id": 3,
        "nome": "Banco de Dados",
        "creditos": 4,
        "pre_requisito": 1,
        "vagas": 2
    },
    {
        "id": 4,
        "nome": "Engenharia de Software",
        "creditos": 4,
        "pre_requisito": 2,
        "vagas": 2
    }
]

alunos = [
    {
        "id": 1,
        "nome": "Iasmyn",
        "creditos": 0
    },
    {
        "id": 2,
        "nome": "Maria",
        "creditos": 0
    }
]

professores = [
    {
        "id": 1,
        "nome": "Professor Carlos"
    },
    {
        "id": 2,
        "nome": "Professora Ana"
    }
]

matriculas = []
notas = []
LIMITE_CREDITOS = 12


def mostrar_disciplinas():

    print("\n===== DISCIPLINAS =====")

    for disciplina in disciplinas:

        if disciplina["pre_requisito"] is None:
            requisito = "Nenhum"
        else:

            requisito = procurar_disciplina(
                disciplina["pre_requisito"]
            )["nome"]

        print(
            disciplina["id"],
            "-",
            disciplina["nome"]
        )

        print(
            "   Créditos:",
            disciplina["creditos"]
        )

        print(
            "   Pré-requisito:",
            requisito
        )

        print(
            "   Vagas:",
            disciplina["vagas"]
        )

def procurar_disciplina(id_disciplina):

    for disciplina in disciplinas:

        if disciplina["id"] == id_disciplina:
            return disciplina

    return None


def procurar_aluno(id_aluno):

    for aluno in alunos:

        if aluno["id"] == id_aluno:
            return aluno

    return None

def verificar_prerequisito(aluno_id, disciplina):

    prerequisito = disciplina["pre_requisito"]

    if prerequisito is None:
        return True

    for nota in notas:

        if (
            nota["aluno_id"] == aluno_id
            and nota["disciplina_id"] == prerequisito
            and nota["media"] >= 7
        ):
            return True

    return False


def calcular_creditos(aluno_id):

    total = 0

    for matricula in matriculas:

        if matricula["aluno_id"] == aluno_id:

            disciplina = procurar_disciplina(
                matricula["disciplina_id"]
            )

            total += disciplina["creditos"]

    return total


def ja_matriculado(aluno_id, disciplina_id):

    for matricula in matriculas:

        if (
            matricula["aluno_id"] == aluno_id
            and matricula["disciplina_id"] == disciplina_id
        ):
            return True

    return False

def realizar_matricula():

    print("\n===== REALIZAR MATRÍCULA =====")

    print("\nAlunos:")

    for aluno in alunos:

        print(
            aluno["id"],
            "-",
            aluno["nome"]
        )

    id_aluno = int(
        input("\nDigite o ID do aluno: ")
    )

    aluno = procurar_aluno(id_aluno)

    if aluno is None:

        print("Aluno não encontrado.")
        return

    mostrar_disciplinas()

    id_disciplina = int(
        input("\nDigite o ID da disciplina: ")
    )

    disciplina = procurar_disciplina(id_disciplina)

    if disciplina is None:

        print("Disciplina não encontrada.")
        return


    if ja_matriculado(
        id_aluno,
        id_disciplina
    ):

        print("\nO aluno já está matriculado.")
        return

    if not verificar_prerequisito(
        id_aluno,
        disciplina
    ):

        print("\nMATRÍCULA BLOQUEADA!")
        print(
            "O aluno não atende ao pré-requisito."
        )

        return


    if disciplina["vagas"] <= 0:

        print("\nMATRÍCULA BLOQUEADA!")
        print("A turma está lotada.")

        return



    creditos_atuais = calcular_creditos(
        id_aluno
    )

    novos_creditos = (
        creditos_atuais +
        disciplina["creditos"]
    )

    if novos_creditos > LIMITE_CREDITOS:

        print("\nMATRÍCULA BLOQUEADA!")

        print(
            "Limite de créditos excedido."
        )

        print(
            "Limite:",
            LIMITE_CREDITOS
        )

        return

    matricula = {

        "aluno_id": id_aluno,

        "disciplina_id": id_disciplina
    }

    matriculas.append(matricula)

    disciplina["vagas"] -= 1


    print("\n==============================")
    print("MATRÍCULA CONFIRMADA!")
    print("==============================")

    print("Aluno:", aluno["nome"])

    print("Disciplina:", disciplina["nome"])

    print(
        "Créditos:",
        disciplina["creditos"]
    )

    print(
        "Créditos totais:",
        novos_creditos
    )



def lancar_notas():

    print("\n===== LANÇAR NOTAS =====")

    print("\nAlunos:")

    for aluno in alunos:

        print(
            aluno["id"],
            "-",
            aluno["nome"]
        )

    id_aluno = int(
        input("\nDigite o ID do aluno: ")
    )

    aluno = procurar_aluno(id_aluno)

    if aluno is None:

        print("Aluno não encontrado.")
        return


    print("\nDisciplinas do aluno:")

    encontrou = False

    for matricula in matriculas:

        if matricula["aluno_id"] == id_aluno:

            disciplina = procurar_disciplina(
                matricula["disciplina_id"]
            )

            print(
                disciplina["id"],
                "-",
                disciplina["nome"]
            )

            encontrou = True

    if not encontrou:

        print("Aluno não possui matrículas.")
        return


    id_disciplina = int(
        input("\nDigite o ID da disciplina: ")
    )

    if not ja_matriculado(
        id_aluno,
        id_disciplina
    ):

        print(
            "O aluno não está matriculado nessa disciplina."
        )

        return

    nota1 = float(
        input("Digite a primeira nota: ")
    )

    nota2 = float(
        input("Digite a segunda nota: ")
    )

    media = (nota1 + nota2) / 2

    nota_existente = None

    for nota in notas:

        if (
            nota["aluno_id"] == id_aluno
            and nota["disciplina_id"] == id_disciplina
        ):

            nota_existente = nota


    if nota_existente is not None:

        nota_existente["nota1"] = nota1
        nota_existente["nota2"] = nota2
        nota_existente["media"] = media

    else:

        notas.append({

            "aluno_id": id_aluno,

            "disciplina_id": id_disciplina,

            "nota1": nota1,

            "nota2": nota2,

            "media": media
        })


    print("\nNotas registradas!")

    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Média:", media)


def consultar_notas():

    print("\n===== CONSULTAR NOTAS =====")

    print("\nAlunos:")

    for aluno in alunos:

        print(
            aluno["id"],
            "-",
            aluno["nome"]
        )

    id_aluno = int(
        input("\nDigite o ID do aluno: ")
    )

    aluno = procurar_aluno(id_aluno)

    if aluno is None:

        print("Aluno não encontrado.")
        return


    encontrou = False

    print(
        "\nBoletim de",
        aluno["nome"]
    )

    print("------------------------------")


    for nota in notas:

        if nota["aluno_id"] == id_aluno:

            disciplina = procurar_disciplina(
                nota["disciplina_id"]
            )

            media = nota["media"]

            if media >= 7:

                situacao = "APROVADO"

            elif media >= 4:

                situacao = "RECUPERAÇÃO"

            else:

                situacao = "REPROVADO"


            print(
                "Disciplina:",
                disciplina["nome"]
            )

            print(
                "Nota 1:",
                nota["nota1"]
            )

            print(
                "Nota 2:",
                nota["nota2"]
            )

            print(
                "Média:",
                media
            )

            print(
                "Situação:",
                situacao
            )

            print("------------------------------")

            encontrou = True


    if not encontrou:

        print(
            "O aluno ainda não possui notas registradas."
        )


def consultar_matriculas():

    print("\n===== MATRÍCULAS =====")

    if len(matriculas) == 0:

        print("Nenhuma matrícula realizada.")
        return


    for matricula in matriculas:

        aluno = procurar_aluno(
            matricula["aluno_id"]
        )

        disciplina = procurar_disciplina(
            matricula["disciplina_id"]
        )

        print(
            "\nAluno:",
            aluno["nome"]
        )

        print(
            "Disciplina:",
            disciplina["nome"]
        )

        print(
            "Créditos:",
            disciplina["creditos"]
        )


while True:

    print("\n")
    print("==============================")
    print("    GESTÃO ACADÊMICA")
    print("==============================")

    print("1 - Mostrar disciplinas")
    print("2 - Realizar matrícula")
    print("3 - Consultar matrículas")
    print("4 - Lançar notas")
    print("5 - Consultar notas")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":

        mostrar_disciplinas()


    elif opcao == "2":

        realizar_matricula()


    elif opcao == "3":

        consultar_matriculas()


    elif opcao == "4":

        lancar_notas()


    elif opcao == "5":

        consultar_notas()


    elif opcao == "6":

        print("\nSistema encerrado.")
        break


    else:

        print("\nOpção inválida.")
