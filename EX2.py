def calcular_valor_transporte(peso):
    if peso <= 10:
        print(f"Peso: {peso} kg - Valor: R$ 50,00")
    elif peso <= 20:
        print(f"Peso: {peso} kg - Valor: R$ 80,00")
    else:
        print(f"Peso: {peso} kg - Transporte não aceito.")

# Programa principal
try:
    peso_digitado = int(input("Digite o peso da carga (em kg): "))
    calcular_valor_transporte(peso_digitado)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
