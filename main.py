import random
import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

#Tabelas
cursor.execute("""CREATE TABLE IF NOT EXISTS login (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               cpf TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL,
               saldo REAL NOT NULL)""")
conexao.commit()

#variaveis
nome = str("User")
cpf = str()
dinheiro = float(0)
senha = str()

def atualizar_saldo():
    global dinheiro
    global cpf
    cursor.execute("UPDATE login SET saldo = ? WHERE cpf = ? ", (dinheiro,cpf))
    conexao.commit()

def roleta():
    global dinheiro
    global nome

    print(f"Bem vindo {nome}, a roleta da sorte.")
    while True:
        print("""Gostaria de:
1 - Jogar
2 - Verificar regras
3 - Voltar""")
        ask = str(input(f"{nome}: "))
        if ask == "1":
            while True:
                print("Quanto gostaria de apostar? (apenas números)")
                ask2 = float(input(f"{nome}: "))
                print(f"R$ {ask2}")
                if ask2 > dinheiro or ask2 < 2:
                    print("Valor invalido, quantidade minima é de 2 reais")
                else:
                    print("Girar? s/n")
                    giro = str(input(f"{nome}: ").lower())
                    if giro == "s":
                        dinheiro -= ask2 + 1
                        atualizar_saldo()
                        re1 = random.randint(1,3)
                        re2 = random.randint(1,3)
                        re3 = random.randint(1,3)


                        print("____________________")
                        print(f"|  {re1}  |  {re2}  |  {re3}  |")
                        print("____________________")

                        if re1 % 2 == 0 and re2 % 2 == 0 and re3 % 2 == 0:
                            print("Você ganhou!")
                            dinheiro += ask2 * 4
                            atualizar_saldo()
                            print("Jogar novamente? s/n")
                            ask3 = str(input(f"{nome}: ").lower())
                            if ask3 == "n":
                                menu()
                                break
                        else:
                            print("Você perdeu")
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            print("Jogar novamente? s/n")
                            ask3 = str(input(f"{nome}: ").lower())
                            if ask3 == "n":
                                menu()
                                break

                    elif giro == "n":
                        menu()
                        break
                    
        elif ask == "2":
            print("""As regras são bem simples, para jogar é necessario pagar uma
taxa de 1 real e gire a roleta, caso caia 3 números pares o valor apostado será quintuplicado""")
        elif ask == "3":
            menu()
            break
        else:
            print("Resposta invalida, digitar novamente")

def mine():
    global dinheiro
    global nome

    print(f"Bem vindo {nome}, ao Mines.")
    while True:
        print("""Gostaria de:
1 - Jogar
2 - Verificar regras
3 - Voltar""")
        ask = str(input(f"{nome}: "))
        if ask == "1":
            while True:
                a = "▊"
                print("Quanto gostaria de apostar? (apenas números)")
                ask2 = float(input(f"{nome}: "))
                print(f"R$ {ask2}")
                if ask2 > dinheiro or ask2 < 2:
                    print("Valor invalido, quantidade minima é de 2 reais")
                else:
                        print(f"""1{a} 2{a} 3{a} 4{a} 5{a}
6{a} 7{a} 8{a} 9{a} 10{a}
11{a} 12{a} 13{a} 14{a} 15{a}""")
                        diamante = random.randint(1,15)
                        print("Escolha o quadrante que você acha que esta o diamante")
                        palpite = int(input(f"{nome}: "))
                        dinheiro -= ask2 + 1
                        atualizar_saldo()
                        if diamante == palpite:
                            print("Você ganhou!")
                            dinheiro += ask2 * 10
                            atualizar_saldo()
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            print("Jogar novamente? s/n")
                            ask3 = str(input(f"{nome}: ").lower())
                            if ask3 == "n":
                                menu()
                                break
                        else:
                            print("Você perdeu!")
                            print("Jogar novamente? s/n")
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            ask3 = str(input(f"{nome}: ").lower())
                            if ask3 == "n":
                                menu()
                                break
                    
        elif ask == "2":
            print("""As regras são bem simples, para jogar é necessario pagar uma
taxa de 1 real e escolher em qual quadrante está o diamante, quase todos os quadrantes
possuem bombas, acerte o quadrante correto e multiplique o valor apostado por dez""")
        elif ask == "3":
            menu()
            break
        else:
            print("Resposta invalida, digitar novamente")

