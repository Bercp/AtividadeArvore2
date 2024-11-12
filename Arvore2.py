def criar_arvore():
    return None


def criar_no(valor):
    return {"valor": valor, "esquerda": None, "direita": None,"nome": None, "descrição": None ,"preco": None}

def adicionar(raiz, valor, nome, descricao, preco):
    if raiz is None:
        return {"valor": valor, "esquerda": None, "direita": None, "nome": nome, "descrição": descricao, "preco": preco}

    if valor < raiz["valor"]:
        raiz["esquerda"] = adicionar(raiz["esquerda"], valor, nome, descricao, preco)
    elif valor > raiz["valor"]:
        raiz["direita"] = adicionar(raiz["direita"], valor, nome, descricao, preco)

    return raiz


def remover(raiz, valor):
    if raiz is None:
        return raiz

    if valor < raiz["valor"]:
        raiz["esquerda"] = remover(raiz["esquerda"], valor)
    elif valor > raiz["valor"]:
        raiz["direita"] = remover(raiz["direita"], valor)
    else:
        if raiz["esquerda"] is None:
            return raiz["direita"]
        elif raiz["direita"] is None:
            return raiz["esquerda"]

        temp = menor_valor(raiz["direita"])
        raiz["valor"] = temp["valor"]
        raiz["direita"] = remover(raiz["direita"], temp["valor"])

    return raiz


def procurar(raiz, valor):
    if raiz is None or raiz["valor"] == valor:
        return raiz

    if valor < raiz["valor"]:
        return procurar(raiz["esquerda"], valor)
    else:
        return procurar(raiz["direita"], valor)


def menor_valor(raiz):
    atual = raiz
    while atual and atual["esquerda"] is not None:
        atual = atual["esquerda"]
    return atual


def exibir_pre_ordem(raiz):
    if raiz:
        print(raiz["valor"], end=" ")
        exibir_pre_ordem(raiz["esquerda"])
        exibir_pre_ordem(raiz["direita"])


def exibir_em_ordem_simetrica(raiz):
    if raiz:
        exibir_em_ordem_simetrica(raiz["esquerda"])
        print(raiz["valor"], end=" ")
        exibir_em_ordem_simetrica(raiz["direita"])


def exibir_pos_ordem(raiz):
    if raiz:
        exibir_pos_ordem(raiz["esquerda"])
        exibir_pos_ordem(raiz["direita"])
        print(raiz["valor"], end=" ")


def menu():
    raiz = criar_arvore()

    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Buscar Produto")
        print("4. Exibir pré-ordem de IDs")
        print("5. Exibir em ordem simétrica de IDs")
        print("6. Exibir pós-ordem de IDs")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o ID a ser adicionado: "))
            
            nome = str(input("Digite o Nome a ser adicionado: "))
            
            descricao = str(input("Digite a Descricao a ser adicionado: "))
            
            preco = int(input("Digite o valor a ser adicionado: "))
            raiz = adicionar(raiz, valor, nome, descricao, preco)
            print("Valor ", valor, " adicionado")

        elif opcao == "2":
            valor = int(input("Digite o valor a ser removido: "))
            raiz = remover(raiz, valor)
            print("Valor ", valor, " remvido")

        elif opcao == "3":
            valor = int(input("Digite o valor do ID a ser buscado: "))
            resultado = procurar(raiz, valor)
            if resultado:
             for chave, valor_atributo in resultado.items():
                print(f"{chave}: {valor_atributo}")
            else:
                print("Valor ", valor, " Nao encontrado na Arvore")

        elif opcao == "4":
            print("Exibindo pre-ordem:")
            exibir_pre_ordem(raiz)
            print()

        elif opcao == "5":
            print("Exibindo em ordem simetrica:")
            exibir_em_ordem_simetrica(raiz)
            print()

        elif opcao == "6":
            print("Exibindo pós-ordem:")
            exibir_pos_ordem(raiz)
            print()

        elif opcao == "7":
            print("Saindo ...")
            break




        else:
            print("Opção inválida! Digite um numero do menu.")

menu()


