#CONTA DO USUARIO
usuario = {"nome" : ("natan"),"conta" : ("0001"),"senha" : ("1234"), "saldo" : 1000.00}
#DECLARACOES DAS VARIAVEIS
login =""
login_senha=""
depositar = 0.0
saque = 0.0
restante = 0.0
#ACESSO DA CONTA
while login.strip().lower() != usuario["nome"]:
        login =input("nome: ").lower()
        print (login.lower())
for a in range(3):
    login_senha = input("senha: ")
    if login_senha != usuario["senha"]:
        print ("erro")
    else:
        print ("acesso permitido")
        break
else:
    print ("erro maximo de tentativas")
    exit()
# MENU
while True:
    print("""MENU
1. Conta
2. Saque
3. Depositar
4. Sair
""") 
    escolha = input("Digite o número da opção: ")
#FUNCAO DE DANDOS DA CONTA 
    if escolha == "1": 
        print(f"""
        nome: {usuario["nome"]}
        conta: {usuario["conta"]}
        saldo: {usuario["saldo"]:.2f}
""")
        input("aperte Enter para voltar ao menu")
#FUNCAO DE SAQUE
    elif escolha == "2": 
        print (f"""
        saldo disponivel: {usuario['saldo']:.2f}
""")
        entrada = input("quanto deseja sacar: ").replace("," , ".")
        try:
            saque = float(entrada)
            if saque < 0:
                print ("erro! entre com valor maior que zero") 
            elif saque > usuario["saldo"]:
                print ("valor indisponivel")
            else:
                usuario["saldo"] = usuario["saldo"] - saque
                print (f"valor atual {usuario['saldo']:.2f}")
                input("aperte Enter para voltar ao menu")
        except ValueError:
            print ("entrada incorreta. tente novamente") 
#FUNCAO DE DEPOSITAR
    elif escolha == "3": 
        print (f"""
        saldo disponivel: {usuario['saldo']:.2f}
        """)
        entrada = input("quanto deseja depositar?").replace("," , ".")
        try:
            depositar = float(entrada)
            if depositar < 0:
                print ("erro! entre com valor maior que zero")
            else:
                usuario["saldo"] = usuario ["saldo"] + depositar
                print (f"""
saldo atual {usuario['saldo']:.2f}
""")
                input("aperte Enter para voltar ao menu")
        except ValueError:
            print ("entrada incorreta. tente novamente") 
#FUNCAO DE SAIDA
    elif escolha == "4": 
        break
    else: 
        print ("opçao errada , tente novamente")