def cara():
    global dinheiro
    global nome
    print(f"Bem vindo {nome}, ao Cara ou Coroa.")
    while True:
        print("""Gostaria de:
1 - Jogar
2 - Verificar regras
3 - Voltar""")
        ask = str(input(f"{nome}: "))
        if ask == "1":
            while True:
                print("Quanto gostaria de apostar? (apenas números)")
                ask2 = float(input(f"{nome}: "))
                print(f"R$ {ask2}")
                if ask2 > dinheiro or ask2 < 2:
                    print("Valor invalido, quantidade minima é de 2 reais")
                else:
                    print("gostaria de apostar em qual?")
                    print("""1 - Cara
2 - Coroa""")
                    ask3 = str(input(f"{nome}: ").lower())
                    if ask3 == "1":
                        dinheiro -= ask2 + 1
                        atualizar_saldo()
                        jogo = random.randint(1,10)
                        if jogo <= 6:
                            print("Coroa")
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            print("Você perdeu, jogar novamente? s/n")
                            ask4 = str(input(f"{nome}: ").lower())
                            if dinheiro >= 2:
                                if ask4 == "n":
                                    menu()
                                    break
                            else:
                                menu()
                                break
                        else:
                            print("Cara")
                            dinheiro += ask2 * 2
                            atualizar_saldo()
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            print("Você ganhou, jogar novamente? s/n")
                            ask4 = str(input(f"{nome}: ").lower())
                            if dinheiro >= 2:
                                if ask4 == "n":
                                    menu()
                                    break
                            else:
                                menu()
                                break
                    elif ask3 == "2":
                        dinheiro -= ask2 + 1
                        atualizar_saldo()
                        jogo = random.randint(1,10)
                        if jogo <= 6:
                            print("Cara")
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            print("Você perdeu, jogar novamente? s/n")
                            ask4 = str(input(f"{nome}: ").lower())
                            if dinheiro >= 2:
                                if ask4 == "n":
                                    menu()
                                    break
                            else:
                                menu()
                                break
                        else:
                            print("Coroa")
                            dinheiro += ask2 * 2
                            atualizar_saldo()
                            print(f"Seu saldo atual é de: R$ {dinheiro}")
                            print("Você ganhou, jogar novamente? s/n")
                            ask4 = str(input(f"{nome}: ").lower())
                            if dinheiro >= 2:
                                if ask4 == "n":
                                    menu()
                                    break
                            else:
                                menu()
                                break
                    else:
                        print("Resposta invalida")
        elif ask == "2":
            print("""As regras são bem simples, para jogar é necessario pagar uma
    taxa de 1 real e apostar a quantia desejada, e escolher o lado que você quer que ganhe, 
    caso você acerte o valor apostado dobra""")
        elif ask == "3":
            menu()
            break
        else:
            print("Resposta invalida, digitar novamente")
        
def jogar():
    global dinheiro
    global nome

    print("Qual jogo gostaria de jogar?")
    print("""1 - Cara ou Coroa
2 - Roleta da fortuna
3 - Mines
4 - Voltar""")
    while True:
        ask = str(input(f"{nome}: "))
        if ask == "1":
            cara()
            break
        elif ask == "2":
            roleta()
            break
        elif ask == "3":
            mine()
            break
        elif ask == "4":
            menu()
            break
        else:
            print("Resposta invalida, digitar novamente")

def saldo():
    global dinheiro
    global nome

    while True:
        print("Gostaria de verificar o saldo ou fazer uma recarga?")
        print("""1 - Recarregar
2 - Consultar saldo
3 - voltar""")
        ask = str(input(f"{nome}: "))
        if ask == "1":
            print("Quanto gostaria de recarregar? (Apenas os números)")
            saldo = int(input(f"{nome}: "))
            dinheiro += saldo
            print(f"Você Regarregou R$ {saldo} reais")
            atualizar_saldo()
        elif ask == "2":
            cursor.execute("SELECT saldo FROM login WHERE cpf = ?", (cpf,))
            saldom = cursor.fetchone()
            for sald in saldom:
                sald = float(sald)
            print(f"Seu saldo é R$ {sald}")
        elif ask == "3":
            menu()
            break
        else:
            print("Resposta invalida, digitar novamente")    
    
def menu():
    global dinheiro
    global nome

    print("O que gostaria de fazer?")
    print("""1 - Jogar
2 - Saldo""")
    while True:
        ask = str(input(f"{nome}: "))
        if ask == "2":
            saldo()
            break
        elif ask == "1":
            jogar()
            break
        else:
            print("Resposta invalida, digitar novamente")

def inicio():
    global dinheiro
    global nome
    global senha
    global cpf

    print("Bem vindo ao cassino Interminal")
    print("para jogar é necesario realizar o cadastro")
    print("já possui um cadastro conosco? s/n")
    ask = str(input(f"{nome}: ").lower())
    infinito = True
    if ask == "s":
        while True:
            print("Nos informe seu CPF:")
            cpf = input(f"{nome}: ")
            print("Nos informe seu senha:")
            senha = input(f"{nome}: ")

            cursor.execute("""SELECT nome,saldo FROM login WHERE cpf = ? AND senha = ?""", (cpf,senha))
            ux = cursor.fetchall()
            if ux == []:
                print("Usúario não encontrado")
            else:
                for ux_nome,saldo in ux:
                    nome = ux_nome
                    dinheiro = saldo
                    menu()
                    break

    else:
        while infinito == True:
            print("Nos informe seu nome:")
            nome = input(f"{nome}: ")
            print("Nos informe seu CPF:")
            cpf = input(f"{nome}: ")
            print("Nos informe uma senha:")
            senha = input(f"{nome}: ")
            print(f"""\n
Nome: {nome}                  
CPF: {cpf}
Senha: {senha}
os dados estão corretos? s/n\n""")
            ask2 = input(f"{nome}: ")
            if ask2 == "S".lower():
                dinheiro = 0
                cursor.execute("""INSERT INTO login (nome, cpf, saldo, senha) VALUES(?,?,?,?)""",(nome,cpf,dinheiro,senha))
                conexao.commit()
                infinito = False
                menu()
                return

inicio()
conexao.close()
