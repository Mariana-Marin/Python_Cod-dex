# Utilice una combinación de operadores lógicos y relacionales para crear las reglas:

# Si son lo suficientemente altos y tienen suficientes créditos, imprima "¡Disfruta el viaje!"
# De lo contrario, si tienen suficientes créditos, pero no son lo suficientemente altos, imprima "No eres lo suficientemente alto para montar".
# De lo contrario, si son lo suficientemente altos, pero no tienen suficientes créditos, imprima "No tienes suficientes créditos".
# De lo contrario, imprima un mensaje diciendo que no han cumplido ninguno de los requisitos.

altura = int(input("Ingrese su altura en cm: "))
creditos = int(input("Ingrese la cantidad de créditos que tiene: "))

if altura >= 135 and creditos >= 10:
    print("¡Disfruta el viaje!")
elif creditos >= 10:
    print("No eres lo suficientemente alto para montar.")
elif altura >= 135:
    print("No tienes suficientes créditos.")
else:
    print("No has cumplido ninguno de los requisitos.")