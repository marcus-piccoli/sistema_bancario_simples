menu = """
========== Desafio 01 ==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
====================================
==> """

saldo = 0
limite = 500
extrato = []  # Lista para armazenar extrato
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")  # Adiciona à lista "extrato"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nValor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, valor, limite, extrato, numero_saques):
    if valor > saldo:
        print("\nSaldo insuficiente.")
    elif valor > limite:
        print("\nValor acima do limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("\nNúmero máximo de saques atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ -{valor:.2f}")  # Adiciona à lista "extrato"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== Extrato ==========")
    
    if extrato:
        for movimentacao in extrato:
            tipo, valor = movimentacao.split(":")  # Separando nome e valor
            print(f"{tipo.ljust(20)} {valor.rjust(10)}")  # Alinhando texto e valores
    else:
        print("\nNenhuma movimentação registrada.")

    print(f"\nSaldo atual: {'R$':>2} {saldo:>8.2f}")  # Alinhando saldo
    print("=============================")

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("\nInforme o valor a ser depositado: R$ "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "2":
        valor = float(input("\nInforme o valor a ser sacado: R$ "))
        saldo, extrato, numero_saques = sacar(saldo, valor, limite, extrato, numero_saques)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")