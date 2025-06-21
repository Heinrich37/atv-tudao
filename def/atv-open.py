def cadastrar_pessoas():
    nomes = []
    idades = []
    sexos = []
    cpfs = []
    enderecos = []
    cidades = []
    estados = []

    while True:
        try:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ").strip().upper()
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            cidade = input("Cidade: ")
            estado = input("Estado (sigla): ").strip().upper()

            nomes.append(nome)
            idades.append(idade)
            sexos.append(sexo)
            cpfs.append(cpf)
            enderecos.append(endereco)
            cidades.append(cidade)
            estados.append(estado)

        except ValueError:
            print("Erro: idade deve ser um número inteiro.")
            continue

        continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    with open("cadastro.txt", "w", encoding="utf-8") as arquivo:
        for i in range(len(nomes)):
            linha = f"Nome: {nomes[i]}, Idade: {idades[i]}, Sexo:{sexos[i]}, CPF: {cpfs[i]}, Endereço: {enderecos[i]}, Cidade: {cidades[i]}, Estado: {estados[i]}"
            arquivo.write(linha + "\n")
            arquivo.write("-" * 100 + "\n")

    print("Dados salvos no arquivo 'cadastro.txt'.")
    return


def consultar_dados():
    try:
        with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            pessoas = [linha for linha in linhas if linha.startswith("Nome")]

            for i, pessoa in enumerate(pessoas, 1):
                print(f"{i} - {pessoa.strip()}")

            numero = int(input("Digite o número da linha que deseja consultar: "))
            if 1 <= numero <= len(pessoas):
                print("Resultado:")
                print(pessoas[numero - 1].strip())
            else:
                print("Número inválido.")
    except FileNotFoundError:
        print("Arquivo de cadastro não encontrado. Cadastre alguém primeiro.")
    except ValueError:
        print("Por favor, digite um número válido.")
    return


def menu():
    while True:
        print("\nMENU")
        print("1 - Cadastrar Pessoas")
        print("2 - Consultar Cadastro")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoas()
        elif opcao == '2':
            consultar_dados()
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
