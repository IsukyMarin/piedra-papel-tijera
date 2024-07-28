import random

def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    if usuario not in ['pi', 'pa', 'ti']:
        return 'Opción no válida. Inténtalo de nuevo.'
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'

    if ganó_el_jugador(usuario, computadora):
        return '¡Ganaste!'

    return '¡Perdiste!'

def ganó_el_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    return False

def iniciar_juego():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    while True:
        resultado = jugar()
        print(resultado)
        seguir_jugando = input("¿Jugar de nuevo? (sí/no): ").lower()
        if seguir_jugando == 'no':  # Cambio aquí
            print("Gracias por jugar. Presiona cualquier tecla para salir.")
            input()  # Espera a que el usuario presione una tecla antes de cerrar.
            break

if __name__ == "__main__":
    iniciar_juego()
