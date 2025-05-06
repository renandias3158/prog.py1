users = ["admin"]
keys = ["admin"]

def sistema(users, keys):
    while True:
        new_login = input("**insira qual função deseja\n1-cadastrar\n2-alterar dados\n3-deletar dados\n4-exibir dados de um usuario\n5-listar usuarios\n6-desligar sistema\n-")
        
        if new_login == "1":
            cadastrar(users, keys)
        elif new_login == "2":
            alterar_dados(users, keys)
        elif new_login == "3":
            deletar_dados(users, keys)
        elif new_login == "4":
            exibir_dados(users, keys)
        elif new_login == "5":
            listar_usuarios(users)
        elif new_login == "6":
            print("Sistema desligado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar(users, keys):
    newuser = input("*nome*do*usuario*\n-")
    if newuser in users:
        print("Usuário já existe.")
    else:
        newkey = input("*nova*senha*\n-")
        users.append(newuser)
        keys.append(newkey)
        print("\n**conta*criada*com*sucesso**")

def alterar_dados(users, keys):
    usuario = input("Insira o nome do usuário que deseja alterar:\n-")
    if usuario in users:
        index = users.index(usuario)
        newkey = input("Insira a nova senha:\n-")
        keys[index] = newkey
        print("Senha alterada com sucesso.")
    else:
        print("Usuário não encontrado.")

def deletar_dados(users, keys):
    usuario = input("Insira o nome do usuário que deseja deletar:\n-")
    if usuario in users:
        index = users.index(usuario)
        users.pop(index)
        keys.pop(index)
        print("Usuário deletado com sucesso.")
    else:
        print("Usuário não encontrado.")

def exibir_dados(users, keys):
    usuario = input("Insira o nome do usuário que deseja exibir:\n-")
    if usuario in users:
        index = users.index(usuario)
        print(f"Usuário: {users[index]}, Senha: {keys[index]}")
    else:
        print("Usuário não encontrado.")

def listar_usuarios(users):
    print("Lista de usuários:")
    for user in users:
        print(user)

sistema(users, keys)
print('\n')