from users import actions
#Menú principal
print("""
Selecciona el número de la acción que desees realizar.
Acciones disponibles:
    -1 Registro.
    -2 Login.
""")

do = actions.Actions()

action = input("¿Qué deseas hacer?")

if action == "1":
    do.register()
elif action == "2":
    do.login()
