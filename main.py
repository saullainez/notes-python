#Menú principal
print("""
Selecciona el número de la acción que desees realizar.
Acciones disponibles:
    -1 Registro.
    -2 Login.
""")

action = input("¿Qué deseas hacer?")

if action == "1":
    print("Perfecto, vamos a registrarte en el sistema")
elif action == "2":
    print("Bien, identifícate en el sistema")