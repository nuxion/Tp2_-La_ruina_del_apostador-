import random
import time

i = int(input("Cantidad fichas: "))

valor = float(input("Probabilidad de ganar (0.0 - 1.0 ): "))
while 0 > valor or valor > 1:
    valor = float(input("Tiene que ser un valor entre 0.0 y 1.0: "))

probabilidad = [valor, (1-valor)]
limite = int(input("Limite de jugadas: "))


def casino(i, probabilidad, limite):
    # cuidado con el usuario de variables en las funciones
    # que se utilizan fuera de la funcion:
    # en este caso las tres variables son definidas arriba.
    inicio = time.time()
    ganar = ["ganar", "perder"]
    veces_jugadas = 0

    # en vez de hacer el break en limit se puede sumar
    # la condicion en el while:
    while i > 0 and limite != 0:

        resultado = random.choices(ganar, weights=probabilidad)

        if resultado[0] == ganar[0]:
            i += 1
        else:
            i -= 1

        veces_jugadas += 1

        limite -= 1
        # if limite == 0:
        #    break
    fin = time.time()
    print("\t" + str(fin-inicio) + " seg.")
    return veces_jugadas


sumatoria = 0
promedio = 0
for x in range(20):

    sumatoria += casino(i, probabilidad, limite)
    promedio = sumatoria/20

print("\n El promedio de apuestas final es: ", promedio, "\n")
