#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 5 - Patrones de comportamiento.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 5:
# Modifique el programa IS2_taller_memory.py para que la clase tenga la 
# capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los 
# mismos en cualquier orden de ser necesario. El método undo deberá tener un 
# argumento adicional indicando si se desea recuperar el inmediato anterior (0) y 
# los anteriores a el (1,2,3)
#------------------------------------------------------------------------------------------------------------------

# Patron de comportamiento memento

import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []  # Lista para almacenar los estados anteriores

    def write(self, string):
        self.content += string

    def save(self):
        if len(self.history) == 4:  # Si ya hay 4 estados en la historia, eliminamos el más antiguo
            del self.history[0]
        memento = Memento(self.file, self.content)
        self.history.append(memento)

    def undo(self, steps_back=0):  # El argumento steps_back indica cuántos pasos hacia atrás se desean recuperar
        if steps_back >= len(self.history):  # Si se solicita más de lo que hay en la historia, se recupera el primer estado
            steps_back = len(self.history) - 1
        memento = self.history[-1 - steps_back]  # Recuperar el memento indicado
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps_back=0):
        writer.undo(steps_back)

    def undo_to_step(self, writer, step):
        total_steps = len(writer.history) - 1
        steps_back = total_steps - step
        writer.undo(steps_back)


if __name__ == '__main__':
    os.system("cls")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

# Se le pasa a undo directamente el espacio en memoria al que se quiera retroceder 
print ("Se invoca al <undo> y se le asigna que vaya a memoria 1 ")
caretaker.undo_to_step(writer, 0)
print ("Se muestra el estado actual:")
print (writer.content + "\n\n")

print ("Se invoca al <undo> y se le asigna que vaya a memoria 2 ")
caretaker.undo_to_step(writer, 1)
print ("Se muestra el estado actual:")
print (writer.content + "\n\n")



#pasos para invocar al <undo> la memoria anterior de cada estado actual

    #print("Se invoca al <undo> para recuperar el estado anterior")
    #caretaker.undo(writer)
    #print("Se muestra el estado actual:")
    #print(writer.content + "\n\n")

    #print("Se invoca al <undo> para recuperar el estado anterior al inmediato anterior")
    #caretaker.undo(writer, steps_back=1)
    #print("Se muestra el estado actual:")
    #print(writer.content + "\n\n")

    #print("Se invoca al <undo> para recuperar el estado dos pasos atrás")
    #caretaker.undo(writer, steps_back=2)
    #print("Se muestra el estado actual:")
    #print(writer.content + "\n\n")

    #print("Se invoca al <undo> para recuperar el estado tres pasos atrás")
    #caretaker.undo(writer, steps_back=3)
    #print("Se muestra el estado actual:")
    #print(writer.content + "\n\n")
