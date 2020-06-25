import users.user as model

class Actions:
    def register(self):
        print("\nPerfecto, vamos a registrarte en el sistema")
        name = input("¿Cuál es tu nombre?: ")
        lastname = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        user = model.User(name, lastname, email, password)
        register = user.register()

        if(register[0] >= 1):
            print(f"\nPerfecto, {register[1].name} te has registrado con el email {register[1].email}")
        else:
            print("\nError al registrarse")


    def login(self):
        print("\nBien, identifícate en el sistema")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            user = model.User("", "", email, password)
            login = user.login()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.nextActions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto")
    
    def nextActions(self, user):
        print("""
        Acciones disponibles:
        -1 Crear notas (crear)
        -2 Mostrar tus notas (mostrar)
        -3 Eliminar nota (eliminar)
        -4 Salir (salir)
        """)

        action = input("¿Qué deseas hacer?: ")

        if action == "crear":
            print("Crear")
            self.nextActions(user)
        elif action == "mostrar":
            print("Mostrar")
            self.nextActions(user)
        elif action == "eliminar":
            print("El")
            self.nextActions(user)
        elif action == "salir":
            print(f"Hasta pronto, {user[1]}")
            exit()