altura = 4

for fila in range(1, altura + 1):
    espacios = altura - fila
    estrellas = 2 * fila - 1

    linea = " " * espacios + "*" * estrellas
    print(linea)