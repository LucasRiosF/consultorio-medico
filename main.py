def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Cadastrar paciente")
    print("2. Listar todos os pacientes")
    print("3. Consultar paciente")
    print("4. Alterar dados de um paciente")
    print("5. Cadastrar consulta")
    print("6. Listar consultas")
    print("7. Alterar dados de uma consulta")
    print("8. Sair")

def main():
    pacientes = []
    consultas = []

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
            cpf = input("Digite o CPF do paciente:")
            encontrado = False
            for paciente in pacientes:
                if cpf == paciente['cpf']:
                    encontrado = True
                    data_hora = input("Data e hora da consulta: ")
                    especialidade = input("Especialidade: ")
                    local = input("Local da consulta: ")
                    valor = input("Valor da consulta: ")
                    medico = input("Nome do médico: ")
                    consultas.append({'data_hora': data_hora, 'especialidade': especialidade, 'local': local, 'valor': valor, 'medico': medico, 'cpf': cpf })
                    print("Consulta cadastrada")

            if not encontrado:
                print("Paciente não encontrado")

        elif escolha == '6':
            if not consultas:
                print("Nenhuma consulta cadastrada")
            else:
                print("\n=== Lista de Consultas ===")
                for consulta in consultas:
                    print("Data e hora:", consulta['data_hora'], "Especialidade:", consulta['especialidade'], "Local: ", consulta['local'], "valor:", consulta['valor'], "Médico:", consulta['medico'], "CPF do paciente:", consulta['cpf'])

        elif escolha == '7':
            alterar = input("Digite o CPF do paciente")
            alterar2 = input("Digite a data e hora da consulta")
            encontrado = False
            for consulta in consultas:
                if alterar == consulta['cpf'] and alterar2 == consulta['data_hora']:
                    encontrado = True
                    nova_data = input(f"Data e hora [{consulta['data_hora']}]: ")
                    if nova_data != "":
                        consulta['data_hora'] = nova_data

                    nova_espec = input(f"Especialidade [{consulta['especialidade']}]: ")
                    if nova_espec != "":
                        consulta['especialidade'] = nova_espec

                    novo_local = input(f"Local [{consulta['local']}]: ")
                    if novo_local != "":
                        consulta['local'] = novo_local

                    novo_valor = input(f"Valor [{consulta['valor']}]: ")
                    if novo_valor != "":
                        consulta['valor'] = novo_valor

                    novo_medico = input(f"Médico [{consulta['medico']}]: ")
                    if novo_medico != "":
                        consulta['medico'] = novo_medico   

                    print("Consulta atualizada!")
                    print("Data e hora:", consulta['data_hora'], "- Especialidade:", consulta['especialidade'], "- Local:", consulta['local'], "- Valor:", consulta['valor'], "- Médico:", consulta['medico'],)
            if not encontrado:
                print("Consulta não encontrada")
                
        elif escolha == '8':
            print("Saindo do programa!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
  main()