class Agenda:
    def __init__(self):
        self.notas = []
        self.tareas = []
        self.eventos = []
        self.agenda = [self.notas, self.tareas, self.eventos]
 
    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota agregada: {nota}")
 
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea agregada: {tarea}")