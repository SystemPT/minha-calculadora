from calc import somar, subtrair, multiplicar, dividir

def menu():
    print("=== Minha Calculadora ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "0":
            break
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if escolha == "1":
            print("Resultado:", somar(a, b))
        elif escolha == "2":
            print("Resultado:", subtrair(a, b))
        elif escolha == "3":
            print("Resultado:", multiplicar(a, b))
        elif escolha == "4":
            print("Resultado:", dividir(a, b))
        else:
            print("Opção inválida.")

