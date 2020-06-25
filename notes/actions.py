import notes.note as model

class Actions:

    def create(self, user):
        print("Vamos a crear una nueva nota")

        title = input("Ingresa el título de tu nota: ")
        desc = input("Ingresa el contenido de tu nota: ")

        note = model.Note(user[0], title, desc)
        save = note.save()

        if save[0] >= 1:
            print(f"\nPerfecto, has guardado la nota {note.title}")
        else:
            print(f"\nNo se ha podido guardar la nota")
