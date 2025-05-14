import json
import os

DADOS_FILE = 'dados.json'
none_usuario = "Usuário não encontrado."

# ASCII art do Shrek para exibir na entrada do sistema
shrek_art = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠫⢻⣿⣿⣿⣿⢟⣩⡍⣙⠛⢛⣿⣿⣿⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⡿⢿⣿
⣿⠤⠄⠄⠙⢿⣿⣿⣿⡿⠿⠛⠛⢛⣧⣿⠇⠄⠂⠄⠄⠄⠘⣿⣿⣿⣿⠁⠄⢻
⣿⣿⣿⣿⣶⣄⣾⣿⢟⣼⠒⢲⡔⣺⣿⣧⠄⠄⣠⠤⢤⡀⠄⠟⠉⣠⣤⣤⣤⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣬⣵⣿⣿⣿⣶⡤⠙⠄⠘⠃⠄⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⢿⣿⣿⠿⠋⠁⠄⠂⠉⠒⢘⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⣷⣶⣤⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣷⣦⣰⠄⠄⠄⠄⢾⠿⢿⣿⣿⣿⣿
⣿⡿⠋⣡⣾⣿⣿⣿⡟⠉⠉⠈⠉⠉⠉⠉⠉⠉⠄⠄⠄⠑⠄⠄⠐⡇⠄⠈⠙⠛⠋
⠋⠄⣾⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⡇⠄⠄⠄⠄⠄
⠄⢸⣿⣿⣿⣿⣿⣯⠄⢠⡀⠄⠄⠄⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄
⠁⢸⣿⣿⣿⣿⣿⣯⣧⣬⣿⣤⣐⣂⣄⣀⣠⡴⠖⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠈⠈⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣽⣉⡉⠉⠈⠁⠄⠁⠄⠄⠄⠄⡂⠄⠄⠄⠄⠄
⠄⠄⠙⣿⣿⠿⣿⣿⣿⣿⣷⡤⠈⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠠⠔⠄⠄⠄⠄⠄
⠄⠄⠄⡈⢿⣷⣿⣿⢿⣿⣿⣷⡦⢤⡀⠄⠄⠄⠄⠄⠄⢐⣠⡿⠁⠄⠄⠄⠄⠄
"""

def carregar_dados():
    if os.path.isfile(DADOS_FILE):
        try:
            with open(DADOS_FILE, 'r') as f:
                dados = json.load(f)
                users = dados.get("Users", [])
                keys = dados.get("Keys", [])
                return users, keys
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de dados. Inicializando base vazia.")
            return [], []
    else:
        # Se o arquivo não existir, inicializa com alguns dados padrão
        return ["admin", "joao", "radolfo"], ["admin", "bananilcom", "lepstopirose"]

def salvar_dados(users, keys):
    with open(DADOS_FILE, 'w') as f:
        json.dump({"Users": users, "Keys": keys}, f, indent=4)

def sistema():
    print(shrek_art)
    print("Bem-vindo ao sherekoso sistem!\n")
    users, keys = carregar_dados()
    while True:
        print("\nEscolha a função desejada (insira o numero correspondente):")
        print("1 - Cadastrar usuário")
        print("2 - Alterar senha")
        print("3 - Deletar usuário")
        print("4 - Exibir dados de um usuário")
        print("5 - Listar usuários")
        print("6 - Desligar sistema")
        escolha = input("- ")

        if escolha == "1":
            cadastrar(users, keys)
            salvar_dados(users, keys)
        elif escolha == "2":
            alterar_dados(users, keys)
            salvar_dados(users, keys)
        elif escolha == "3":
            deletar_dados(users, keys)
            salvar_dados(users, keys)
        elif escolha == "4":
            exibir_dados(users, keys)
        elif escolha == "5":
            listar_usuarios(users)
        elif escolha == "6":
            print("Sistema desligado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar(users, keys):
    newuser = input("Nome do usuário para cadastro: ").strip()
    if not newuser:
        print("Nome de usuário inválido.")
        return
    if newuser in users:
        print("Usuário já existe.")
    else:
        newkey = input("Digite a nova senha: ").strip()
        if not newkey:
            print("Senha inválida.")
            return
        users.append(newuser)
        keys.append(newkey)
        print(f"Conta '{newuser}' criada com sucesso!")

def alterar_dados(users, keys):
    usuario = input("Nome do usuário que deseja alterar a senha: ").strip()
    if usuario in users:
        index = users.index(usuario)
        newkey = input("Digite a nova senha: ").strip()
        if not newkey:
            print("Senha inválida.")
            return
        keys[index] = newkey
        print(f"Senha do usuário '{usuario}' alterada com sucesso.")
    else:
        print(none_usuario)

def deletar_dados(users, keys):
    usuario = input("Nome do usuário que deseja deletar: ").strip()
    if usuario in users:
        index = users.index(usuario)
        users.pop(index)
        keys.pop(index)
        print(f"Usuário '{usuario}' deletado com sucesso.")
    else:
        print(none_usuario)

def exibir_dados(users, keys):
    usuario = input("Nome do usuário que deseja exibir: ").strip()
    if usuario in users:
        index = users.index(usuario)
        print(f"Usuário: {usuario}")
        print(f"Senha: {keys[index]}")
    else:
        print(none_usuario)

def listar_usuarios(users):
    print("Lista de usuários cadastrados:")
    for user in users:
        print("-", user)

if __name__ == "__main__":
    sistema()

