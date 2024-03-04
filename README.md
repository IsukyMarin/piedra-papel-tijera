import random

def juego_adivina_numero():
    print("¡Bienvenido al juego Adivina el Número!")

    # Elige un número aleatorio del 1 al 10
    numero_para_adivinar = random.randint(1, 10)

    # Adivina el número de la consola
    mi_numero = int(input("Intenta adivinar el número de la consola (1 al 10): "))
    print(f"La consola eligió el número {numero_para_adivinar}.")

    # Tu turno para adivinar
    numero_para_adivinar_tu = random.randint(1, 10)
    print(f"La consola eligió un número para ti. ¡Adivina el número!")

    intentos = 0
    while True:
        tu_adivinanza = int(input("Tu adivinanza (1 al 10): "))
        intentos += 1

        if tu_adivinanza == numero_para_adivinar_tu:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
        else:
            print("Incorrecto. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
    juego_adivina_numero()
