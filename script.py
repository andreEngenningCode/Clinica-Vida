# Lista global para armazenar os pacientes.
# Cada paciente será um dicionário dentro desta lista.
pacientes = []


def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ")

    
    while True:
        try:
            idade_str = input("Idade: ")
            idade = int(idade_str)
            if idade <= 0:
                print("Por favor, insira uma idade válida (número maior que zero).")
            else:
                break  
        except ValueError:
            print("Erro: A idade deve ser um número inteiro. Tente novamente.")

        
    while True:
        telefone = input("Telefone (ex: (11) 99999-9999): ")

        
        telefone_limpo = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '').replace('+', '')

        if not telefone_limpo.isdigit():
            print("Erro: O telefone deve conter apenas números e caracteres de formatação ( ), -, +.")
        elif len(telefone_limpo) < 10:  
            print("Erro: O telefone parece curto. Insira pelo menos 10 dígitos (incluindo DDD).")
        else:
            break  

    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    
    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")


def ver_estatisticas():
    print("\n--- Estatísticas da Clínica ---")

   
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return

    
    total_pacientes = len(pacientes)
    print(f"Número total de pacientes: {total_pacientes}")

    
    idades = []
    for p in pacientes:
        idades.append(p['idade'])

    
    media_idades = sum(idades) / total_pacientes
    print(f"Idade média dos pacientes: {media_idades:.1f} anos")  

    
    paciente_mais_novo = min(pacientes, key=lambda p: p['idade'])
    paciente_mais_velho = max(pacientes, key=lambda p: p['idade'])

    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")


def buscar_paciente():
    """
    Função para buscar um paciente pelo nome.
    A busca não diferencia maiúsculas/minúsculas.
    """
    print("\n--- Buscar Paciente ---")
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return

    nome_busca = input("Digite o nome (ou parte do nome) do paciente: ").lower()

    encontrados = []
    for p in pacientes:
        if nome_busca in p['nome'].lower():
            encontrados.append(p)

    if not encontrados:
        print(f"Nenhum paciente encontrado com o nome '{nome_busca}'.")
    else:
        print(f"\nPacientes encontrados ({len(encontrados)}):")
        for p in encontrados:
            print(f"  - Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")


def listar_todos_pacientes():
    print("\n--- Lista de Todos os Pacientes ---")

    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return

    print(f"Total de pacientes: {len(pacientes)}\n")
    print("-----------------------------------------")
    for p in pacientes:
        print(f"Nome:     {p['nome']}")
        print(f"Idade:    {p['idade']}")
        print(f"Telefone: {p['telefone']}")
        print("-----------------------------------------")


def main():
    while True:
        print("\n\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            ver_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listar_todos_pacientes()
        elif opcao == '5':
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")



if __name__ == "__main__":
    main()

