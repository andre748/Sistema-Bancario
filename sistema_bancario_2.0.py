import textwrap
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n==== Depósito realizado com sucesso! ===")
    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"""Saque: R$ {valor:.2f}
                        Saldo: {saldo}"""
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    cpf_verificado = verificar_cpf(cpf=cpf)

    if cpf_verificado:
        usuario = filtrar_usuario(cpf, usuarios) 

        if usuario:
            print("\n=== Já existe usuário com esse CPF! ===")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro- cidade/sigla estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
        print("=== Usuário criado com sucesso! ===")
    else:
        main()

def verificar_cpf(cpf):
    cpf_ultimos_digitos = '' 
    cpf_str = ''
    cpf_digito = 0
    cpf_conta = 0
    contagem_regressiva = 10
    contagem_regressiva_2 = 11
    for digito in cpf:
        if len(cpf_str) < 9:
            try:
                cpf_digito = int(digito)
                cpf_str += digito
            except:
                continue
        else:
            try:
                cpf_digito = int(digito)
                cpf_ultimos_digitos += digito
            except:
                continue                
    if (len(cpf_str)+len(cpf_ultimos_digitos)) == 11:
        for algarismo in cpf_str:
            cpf_digito = 0
            cpf_digito = int(algarismo)*contagem_regressiva
            cpf_conta += cpf_digito
            contagem_regressiva += -1
        resto_da_divisão = (cpf_conta*10)%11
        primeiro_digito = resto_da_divisão if resto_da_divisão <= 9 else 0
        cpf_str += str(primeiro_digito)
        cpf_conta = 0
        for segundo_algarismo in cpf_str:
            cpf_conta += int(segundo_algarismo)*contagem_regressiva_2
            contagem_regressiva_2 += -1
        segundo_digito = (cpf_conta * 10)%11
        segundo_digito = segundo_digito if segundo_digito <= 9 else 0
        digitos_finais = str(primeiro_digito)+str(segundo_digito)
        if digitos_finais == cpf_ultimos_digitos:
            print('O CPF que você digitou é valido.')
            return True
        else:
            print('O CPF que você digitou é invalido.')
            return False
    else:
        print('Número de digitos invalidos.')
        return False

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n=== Usuário não encontrado, fluxo de criação de conta encerrado! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}

"""
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        

        else :
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        
main()