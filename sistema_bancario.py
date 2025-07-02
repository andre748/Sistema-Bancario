menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[f] Finalizar
=> """

titulo = "EXTRATO"
saldo, limite, extrato, numero_saques = 0, 500, '', 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} || SALDO: R$ {saldo}\n"
        else:
            print("Valor digitado inválido.")
    
    elif opcao == 's':
        valor = float(input("Informe o valor a ser sacado: "))
        if valor > saldo:
            print("Você não tem saldo suficiente.")
        elif valor > limite:
            print("O valor do saque excedeu o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido.")
        elif valor <= 0:
            print("O valor informado é invalido.")
        else:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f} || SALDO: R$ {saldo}\n"
            numero_saques += 1
            

    elif opcao == 'e':
        print(titulo.center(41, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(41*'=')
    elif opcao == 'f':
        break

    else:
        print("Operação inválida, por favor tente de novo.")