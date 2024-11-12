def criar_arvore():
    return None


def criar_no(ID):
    return {"ID": ID, "esquerda": None, "direita": None,"nome": None, "descrição": None ,"preco": None}

def adicionar(raiz, ID, nome, descricao, preco):
    if raiz is None:
        return {"ID": ID, "esquerda": None, "direita": None, "nome": nome, "descrição": descricao, "preco": preco}

    if ID < raiz["ID"]:
        raiz["esquerda"] = adicionar(raiz["esquerda"], ID, nome, descricao, preco)
    elif ID > raiz["ID"]:
        raiz["direita"] = adicionar(raiz["direita"], ID, nome, descricao, preco)

    return raiz


def remover(raiz, ID):
    if raiz is None:
        return raiz

    if ID < raiz["ID"]:
        raiz["esquerda"] = remover(raiz["esquerda"], ID)
    elif ID > raiz["ID"]:
        raiz["direita"] = remover(raiz["direita"], ID)
    else:
        if raiz["esquerda"] is None:
            return raiz["direita"]
        elif raiz["direita"] is None:
            return raiz["esquerda"]

        temp = menor_ID(raiz["direita"])
        raiz["ID"] = temp["ID"]
        raiz["direita"] = remover(raiz["direita"], temp["ID"])

    return raiz


def procurar(raiz, ID):
    if raiz is None or raiz["ID"] == ID:
        return raiz

    if ID < raiz["ID"]:
        return procurar(raiz["esquerda"], ID)
    else:
        return procurar(raiz["direita"], ID)


def menor_ID(raiz):
    atual = raiz
    while atual and atual["esquerda"] is not None:
        atual = atual["esquerda"]
    return atual


def exibir_pre_ordem(raiz):
    if raiz:
        print(raiz["ID"], end=" ")
        exibir_pre_ordem(raiz["esquerda"])
        exibir_pre_ordem(raiz["direita"])


def exibir_em_ordem_simetrica(raiz):
    if raiz:
        exibir_em_ordem_simetrica(raiz["esquerda"])
        print(raiz["ID"], end=" ")
        exibir_em_ordem_simetrica(raiz["direita"])


def exibir_pos_ordem(raiz):
    if raiz:
        exibir_pos_ordem(raiz["esquerda"])
        exibir_pos_ordem(raiz["direita"])
        print(raiz["ID"], end=" ")


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
            ID = int(input("Digite o ID a ser adicionado: "))
            
            nome = str(input("Digite o Nome a ser adicionado: "))
            
            descricao = str(input("Digite a Descricao a ser adicionado: "))
            
            preco = int(input("Digite o Preco a ser adicionado: "))
            raiz = adicionar(raiz, ID, nome, descricao, preco)
            print("ID ", ID, " adicionado")

        elif opcao == "2":
            ID = int(input("Digite o ID a ser removido: "))
            raiz = remover(raiz, ID)
            print("ID ", ID, " remvido")

        elif opcao == "3":
            ID = int(input("Digite o ID do ID a ser buscado: "))
            resultado = procurar(raiz, ID)
            if resultado:
             for chave, ID_atributo in resultado.items():
                if chave not in ["esquerda", "direita"]:
                
                    print(f"{chave}: {ID_atributo}")
            else:
                print("ID ", ID, " Nao encontrado na Arvore")

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
