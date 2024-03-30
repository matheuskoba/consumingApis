import requests

# Airtable
base_id = 'appvVrMPro9b2wo5S'
table_name = 'Tasks'
token_airtable = 'patIkwqUxPFyP03oQ.e28446a815d9e63b58958aca4ffa1bc65e3c82b32004857a1b19a3f27445b86f'
headers_airtable = {"Content-Type": "application/json", "Authorization": f"Bearer {token_airtable}"}
base_url_airtable = f'https://api.airtable.com/v0/{base_id}/{table_name}'

# Calendly
user_id = 'https://api.calendly.com/users/2211a9d3-98ea-4a82-bbc0-e67d3be6b598'
base_url_calendly = 'https://api.calendly.com'
token_calendly = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzExODM1NzI3LCJqdGkiOiIxMjYwODkzNS1mOGVjLTRjOTctOTZiNS0yN2JhODcwMWQ1NzMiLCJ1c2VyX3V1aWQiOiIyMjExYTlkMy05OGVhLTRhODItYmJjMC1lNjdkM2JlNmI1OTgifQ.LWSnTxHZixlzMn7qQHin6mrxI-BKIZY5umMq8IvV8_MZcTTyLyQehQeq7fy7T1dlrQ7ZfMZWfOBIfDbzR5CiYQ'
headers_calendly = {"Content-Type": "application/json", "Authorization": f"Bearer {token_calendly}"}


# Função para listar todos os registros
def list_records():
    url = base_url_airtable
    response = requests.get(url, headers=headers_airtable)
    return response.json()

# Função para obter um registro específico
def get_record(record_id):
    url = f'{base_url_airtable}/{record_id}'
    response = requests.get(url, headers=headers_airtable)
    return response.json()

# Função para atualizar um registro
def update_record(record_id, data):
    url = f'{base_url_airtable}/{record_id}'
    response = requests.put(url, headers=headers_airtable, json=data)
    return response.json()

# Função para criar um novo registro
def create_record(data):
    url = base_url_airtable
    response = requests.post(url, headers=headers_airtable, json=data)
    return response.json()

# Função para excluir um registro
def delete_record(record_id):
    url = f'{base_url_airtable}/{record_id}'
    response = requests.delete(url, headers=headers_airtable)
    return response.json()


# Funções do calendly
# Identificar usuário autenticado
def my_user():
    url = f'{base_url_calendly}/users/me'
    response = requests.get(url, headers=headers_calendly)
    return response.json()

# Verificar agendamentos marcados
def user_busy_time(data):
    url = f'{base_url_calendly}/user_busy_times'
    response = requests.get(url, headers=headers_calendly, json=data)
    return response.json()

# Verificar horários disponíveis na agenda
def list_user_availability_schedules(data):
    url = f'{base_url_calendly}/user_availability_schedules'
    response = requests.get(url, headers=headers_calendly, json=data)
    return response.json()

# Exemplos de uso das funções
if __name__ == '__main__':

    # Escolha a api que deseja consultar
    print("Escolha qual api deseja esecutar:")
    print("1. Airtable")
    print("2. Calendly")
    result = input("Digite o número da opção desejada: ")

    match result:
        case '1':
            # Escolha a função que deseja executar
            print("Escolha a função que deseja executar:")
            print("1. Listar registros")
            print("2. Obter um registro específico")
            print("3. Atualizar um registro")
            print("4. Criar um novo registro")
            print("5. Excluir um registro")
            choice = input("Digite o número da opção desejada: ")

            match choice:
                case '1':
                    print("Listando registros:")
                    print(list_records())
                case '2':
                    record_id = input("Digite o ID do registro que deseja obter: ")
                    print(f"\nObtendo o registro com ID {record_id}:")
                    print(get_record(record_id))
                case '3':
                    record_id = input("Digite o ID do registro que deseja atualizar: ")
                    name = input("Digite o novo nome: ")
                    deadline = input("Digite a nova data no formato (yyyy-mm-dd): ")
                    priority = input("Escolha um nível de prioridade (Low, Medium, High): ")
                    status = input("Escolha um status (In progress, To do, Done): ")

                    data = {
                        "fields": {
                            "Name": name,
                            "Deadline": deadline,
                            "Priority": priority,
                            "Status": status
                        }
                    }
                    print(f"\nAtualizando o registro com ID {record_id}:")
                    print(update_record(record_id, data))
                case '4':
                    name = input("Digite o novo nome: ")
                    deadline = input("Digite a nova data no formato (yyyy-mm-dd): ")
                    priority = input("Escolha um nível de prioridade (Low, Medium, High): ")
                    status = input("Escolha um status (In progress, To do, Done): ")

                    data = {
                        "fields": {
                            "Name": name,
                            "Deadline": deadline,
                            "Priority": priority,
                            "Status": status
                        }
                    }
                    print("\nCriando um novo registro:")
                    print(create_record(data))
                case '5':
                    record_id = input("Digite o ID do registro que deseja excluir: ")
                    print(f"\nExcluindo o registro com ID {record_id}:")
                    print(delete_record(record_id))
                case _:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        case '2':
            print("Escolha a função que deseja executar:")
            print("1. Meu usuário")
            print("2. Horários Agendados")
            print("3. Horários disponíveis na agenda")

            choice = input("Digite o número da opção desejada: ")

            match choice:
                case "1":
                    print(my_user())
                case "2":
                    user = input("Informe o ID do usuário: ")
                    startTime = "2024-04-16T20:30:00.000000Z"
                    endTime = "2024-04-17T20:30:00.000000Z"
                    data = {
                        "user": user,
                        "start_time": startTime,
                        "end_time": endTime
                    }
                    print(user_busy_time(data))
                case "3":
                    user = input("Informe o ID do usário: ")
                    data = {
                        "user": user
                    }
                    print(f"\nCarregando as datas disponíveis: ")
                    print(list_user_availability_schedules(data))
                case _:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
