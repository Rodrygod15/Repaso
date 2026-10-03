class Mascara:
    def __init__(self, personaje, color):
        self.personaje = personaje
        self.color = color

    def mostrar_informacion(self):
        print(f"Esta es la máscara de {self.personaje} y su color es {self.color}")
 