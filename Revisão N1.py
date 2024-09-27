import json

# Inicializando uma lista de livros
livros = []

# Função para mostrar o menu
def mostrar_menu():
    print("\n1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Realizar Empréstimo")
    print("4. Realizar Devolução")
    print("5. Relatórios")
    print("6. Sair")

# Função principal
def main():
    while True:
        mostrar_menu()
        opcao = input("Informe a opção: ")

        if opcao == '1':
            cadastrar_livro()
        if opcao == '2':
            consultar_livro()
        if opcao == '3':
            realizar_emprestimo()
        if opcao == '4':
            realizar_devolucao()
        if opcao == '5':
            gerar_relatorios()
        if opcao == '6':
            salvar_livros()
            print("Saindo...")
            break

# Função para salvar os livros em um arquivo
def salvar_livros():
    with open('livros.json', 'w') as f:
        json.dump(livros, f)

# Função para carregar os livros do arquivo
def carregar_livros():
    global livros
    try:
        with open('livros.json', 'r') as f:
            livros = json.load(f)
    except FileNotFoundError:
        livros = []

# Função para cadastrar livros
def cadastrar_livro():
    codigo = input("Informe o código único do livro: ")
    titulo = input("Informe o título do livro: ")
    autor = input("Informe o autor do livro: ")
    isbn = input("Informe o ISBN do livro: ")
    editora = input("Informe a editora do livro: ")
    status = "disponível"

    livro = {
        'codigo': codigo,
        'titulo': titulo,
        'autor': autor,
        'isbn': isbn,
        'editora': editora,
        'status': status
    }

    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    consulta = input("Informe o título, autor ou ISBN para consulta: ")
    
    for livro in livros:
        if consulta in (livro['titulo'], livro['autor'], livro['isbn']):
            print(f"\nTítulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Editora: {livro['editora']}")
            print(f"Status: {livro['status']}")
            return
    print("Livro não encontrado.")

# Função para realizar empréstimo
def realizar_emprestimo():
    codigo = input("Informe o código do livro para empréstimo: ")
    
    for livro in livros:
        if livro['codigo'] == codigo:
            if livro['status'] == "disponível":
                usuario = input("Informe o nome do usuário que está realizando o empréstimo: ")
                livro['status'] = "emprestado"
                livro['usuario'] = usuario
                print(f"Empréstimo realizado para o livro '{livro['titulo']}'.")
                return
            print("O livro já está emprestado.")
            return
    print("Livro não encontrado.")

# Função para realizar devolução
def realizar_devolucao():
    codigo = input("Informe o código do livro para devolução: ")
    
    for livro in livros:
        if livro['codigo'] == codigo:
            if livro['status'] == "emprestado":
                usuario = input("Informe o nome do usuário que está devolvendo o livro: ")
                if livro['usuario'] == usuario:
                    livro['status'] = "disponível"
                    livro.pop('usuario', None)
                    print(f"Devolução realizada para o livro '{livro['titulo']}'.")
                    return
                print("Este livro não foi emprestado para esse usuário.")
                return
            print("O livro já está disponível.")
            return
    print("Livro não encontrado.")

# Função para gerar relatórios
def gerar_relatorios():
    print("\n1. Listar todos os livros")
    print("2. Listar livros disponíveis")
    print("3. Listar livros emprestados")
    opcao = input("Escolha uma opção de relatório: ")

    if opcao == '1':
        print("\nTodos os livros:")
        for livro in livros:
            print(f"{livro['titulo']} ({livro['status']})")
        return
    
    if opcao == '2':
        print("\nLivros disponíveis:")
        for livro in livros:
            if livro['status'] == "disponível":
                print(livro['titulo'])
        return
    
    if opcao == '3':
        print("\nLivros emprestados:")
        for livro in livros:
            if livro['status'] == "emprestado":
                print(f"{livro['titulo']} (Emprestado para {livro['usuario']})")
        return

# Carregando os livros ao iniciar o programa
carregar_livros()

if __name__ == "__main__":
    main()
