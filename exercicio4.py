def cadastrar_livro(livros):
    # Função para permitir que o usuário cadastre um novo livro
    print("\n--- CADASTRAR LIVRO ---")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")

    # Vamos gerar um ID único para o novo livro (poderia ser mais sofisticado em um sistema real)
    novo_id = len(livros) + 1
    novo_livro = {'id': novo_id, 'nome': nome, 'autor': autor, 'editora': editora}
    livros.append(novo_livro)
    print(f"\nLivro '{nome}' cadastrado com sucesso com o ID: {novo_id}")

def consultar_livro_por_id(livros):
    # Esta função busca um livro na nossa lista pelo seu ID único.
    print("\n--- CONSULTA POR ID ---")
    try:
        id_consulta = int(input("Digite o id do livro: "))
        encontrado = False # Uma flag para saber se encontramos o livro
        for livro in livros:
            if livro['id'] == id_consulta:
                # Achamos o livro! Vamos imprimir os detalhes.
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                encontrado = True # Marcamos que encontramos o livro
                break # Não precisamos continuar procurando
        if not encontrado:
            # Se a flag 'encontrado' continua False, o livro não existe.
            print("Livro não encontrado.")
    except ValueError:
        # Se o usuário digitar algo que não é um número, tratamos o erro aqui.
        print("Por favor, digite um número inteiro para o ID.")

def consultar_livros_por_autor(livros):
    # Aqui, vamos encontrar todos os livros de um determinado autor.
    print("\n--- CONSULTA POR AUTOR ---")
    autor_consulta = input("Digite o autor(es) do livro(s): ").upper() # Pegamos o nome do autor e convertemos para maiúsculo para facilitar a comparação.
    encontrados = False # Outra flag para verificar se algum livro foi encontrado.
    for livro in livros:
        if livro['autor'].upper() == autor_consulta:
            # Se o nome do autor do livro (em maiúsculo) corresponde ao que o usuário digitou...
            print(f"\nid: {livro['id']}")
            print(f"nome: {livro['nome']}")
            print(f"autor: {livro['autor']}")
            print(f"editora: {livro['editora']}")
            encontrados = True # Marcamos que encontramos pelo menos um livro.
    if not encontrados:
        # Se a flag continua False, nenhum livro daquele autor foi encontrado.
        print("Nenhum livro encontrado para este autor.")

def consultar_todos_os_livros(livros):
    # Esta função é simples: mostra todos os livros que temos na lista.
    print("\n--- TODOS OS LIVROS CADASTRADOS ---")
    if not livros:
        # Se a lista de livros estiver vazia...
        print("Nenhum livro cadastrado.")
        return # Saímos da função, pois não há nada para mostrar.
    for livro in livros:
        # Para cada livro na nossa lista, vamos imprimir seus detalhes.
        print(f"\nid: {livro['id']}")
        print(f"nome: {livro['nome']}")
        print(f"autor: {livro['autor']}")
        print(f"editora: {livro['editora']}")

def remover_livro(livros):
    # Função para remover um livro da lista (ainda não implementada completamente).
    print("\n--- REMOVER LIVRO ---")
    try:
        id_remover = int(input("Digite o ID do livro que deseja remover: "))
        encontrado = False
        for i, livro in enumerate(livros):
            if livro['id'] == id_remover:
                del livros[i]
                print(f"Livro com ID {id_remover} removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print(f"Não foi encontrado nenhum livro com o ID {id_remover}.")
    except ValueError:
        print("Por favor, digite um número inteiro para o ID.")

def menu_consultar_livro(livros):
    # Este é o submenu que aparece quando o usuário escolhe "Consultar Livro(s)" no menu principal.
    while True:
        print("\n--------- MENU CONSULTAR LIVRO ---------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar")

        opcao = input(">>")

        if opcao == '1':
            consultar_todos_os_livros(livros)
        elif opcao == '2':
            consultar_livro_por_id(livros)
        elif opcao == '3':
            consultar_livros_por_autor(livros)
        elif opcao == '4':
            break # Se a opção for 4, saímos deste menu e voltamos para o principal.
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal(livros):
    # A função principal que roda o menu do nosso sistema.
    while True:
        print("\n--------- MENU PRINCIPAL ---------")
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Livro")
        print("2 - Consultar Livro(s)")
        print("3 - Remover Livro")
        print("4 - Sair")

        opcao = input(">>")

        if opcao == '1':
            cadastrar_livro(livros) # Agora passamos a lista de livros para a função de cadastro.
        elif opcao == '2':
            menu_consultar_livro(livros) # Chama o submenu de consulta.
        elif opcao == '3':
            remover_livro(livros) # Também precisamos passar a lista para a função de remoção.
        elif opcao == '4':
            print("Saindo do sistema.")
            break # Se a opção for 4, saímos do loop principal e o programa termina.
        else:
            print("Opção inválida. Tente novamente.")

# Nossa lista inicial de livros cadastrados. Em um sistema real, isso viria de um banco de dados ou arquivo.
livros_cadastrados = [
    {'id': 1, 'nome': 'Jogos Vorazes', 'autor': 'Suzanne Collins', 'editora': 'Rocco'},
    {'id': 2, 'nome': 'Crepúsculo', 'autor': 'Stephenie Meyer', 'editora': 'Intrínseca'},
    {'id': 3, 'nome': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'editora': 'Martins Fontes'}
]

if __name__ == "__main__":
    # Esta parte garante que a função menu_principal() só seja chamada quando o script é executado diretamente.
    menu_principal(livros_cadastrados)