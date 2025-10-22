def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Cadastrar paciente")
    print("2. Listar todos os pacientes")
    print("3. Sair")

def main():
    pacientes = []

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do paciente: ")
            idade = input("Idade do paciente: ")
            pacientes.append({'nome': nome, 'idade': idade})
            print("Paciente cadastrado")
        elif escolha == '2':
            if not pacientes:
                print("Nenhum paciente cadastrado.")
            else:
                print("\n=== Lista de Pacientes ===")
                for paciente in pacientes:
                    print("Nome:", paciente['nome'], "- Idade:", paciente['idade'])
        elif escolha == '3':
            print("Saindo do programa!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
  main()