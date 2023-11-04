
nombre = input("Ingrese el nombre del estudiante: ")
notas = []
for i in range(4):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)


notas = [float(nota) for nota in notas]
promedio = sum(notas) / len(notas)


with open("notas.txt", "a") as archivo:
    archivo.write(f"Nombre del estudiante: {nombre}\n")
    archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
    archivo.write(f"Promedio: {promedio}\n\n")

    print("Datos guardados en el archivo 'notas.txt'.")


