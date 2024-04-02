class Alternativas():

    def __init__(self, contenido: str, ayuda: str):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        return f"""Contenido: {self.contenido}\tAyuda: {self.ayuda}"""