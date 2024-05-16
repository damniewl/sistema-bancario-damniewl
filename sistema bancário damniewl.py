# projeto de sistema bancário DIO python
# depósito, saque, extrato
# depósito - somentes valores positivos, depósitos devem ser armazenados em uma variavel e exibidos na op extrato
# saque - limite de 3 saques diarios com limite de 500 reais por saque, caso usario nao tenha saldo, exibir mensagem informando, armazenado em extrato
# extrato - deve listar os depositos e saques e no fim da listagem mostra o saldo atual da conta R$xxxx.xx

menu = """

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falho! O valor do saque excedeu o limite")

        elif excedeu_saques:
            print("Operação falhou! Limite de saques atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falho! O valor informado é inválido.")

    elif opcao == "e":
        print("=======================EXTRATO=======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
