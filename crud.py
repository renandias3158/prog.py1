import json
import os
from datetime import datetime

DADOS_FILE = 'dados.json'
MSG_USUARIO_NAO_ENCONTRADO = "Usuário não encontrado."
contador = 0
shrek_art = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠫⢻⣿⣿⣿⣿⢟⣩⡍⣙⠛⢛⣿⣿⣿⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⡿⢿⣿
⣿⠤⠄⠄⠙⢿⣿⣿⣿⡿⠿⠛⠛⢛⣧⣿⠇⠄⠂⠄⠄⠄⠘⣿⣿⣿⣿⠁⠄⢻
⣿⣿⣿⣿⣶⣄⣾⣿⢟⣼⠒⢲⡔⣺⣿⣧⠄⠄⣠⠤⢤⡀⠄⠟⠉⣠⣤⣤⣤⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣬⣵⣿⣿⣿⣶⡤⠙⠄⠄⠘⠃⠄⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⢿⣿⣿⠿⠋⠁⠄⠄⠂⠉⠒⢘⣿⣿⣿⣿⣿⣿⣿
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
        with open(DADOS_FILE, 'r') as f:
            try:
                dados = json.load(f)
                return dados
            except:
                print("Erro ao ler dados. Inicializando vazio.")
    return {"Users": [], "Keys": [], "Veiculos": [], "Periodos": []}
#por motivos de simplificação, eu prefiri adicionar e carregar todas as informações em apenas um array, permitindo qeu o codigo ficasse mais simples.
def salvar_dados(dados):
    with open(DADOS_FILE, 'w') as f:
        json.dump(dados, f, indent=4)

def cadastrar(dados):
 global contador
 while contador < 1:
    #melhoria nessa area do cadastro, porque em certos casos estva dando erro.
    user = input("Nome do usuário: ").strip()
    if user == "" or user in dados["Users"]:
        print("Usuário inválido ou já existe.")
        cadastrar(dados)
        return
    senha = input("Senha: ").strip()
    veiculo = input("Veículo: ").strip()
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dados["Users"].append(user)
    dados["Keys"].append(senha)
    dados["veiculos"].append(veiculo)
    dados["Periodos"].append(horario)
    print(f"Usuário {user} cadastrado com sucesso.")
    contador += 1
def alterar(dados):
    user = input("Usuário para alterar: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    #idx, é basicamente é o index que vai ser usado para buscar o os dados no Json, para depois alterar ou pagar a divida.
    nova_senha = input("Nova senha (deixe vazio para manter): ").strip()
    novo_veiculo = input("Novo veículo (deixe vazio para manter): ").strip()
    if nova_senha:
        dados["Keys"][idx] = nova_senha
    if novo_veiculo:
        dados["Veiculos"][idx] = novo_veiculo
    print("Dados atualizados.")

def deletar(dados):
    user = input("Usuário para deletar: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    for chave in ["Users", "Keys", "veiculos", "Periodos"]:
        dados[chave].pop(idx)
        #Aqui ela apaga o usuario com seus respectivos dados no Json.
    print(f"Usuário {user} deletado.")

def exibir(dados):
    user = input("Usuário para exibir: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    print(f"Usuário: {user}")
    print(f"Senha: {dados['Keys'][idx]}")
    print(f"Veículo: {dados['veiculos'][idx]}")
    print(f"Horário de registro: {dados['Periodos'][idx]}")
#esse foi um tanto complicado de fazer só com um array multi-dimensional, mas, depois de um certo esforço e tempo, eu consegui.
def listar(dados):
    if not dados["Users"]:
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for u in dados["Users"]:
        print("-", u)
#esse provavelmente foi a mais fácil de fazer, porque ele só lista os usuarios cadastrados.
def calcular_divida(horario_str):
    fmt = "%Y-%m-%d %H:%M:%S"
    try:
        horario = datetime.strptime(horario_str, fmt)
        agora = datetime.now()
        horas = (agora - horario).total_seconds() / 3600
        valor = 10 * horas
        return max(valor, 0)
    except:
        return 0
#A função de calcular divida foi de fato a mais complicada de fazer, porque tive problemas tanto para armazenar quantopara puxar o valor do Json, mas ainda bem que existe o youtube para isso.
def divida(dados):
    user = input("Usuário para calcular dívida: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    valor = calcular_divida(dados["Periodos"][idx])
    print(f"Dívida do usuário {user}: R$ {valor:.2f}")
#essa função é basicamente a mesma coisa que a de exibir, mas com o valor da divida, e com o valor do horario de registro.
def sistema():
    #essa função foi a amis simples de fazer, porque ela só chama as outras funções e faz o menu.
    print(shrek_art)
    print("Bem-vindo ao sistema do estacionamento do Shrekoso!\n")
    dados = carregar_dados()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Alterar dados do usuário")
        print("3 - Deletar usuário")
        print("4 - Exibir dados do usuário")
        print("5 - Listar usuários")
        print("6 - Calcular dívida")
        print("7 - Sair")

        escolha = input("> ").strip()
        if escolha == "1":
            cadastrar(dados)
        elif escolha == "2":
            alterar(dados)
        elif escolha == "3":
            deletar(dados)
        elif escolha == "4":
            exibir(dados)
        elif escolha == "5":
            listar(dados)
        elif escolha == "6":
            divida(dados)
        elif escolha == "7":
            salvar_dados(dados)
            print("Sistema desligado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema()
