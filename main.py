#Menú principal
print("""
Selecciona el número de la acción que desees realizar.
Acciones disponibles:
    -1 Registro.
    -2 Login.
""")

action = input("¿Qué deseas hacer?")

if action == "1":
    print("\nPerfecto, vamos a registrarte en el sistema")
    name = input("¿Cuál es tu nombre?")
    lastname = input("¿Cuáles son tus apellidos?")
    email = input("Introduce tu email")
    password = input("Introduce tu contraseña")
elif action == "2":
    print("\nBien, identifícate en el sistema")
    email = input("Introduce tu email")
    password = input("Introduce tu contraseña")