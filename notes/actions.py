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
    
    def show(self, user):
        print("\nEstas son tus notas: ")

        note = model.Note(user[0])
        notes = note.show()

        for note in notes:
            print("\n****************************************************")
            print(note[2])
            print(note[3])
            print("\n****************************************************")

    def delete(self, user):
        print("\nVamos a borrar notas")
        title = input("\nIntroduce el título de la nota a borrar: ")

        note = model.Note(user[0], title)
        delete = note.delete()

        if delete[0] >= 1:
            print(f"Se ha borrado la nota: {note.title}")
        else:
            print("No se ha podido borrar la nota")
