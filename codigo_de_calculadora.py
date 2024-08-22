

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."



def calculator():
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        
        choice = input("Digite o número da operação (1/2/3/4) ou 'sair' para encerrar: ")

        if choice == 'sair':
            print("Saindo da calculadora. Até logo!")
            break

        
        if choice in ['1', '2', '3', '4']:
            try:
                
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                
                if choice == '1':
                    print(f"O resultado é: {add(num1, num2)}")
                elif choice == '2':
                    print(f"O resultado é: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"O resultado é: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"O resultado é: {divide(num1, num2)}")

            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")

        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    calculator()
