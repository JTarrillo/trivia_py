import random
import time
import os
from data import data
from tri_ascii import trivia_ascii
from colors import colors

colors_list = list(
    colors.keys()
)  # lista de colores usando el diccinario colors de colors.py
random_color = random.choice(colors_list)  # color aleatorio para el primer mensaje

print(
    f"{colors[random_color]} {trivia_ascii}{colors['RESET']}"
)  # imprimir el mensaje de trivia_ascii usando el color aleatorio
print(f"{colors['BLUE']}Bienvenido a la trivia sobre computación {colors['RESET']}")
print("Pondremos a prueba tus conocimientos")
nombre = input("Ingresa tu nombre: ")

print("-" * 10)

print(
    "\nHola,",
    nombre,
    ", responde las siguientes preguntas escribiendo la letra de la alternativa correcta y presiona 'Enter' para confirmar y enviar la respuesta:",
)
input("Presiona Enter para continuar...")

en_trivia = True  # para mantener el loop
intentos = 0  # cuenta el numero de intentos por parte del usuario

while en_trivia:
    intentos += 1
    puntaje = 0
    counter = 0  # cuenta las preguntas que se van imprimiendo

    print(f"\nEste es tu intento número {intentos}: ")
    # input("Presiona Enter para continuar...")
    time.sleep(2)
    counter += 1
    os.system("cls")  # permite limpiar la pantalla

    # crea una lista de las keys del diccionario data,
    # esta lista sera aleatoria para que la trivia tenga
    # un orden de aparicion aleatorio de las preguntas
    random_list_data = sorted(data)

    # iteracion entre las keys de data
    for key in random.sample(random_list_data, len(random_list_data)):
        # obtenemos los values de data donde estan la pregunta, alternativas y la alternativa correcta
        pregunta = data[key]["pregunta"]
        alternativas = data[key]["alternativas"]
        correcta = data[key]["respuesta"]

        # uso el counter para imprimir la pregunta en orden de aparicion
        print(f"{counter}) {pregunta}")

        for alternativa in alternativas:
            print(alternativa)
        print()

        # obtiene la respuesta del usuario y la pone en minusculas
        respuesta = input("Tu respuesta: ").lower()

        # permite que la respuesta obtenida sea una alternativa valida
        while respuesta not in ("a", "b", "c", "d"):
            respuesta = input(
                "Respuesta invalida, debes responder una de las alternativas a, b, c o d. Ingresa nuevamente tu respuesta: "
            ).lower()

        # verifica si la respuestas del usuario es correcta
        if respuesta == correcta:
            puntaje += 10  # 10 puntos si es correcta
            print(f"{colors['GREEN']}Muy bien, {nombre}!{colors['RESET']}")
        else:
            # 0 puntos si es incorrecta
            print(
                f"{colors['RED']}Tu respuesta fue incorrecta, {nombre}{colors['RESET']}"
            )
        input("Presiona Enter para continuar...")

        # limpia la pantalla y continua con la siguiente pregunta
        counter += 1
        os.system("cls")

    # clasifica el puntaje del usuario de acuerdo a sus puntos y da color al mensaje
    if puntaje > 50:
        print(
            f"{colors['GREEN']}Excelente, {nombre}, has obtenido {puntaje}/100 puntos {colors['RESET']}"
        )
    elif puntaje > 20:
        print(
            f"{colors['YELLOW']}No esta mal {nombre}, has obtenido {puntaje}/100 puntos {colors['RESET']}"
        )
    else:
        print(
            f"{colors['RED']}Has obtenido {puntaje}/100 puntos. Repasa y si quieres puedes seguir intentando{colors['RESET']}"
        )

    # pregunta al usuario si quiere continuar la trivia
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: "
    ).lower()

    # si no quiere, en_trivia es falso y no habra otro loop
    if repetir_trivia != "si":
        print(f"\nEspero que lo hayas pasado bien, {nombre}, hasta pronto!")
        en_trivia = False
        
        #Todo bien me gusto la importación de otros archivos pero falta crear el readme
