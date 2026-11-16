total = 0

while True:
    numero = int(input("Escribe un entero (0 para terminar): "))

    if numero == 0:
        break

    total += numero

print("La suma es", total)