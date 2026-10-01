def cadastrar_produto():
    produto = input("Digite o nome do produto: ")
    while True:
        try:
            estoque = int(input("Digite a quantidade inicial: "))
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if estoque < 0:
            print("O estoque não pode ser negativo.")
            continue
        return produto, estoque

produto, estoque = cadastrar_produto()

while True:

    #Menu de opções
    print("\n O que você deseja fazer?")
    print("1. Adicionar produtos")
    print("2. Retirar produtos")
    print("3. Cadastrar novo produto")
    print("4. Sair do programa")

    opcao = input("\n" "Escolha uma opção: ")

    #Se a opção escolhida for 1 para adicionar produtos
    if opcao == "1":

        while True:
            #Utilizando try e except para tratar a entrada de dados, caso o usuário digite algo que não seja um número inteiro.
            try:
                quantidade = int(input("Digite a quantidade que deseja adicionar: "))
            except ValueError:
                print("\n" "Entrada inválida. Por favor, digite um número inteiro.")
                continue

            if quantidade <= 0:
                print("\n" "A quantidade não pode ser negativa ou igual a zero.")
                continue

            #(estoque = estoque + quantidade) é menos utilizada que o de baixo, porém o resultado é o mesmo.
            estoque += quantidade
            print("\n" f"Estoque atualizado de {produto} para: {estoque}")

            break

    #Se a opção escolhida for 2 para retirar produtos
    elif opcao == "2":

        while True:
            #Utilizando try e except para tratar a entrada de dados, caso o usuário digite algo que não seja um número inteiro.
            try:
                print("\n" f"{estoque} unidades disponíveis no estoque.")
                quantidade = int(input("Digite a quantidade que deseja retirar: "))
            except ValueError:
                print("\n" "Entrada inválida. Por favor, digite um número inteiro.")
                continue

            if quantidade <= 0:
                print("\n" "A quantidade não pode ser negativa ou igual a zero.")
                continue

            estoque_atualizado = estoque - quantidade

            break
        
        if estoque_atualizado < 0:
            print("\n" "Estoque insuficiente.")
            print(f"Apenas {estoque} unidades disponíveis no estoque.")

        elif estoque_atualizado == 1:
            print("\n" f"Atualizado para {estoque_atualizado} unidade disponível no estoque.")
            estoque = estoque_atualizado

        elif estoque_atualizado == 0:
            print("\n" f"Atualizado para {estoque_atualizado} unidades disponíveis no estoque.")
            print("ATENÇÃO, O ESTOQUE ZEROU!")
            estoque = estoque_atualizado

        else:
            estoque = estoque_atualizado
            print("\n" f"Estoque atualizado de {produto} para: {estoque}")

    #Se a opção escolhida for 3 para cadastrar um novo produto
    elif opcao == "3":
        produto, estoque = cadastrar_produto()

    elif opcao == "4":
        print("\n" "Saindo do programa...")
        break

    #Se a opção escolhida for diferente de 1, 2 ,3 ou 4 exibe uma mensagem de erro.
    else:
        print("\n" "Opção inválida. Por favor, escolha uma opção válida.")
