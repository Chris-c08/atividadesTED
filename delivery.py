
produtos = [
    {
        "id": 1,
        "nome": "Hambúrguer",
        "preco": 20.00
    },
    {
        "id": 2,
        "nome": "Pizza",
        "preco": 35.00
    },
    {
        "id": 3,
        "nome": "Batata Frita",
        "preco": 12.00
    },
    {
        "id": 4,
        "nome": "Refrigerante",
        "preco": 7.00
    }
]

pedido = []

def mostrar_produtos():

    print("\n===== CARDÁPIO =====")

    for produto in produtos:

        print(
            produto["id"],
            "-",
            produto["nome"],
            "- R$",
            produto["preco"]
        )


def adicionar_produto():

    mostrar_produtos()

    id_produto = int(
        input("\nDigite o ID do produto: ")
    )

    produto_encontrado = None

    for produto in produtos:

        if produto["id"] == id_produto:

            produto_encontrado = produto

    if produto_encontrado is None:

        print("Produto não encontrado.")
        return

    pedido.append(produto_encontrado)

    print(
        produto_encontrado["nome"],
        "adicionado ao pedido!"
    )


def mostrar_pedido():

    print("\n===== SEU PEDIDO =====")

    if len(pedido) == 0:

        print("Nenhum produto no pedido.")
        return 0

    total = 0

    for produto in pedido:

        print(
            "-",
            produto["nome"],
            "R$",
            produto["preco"]
        )

        total += produto["preco"]

    print("----------------------")
    print("TOTAL: R$", total)

    return total

def realizar_pagamento(total):

    print("\n===== PAGAMENTO =====")

    print("Valor do pedido: R$", total)

    print("1 - Pagamento aprovado")
    print("2 - Falha no pagamento")

    opcao = input("Escolha: ")

    if opcao == "1":

        print("\nPagamento aprovado!")

        return True

    else:

        print("\nFalha no pagamento!")

        return False


def restaurante():

    print("\n===== RESTAURANTE =====")

    print("Pedido recebido!")

    print("1 - Aceitar pedido")
    print("2 - Recusar pedido")

    opcao = input("Escolha: ")

    if opcao == "1":

        print("\nRestaurante aceitou o pedido.")

        return True

    else:

        print("\nRestaurante recusou o pedido.")

        return False


def preparar_pedido():

    print("\n===== PREPARAÇÃO =====")

    print("Restaurante está preparando o pedido...")

    print("Pedido pronto!")

    return True


def realizar_entrega():

    print("\n===== ENTREGA =====")

    print("Entregador foi chamado.")

    print("Entregador está a caminho.")

    tempo = 30

    print(
        "Tempo estimado de entrega:",
        tempo,
        "minutos."
    )

    print("Entregador realizou a entrega!")

    print("Cliente recebeu o pedido.")


def finalizar_pedido():

    if len(pedido) == 0:

        print("\nVocê não possui produtos no pedido.")
        return

    total = mostrar_pedido()

    confirmar = input(
        "\nConfirmar pedido? (s/n): "
    )

    if confirmar.lower() != "s":

        print("Pedido cancelado.")
        return


    pagamento = realizar_pagamento(total)

    if pagamento == False:

        print("\nPedido não enviado ao restaurante.")

        return


    aceito = restaurante()

    if aceito == False:

        print("\nPedido foi recusado pelo restaurante.")

        return


    preparar_pedido()

    realizar_entrega()


while True:

    print("\n")
    print("==============================")
    print("       DELIVERY")
    print("==============================")

    print("1 - Mostrar produtos")
    print("2 - Adicionar produto")
    print("3 - Ver pedido")
    print("4 - Finalizar pedido")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":

        mostrar_produtos()


    elif opcao == "2":

        adicionar_produto()


    elif opcao == "3":

        mostrar_pedido()


    elif opcao == "4":

        finalizar_pedido()


    elif opcao == "5":

        print("\nSistema encerrado.")
        break


    else:

        print("\nOpção inválida.")
