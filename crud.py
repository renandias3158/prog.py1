import json
import os
from datetime import datetime
import time

DADOS_FILE = 'dados.json'
MSG_USUARIO_NAO_ENCONTRADO = "Usuário não encontrado."
contador = 0
shrek_art = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠫⢻⣿⣿⣿⣿⢟⣩⡍⣙⠛⢛⣿⣿⣿⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⡿⢿⣿
⣿⠤⠄⠄⠙⢿⣿⣿⣿⡿⠿⠛⠛⢛⣧⣿⠇⠄⠄⠂⠄⠄⠄⣿⣿⣿⣿⠁⠄⢻
⣿⣿⣿⣿⣶⣄⣾⣿⢟⣼⠒⢲⡔⣺⣿⣧⠄⠄⣠⠤⢤⡀⠄⠟⠉⣠⣤⣤⣤⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣬⣵⣿⣿⣿⣶⡤⠙⠄⠄⠘⠃⠄⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⢿⣿⣿⠿⠋⠁⠄⠄⠄⠄⠄⠄⢘⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⣷⣶⣤⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣷⣦⣰⠄⠄⠄⠄⢾⠿⢿⣿⣿⣿⣿
⣿⡿⠋⣡⣾⣿⣿⣿⡟⠉⠉⠈⠉⠉⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠐⡇⠄⠈⠙⠛⠋
⠋⠄⣾⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⡇⠄⠄⠄⠄⠄
⠄⢸⣿⣿⣿⣿⣿⣯⠄⢠⡀⠄⠄⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄
⠁⢸⣿⣿⣿⣿⣿⣯⣧⣬⣿⣤⣐⣂⣄⣀⣠⡴⠖⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠈⠈⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣽⣉⡉⠉⠈⠁⠄⠁⠄⠄⠄⠄⡂⠄⠄⠄⠄⠄
⠄⠄⠙⣿⣿⠿⣿⣿⣿⣿⣷⡤⠈⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠠⠔⠄⠄⠄⠄⠄
⠄⠄⠄⡈⢿⣷⣿⣿⢿⣿⣿⣷⡦⢤⡀⠄⠄⠄⠄⠄⠄⠄⢐⣠⡿⠁⠄⠄⠄⠄
"""

def carregar_dados():
    if os.path.isfile(DADOS_FILE):
        with open(DADOS_FILE, 'r') as f:
            try:
                dados = json.load(f)
                return dados
            except:
                print("Erro ao ler dados. Inicializando vazio.")
    return {"Users": [], "Keys": [], "veiculos": [], "Periodos": [], "Categorias": []}
#Função que carrega os dados do Json.
def salvar_dados(dados):
    with open(DADOS_FILE, 'w') as f:
        json.dump(dados, f, indent=4)
#Função que salva os dados no Json
def categorizar(dados):
    print("Serviços disponíveis:\n - Econômico: 10.0 reais, sem limpeza \n - Premium: 25.00 reais, com limpeza e lustração!")
    separar = input("Qual serviço você deseja? (insira 1 para Econômico e 2 para Premium):\n- ")
    if separar == "1":
        dados["Categorias"].append("1")  # Armazenar "1" para Econômico
        print("Cadastro realizado com sucesso!")
    elif separar == "2":
        dados["Categorias"].append("2")  # Armazenar "2" para Premium
        print("Cadastro realizado com sucesso!")
    else:
        print("Cadastro inválido")
#Função a parte, que separa os serviços
def cadastrar(dados):
    global contador
    while contador < 1:
        user = input("Nome do usuário: ").strip()
        if user == "" or user in dados["Users"]:
            print("Usuário inválido ou já existe.")
            return
        senha = input("Senha: ").strip()
        veiculo = input("Veículo: ").strip()
        horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dados["Users"].append(user)
        dados["Keys"].append(senha)
        dados["veiculos"].append(veiculo)
        dados["Periodos"].append(horario)
        categorizar(dados)
        contador += 1
#Devido a testes com pessoas externas, notei que seria mais interessante colocar em um loop.
#Já que, quando dava "Usuário inválido" ele voltava pro menu.
def alterar(dados):
    user = input("Usuário para alterar: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    nova_senha = input("Nova senha (deixe vazio para manter): ").strip()
    novo_veiculo = input("Novo veículo (deixe vazio para manter): ").strip()
    if nova_senha:
        dados["Keys"][idx] = nova_senha
    if novo_veiculo:
        dados["veiculos"][idx] = novo_veiculo
    print("Dados atualizados.")
#Infelizmente, eu acabei esquecendo de fazer a parte de alterar o serviço, mas é algo "aceitável", considerando que é perguntado antes.
def pagar_divida(dados):
    user = input("Usuário com dívida a ser paga: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    for chave in ["Users", "Keys", "veiculos", "Periodos", "Categorias"]:
        dados[chave].pop(idx)
    print("Pagando....")
    time.sleep(3)  
    print(f"Dívida do {user} paga.")
#Basicamente, é uma função de deletar o usuário, considerando que, apartir do momento em que a sua divída foi paga, o cliente sairia do estabelecimento.
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
    if dados['Categorias'][idx] == "1":
        print("Serviço escolhido: Econômico")
    elif dados['Categorias'][idx] == "2":
        print("Serviço escolhido: Premium")
#Função básica de exibir os dados.
#No caso dessa função, para facilitar a minha vida, eu acabei por armazenar os serviços em "1" ou "2".
#Porque, desse jeito ficaria mais fácil de fazer as interações, tanto nessa quanto em outras funções.
def listar(dados):
    if not dados["Users"]:
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for u in dados["Users"]:
        print("-", u)
#Possivelmente, a função mais fácil de fazer, já que ela só exibe os usuários em um laço for.
def calcular_divida(horario_str, categoria):
    fmt = "%Y-%m-%d %H:%M:%S"
    try:
        horario = datetime.strptime(horario_str, fmt)
        agora = datetime.now()
        horas = (agora - horario).total_seconds() / 3600
        if categoria == "1":  # Econômico
            valor_hora = 10.0
        elif categoria == "2":  # Premium
            valor_hora = 25.0
        else:
            valor_hora = 10.0  # Padrão: econômico
        valor = valor_hora * horas
        return max(valor, 0)
    except:
        return 0
#Possivelmente a que deu mais erro, considerando que eu nunca mexi com valores temporais.
#Mas, basicamente, é uma função que calcula a divída, baseada numa subtração do tempo atual pelo tempo aramazenado.
#E o resultado é multiplicado pela taxa do respectivo serviço(Econômico ou Premium).
def divida(dados):
    user = input("Usuário para calcular dívida: ").strip()
    if user not in dados["Users"]:
        print(MSG_USUARIO_NAO_ENCONTRADO)
        return
    idx = dados["Users"].index(user)
    categoria = dados["Categorias"][idx]
    valor = calcular_divida(dados["Periodos"][idx], categoria)
    print(f"Dívida do usuário {user}: R$ {valor:.2f}")
#Exibe a divída do respectivo usuário inserido.
def sistema():
    print(shrek_art)
    print("Bem-vindo ao sistema do estacionamento do Shrekoso!\n")
    dados = carregar_dados()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Alterar dados do usuário")
        print("3 - Pagar dívida do usuário")
        print("4 - Exibir dados do usuário")
        print("5 - Listar usuários")
        print("6 - Calcular dívida")
        print("7 - Sair")

        escolha = input("> ").strip()
        if escolha == "1":
            global contador
            contador = 0
            cadastrar(dados)
        elif escolha == "2":
            alterar(dados)
        elif escolha == "3":
            pagar_divida(dados)
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
#Função "Menu"
if __name__ == "__main__":
    sistema()
