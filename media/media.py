def calcular_media(valores):
    return sum(valores) / len(valores)

valores = [float(input(f"Digite o valor {i+1}: ")) for i in range(4)]
print(f"A média dos valores é: {calcular_media(valores)}")