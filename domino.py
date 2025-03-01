from random import shuffle

FICHAS = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    (3, 3), (3, 4), (3, 5), (3, 6),
    (4, 4), (4, 5), (4, 6),
    (5, 5), (5, 6),
    (6, 6)
]

CANT_FICHAS = 7
JUGADOR_1, JUGADOR_2 = "Jugador 1", "Jugador 2"

def escoger_fichas():
    shuffle(FICHAS)
    return sorted([FICHAS.pop(0) for _ in range(CANT_FICHAS)])

def robar_ficha(fichas_jugador):
    fichas_jugador.append(FICHAS.pop(0))

def comprobar_colocacion(ficha, campo_juego):
    primera_ficha = campo_juego[0]
    ultima_ficha = campo_juego[-1]
    colocar_izq, colorar_der = False, False

    if ficha[0] == primera_ficha[0] or ficha[1] == primera_ficha[0]:
        colocar_izq = True

    if ficha[0] == ultima_ficha[1] or ficha[1] == ultima_ficha[1]:
        colorar_der = True

    return colorar_der, colocar_izq
        
def imprimir(lista_fichas):
    for ficha in lista_fichas:
        print(*ficha, sep="-", end=" ")

def colocar_ficha(campo_juego, ficha, posicion):
    primera_ficha = campo_juego[0]
    ultima_ficha = campo_juego[-1]

    if posicion == "d":
        if ficha[0] == ultima_ficha[1]:
            campo_juego.append(ficha)
        else:
            campo_juego.append((ficha[1], ficha[0]))
    else:
        if ficha[0] == primera_ficha[0]:
            campo_juego.insert(0, (ficha[1], ficha[0]))
        else:
            campo_juego.insert(0, ficha)

def jugar():
    fichas_jug_1 = escoger_fichas()
    fichas_jug_2 = escoger_fichas()
    cont = 0
    tablero = []

    while len(fichas_jug_1) != 0 and len(fichas_jug_2) != 0:
        turno_actual = JUGADOR_1 if cont % 2 == 0 else JUGADOR_2
        fichas_a_jugar = fichas_jug_1 if turno_actual == JUGADOR_1 else fichas_jug_2

        print(f"\nEs el turno de {turno_actual}")
        print("*" * 28)

        print("\nFichas de tu mazo:")
        imprimir(fichas_a_jugar)
        print()

        ficha_escogida = ""
        
        while ficha_escogida not in fichas_a_jugar:
            ficha_escogida = tuple(int(x) for x in input("\n¿Que fichas deseas usar?: ").split())
            if ficha_escogida not in fichas_a_jugar:
                print("Error, no tienes esa ficha en tu mazo. Escoge de nuevo")
        
        if len(tablero) != 0:
            colocar_derecha, colocar_izquierda = comprobar_colocacion(ficha_escogida, tablero)
            lugar_colocacion = ""
            if colocar_derecha or colocar_izquierda:
                if colocar_izquierda and colocar_derecha:
                    while lugar_colocacion not in ('d','i'):
                        lugar_colocacion = input("¿Dónde deseas colocar?(I / D): ").lower()
                elif colocar_derecha:
                    lugar_colocacion = "d"
                else:
                    lugar_colocacion = "i"

                colocar_ficha(tablero, ficha_escogida, lugar_colocacion)
                fichas_a_jugar.remove(ficha_escogida)
            else:
                print("No puedes colocar ninguna ficha. ",end="")
                if len(FICHAS) > 0:
                    robar_ficha(fichas_a_jugar)
                    print("Robando una ficha...")
                    
                print("Has perdido el turno")
  
        else:
            tablero.append(ficha_escogida)
            fichas_a_jugar.remove(ficha_escogida)

        print("\nFichas jugadas: ")
        imprimir(tablero)
        print()
        cont += 1

    print()
    print(f"Enhorabuena a {JUGADOR_1 if len(fichas_jug_1) == 0 else JUGADOR_2}, ha conseguido colocar todas las fichas!")
if __name__ == '__main__':
    jugar()