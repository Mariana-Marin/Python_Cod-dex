Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")

respuesta1 = int(input("Ingrese su respuesta (1 o 2): "))
if respuesta1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif respuesta1 == 2:
    Slytherin += 1
    Hufflepuff += 1
else:
    print("Respuesta no válida. Por favor, ingrese 1 o 2.")

print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")


respuesta2 = int(input("Ingrese su respuesta (entre 1 y 4): "))
if respuesta2 == 1:
    Hufflepuff += 2
elif respuesta2 == 2:
    Slytherin += 2
elif respuesta2 == 3:
    Ravenclaw += 2
elif respuesta2 == 4:
    Gryffindor += 2
else:
    print("Respuesta no válida. Por favor, ingrese un número entre 1 y 4.")

print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")

respuesta3 = int(input("Ingrese su respuesta (1 a 4): "))
if respuesta3 == 1:
    Hufflepuff += 4
elif respuesta3 == 2:
    Ravenclaw += 4
elif respuesta3 == 3:
    Gryffindor += 4
elif respuesta3 == 4:
    Slytherin += 4
else:
    print("Respuesta no válida. Por favor, ingrese un número entre 1 y 4.")

print ("resultados:")
print (f"Gryffindor: {Gryffindor}")
print (f"Ravenclaw: {Ravenclaw}")
print (f"Hufflepuff: {Hufflepuff}")
print (f"Slytherin: {Slytherin}")

if Gryffindor > max(Ravenclaw, Hufflepuff, Slytherin):
    print("¡Felicidades! Has sido seleccionado para Gryffindor.")
elif Ravenclaw > max(Gryffindor, Hufflepuff, Slytherin):
    print("¡Felicidades! Has sido seleccionado para Ravenclaw.")
elif Hufflepuff > max(Gryffindor, Ravenclaw, Slytherin):
    print("¡Felicidades! Has sido seleccionado para Hufflepuff.")
elif Slytherin > max(Gryffindor, Ravenclaw, Hufflepuff):
    print("¡Felicidades! Has sido seleccionado para Slytherin.")