# Yes - definitely.
# It is decidedly so.
# Without a doubt.
# Reply hazy, try again.
# Ask again later.
# Better not tell you now.
# My sources say no.
# Outlook not so good.
# Very doubtful.

import random

pregunta=input("¿Tienes una pregunta para la bola mágica?:  ")

respuesta = random.randint(1, 9)

if respuesta == 1:
    print("Sí - definitivamente.")
elif respuesta == 2:
    print("Es decididamente así.")
elif respuesta == 3:
    print("Sin duda.")
elif respuesta == 4:
    print("Respuesta vaga, intenta de nuevo.")
elif respuesta == 5:
    print("Debes preguntar de nuevo más tarde.")
elif respuesta == 6:
    print("Mejor no te lo digo ahora.")
elif respuesta == 7:
    print("Mis fuentes dicen que no.")
elif respuesta == 8:
    print("Las perspectivas no son tan buenas.")
elif respuesta == 9:
    print("Muy dudoso.")
elif respuesta < 1 or respuesta > 9:
    print("Por favor, ingresa un número entre 1 y 9.")