users = ["admin"]
keys = ["admin"]
def sistema(users,keys):
    new_login = input("**nao*tem*uma*conta?*(s/n)\n-");
    if new_login == "s":
        newuser = input("*nome*do*usuario*\n-");
        users.append(newuser);
        newkey = input("*nova*senha*\n-");
        keys.append(newkey);
        print("\n**conta*criada*com*sucesso**");
        print("insira*suas*credenciais*para*acessar*o*sistema:*");
        logar();
    else:
        logar();
def logar():  
    usuario = input("***insira*o*usuario!**\n-");
    senha = input("****insira*a*senha!***\n-");
    if usuario in users and senha in keys:
        print("*Login*realizado*com*sucesso!*");
    else:
        print("*Login*invalido!*");
        sistema(users,keys)
ligar = input("*Deseja*ligar*o*sistema?*(s/n)\n-");
if ligar =="s":
   
    print("*BEM*VINDO*AO*SISTEMA*");
    print("**********************");
    print("**********************");
    sistema(users,keys);
else:
    print("SISTEMA*DESATIVADO*");
    # end file;