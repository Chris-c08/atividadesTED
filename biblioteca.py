from datetime import date, timedelta

livros = [
    {
        "id": 1,
        "titulo": "Introdução à Programação",
        "autor": "Carlos Silva",
        "disponivel": True
    },
    {
        "id": 2,
        "titulo": "Estruturas de Dados",
        "autor": "Ana Souza",
        "disponivel": True
    },
    {
        "id": 3,
        "titulo": "Banco de Dados",
        "autor": "Pedro Santos",
        "disponivel": True
    },
    {
        "id": 4,
        "titulo": "Engenharia de Software",
        "autor": "Maria Oliveira",
        "disponivel": True
    },
    {
        "id": 5,
        "titulo": "Redes de Computadores",
        "autor": "João Costa",
        "disponivel": True
    },
    {
        "id": 6,
        "titulo": "Python para Iniciantes",
        "autor": "Lucas Lima",
        "disponivel": True
    }
]

alunos = [
    {
        "id": 1,
        "nome": "Iasmyn",
        "multa": 0
    },
    {
        "id": 2,
        "nome": "Maria",
        "multa": 0
    }
]

emprestimos = []

def mostrar_livros():

    print("\n===== LIVROS =====")

    for livro in livros:

        if livro["disponivel"]:
            situacao = "Disponível"
        else:
            situacao = "Emprestado"

        print(
            livro["id"],
            "-",
            livro["titulo"],
            "-",
            livro["autor"],
            "-",
            situacao
        )


def mostrar_alunos():

    print("\n===== ALUNOS =====")

    for aluno in alunos:

        print(
            aluno["id"],
            "-",
            aluno["nome"],
            "- Multa: R$",
            aluno["multa"]
        )


def procurar_aluno(id_aluno):

    for aluno in alunos:

        if aluno["id"] == id_aluno:
            return aluno

    return None


def procurar_livro(id_livro):

    for livro in livros:

        if livro["id"] == id_livro:
            return livro

    return None


def contar_livros_aluno(id_aluno):

    contador = 0

    for emprestimo in emprestimos:

        if emprestimo["aluno_id"] == id_aluno:
            contador += 1

    return contador



def realizar_emprestimo():

    print("\n===== REALIZAR EMPRÉSTIMO =====")

    mostrar_alunos()

    id_aluno = int(input("\nDigite o ID do aluno: "))

    aluno = procurar_aluno(id_aluno)

    if aluno is None:

        print("Aluno não encontrado.")
        return


    if aluno["multa"] > 0:

        print("\nEMPRÉSTIMO BLOQUEADO!")
        print("O aluno possui uma multa de R$",
              aluno["multa"])

        return


    

    quantidade = contar_livros_aluno(id_aluno)

    if quantidade >= 5:

        print("\nEMPRÉSTIMO BLOQUEADO!")

        print(
            "O aluno já possui o limite máximo de 5 livros."
        )

        return


   
    mostrar_livros()

    id_livro = int(input("\nDigite o ID do livro: "))

    livro = procurar_livro(id_livro)

    if livro is None:

        print("Livro não encontrado.")
        return


    if not livro["disponivel"]:

        print("\nLivro indisponível.")
        print("Escolha outro livro.")

        return


    data_emprestimo = date.today()

    data_devolucao = data_emprestimo + timedelta(days=7)


    emprestimo = {

        "aluno_id": id_aluno,

        "livro_id": id_livro,

        "data_emprestimo": data_emprestimo,

        "data_devolucao": data_devolucao
    }

    emprestimos.append(emprestimo)


    livro["disponivel"] = False

    print("\n==============================")
    print("EMPRÉSTIMO REALIZADO!")
    print("==============================")

    print("Aluno:", aluno["nome"])

    print("Livro:", livro["titulo"])

    print(
        "Data do empréstimo:",
        data_emprestimo.strftime("%d/%m/%Y")
    )

    print(
        "Data de devolução:",
        data_devolucao.strftime("%d/%m/%Y")
    )


def mostrar_emprestimos():

    print("\n===== EMPRÉSTIMOS =====")

    if len(emprestimos) == 0:

        print("Nenhum empréstimo realizado.")
        return


    for emprestimo in emprestimos:

        aluno = procurar_aluno(
            emprestimo["aluno_id"]
        )

        livro = procurar_livro(
            emprestimo["livro_id"]
        )

        print("\n----------------------")

        print("Aluno:", aluno["nome"])

        print("Livro:", livro["titulo"])

        print(
            "Empréstimo:",
            emprestimo["data_emprestimo"].strftime(
                "%d/%m/%Y"
            )
        )

        print(
            "Devolução:",
            emprestimo["data_devolucao"].strftime(
                "%d/%m/%Y"
            )
        )



def devolver_livro():

    print("\n===== DEVOLVER LIVRO =====")

    if len(emprestimos) == 0:

        print("Não existem empréstimos.")
        return


    mostrar_emprestimos()

    id_aluno = int(
        input("\nDigite o ID do aluno: ")
    )

    id_livro = int(
        input("Digite o ID do livro: ")
    )


    emprestimo_encontrado = None

    for emprestimo in emprestimos:

        if (
            emprestimo["aluno_id"] == id_aluno
            and emprestimo["livro_id"] == id_livro
        ):

            emprestimo_encontrado = emprestimo
            break


    if emprestimo_encontrado is None:

        print("Empréstimo não encontrado.")
        return


    hoje = date.today()

    data_devolucao = emprestimo_encontrado[
        "data_devolucao"
    ]

    atraso = (hoje - data_devolucao).days


    aluno = procurar_aluno(id_aluno)

    livro = procurar_livro(id_livro)


    if atraso > 0:

        multa = atraso * 1

        aluno["multa"] += multa

        print("\nLivro devolvido com atraso.")

        print("Dias de atraso:", atraso)

        print("Multa: R$", multa)

    else:

        print("\nLivro devolvido dentro do prazo.")

  
    livro["disponivel"] = True

    emprestimos.remove(emprestimo_encontrado)


while True:

    print("\n")
    print("==============================")
    print("       BIBLIOTECA")
    print("==============================")

    print("1 - Mostrar livros")
    print("2 - Mostrar alunos")
    print("3 - Realizar empréstimo")
    print("4 - Mostrar empréstimos")
    print("5 - Devolver livro")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":

        mostrar_livros()


    elif opcao == "2":

        mostrar_alunos()


    elif opcao == "3":

        realizar_emprestimo()


    elif opcao == "4":

        mostrar_emprestimos()


    elif opcao == "5":

        devolver_livro()


    elif opcao == "6":

        print("\nSistema encerrado.")
        break


    else:

        print("\nOpção inválida.")
