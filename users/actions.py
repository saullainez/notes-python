class Actions:
    def register(self):
        print("\nPerfecto, vamos a registrarte en el sistema")
        name = input("¿Cuál es tu nombre?")
        lastname = input("¿Cuáles son tus apellidos?")
        email = input("Introduce tu email")
        password = input("Introduce tu contraseña")

    def login(self):
        print("\nBien, identifícate en el sistema")
        email = input("Introduce tu email")
        password = input("Introduce tu contraseña")