def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Cadastrar paciente")
    print("2. Listar todos os pacientes")
    print("3. Consultar paciente")
    print("4. Alterar dados de um paciente")
    print("5. Sair")

def main():
    pacientes = []

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do paciente: ")
            idade = input("Idade do paciente: ")
            cpf = input("CPF do paciente: ")
            endereco = input("Endereço do paciente: ")
            pacientes.append({'nome': nome, 'idade': idade, 'cpf': cpf, 'endereco': endereco})
            print("Paciente cadastrado")
        elif escolha == '2':
            if not pacientes:
                print("Nenhum paciente cadastrado.")
            else:
                print("\n=== Lista de Pacientes ===")
                for paciente in pacientes:
                    print("Nome:", paciente['nome'], "- Idade:", paciente['idade'])

        elif escolha == '3':
            busca = input("Digite o CPF ou nome do paciente: ")
            encontrado = False
            for paciente in pacientes:
                if busca == paciente['cpf'] or busca == paciente['nome']: 
                    encontrado = True
                    print("Nome:", paciente['nome'], "- Idade:", paciente['idade'], "-CPF:", paciente['cpf'])

            if not encontrado:
                print("Paciente não encontrado")

        elif escolha == '4':
            alterar = input("Digite o CPF do paciente:")
            encontrado = False
            for paciente in pacientes:
                if alterar == paciente['cpf']:
                    encontrado = True
                    novo_nome = input(f"Nome [{paciente['nome']}]: ")
                    if novo_nome != "":
                        paciente['nome'] = novo_nome

                    nova_idade = input(f"Idade [{paciente['idade']}]: ")
                    if nova_idade != "":
                        paciente['idade'] = nova_idade

                    novo_endereco = input(f"Endereço [{paciente['endereco']}]: ")
                    if novo_endereco != "":
                        paciente['endereco'] = novo_endereco

                    novo_cpf = input(f"CPF [{paciente['cpf']}]: ")
                    if novo_cpf != "":
                        paciente['cpf'] = novo_cpf   

                    print("Paciente atualizado!")
                    print("Nome:", paciente['nome'], "- Idade:", paciente['idade'], "-CPF:", paciente['cpf'])
        
            if not encontrado:
                print("Paciente não encontrado")
                
            
        elif escolha == '5':
            print("Saindo do programa!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
  main()