from alternativa import Alternativas

class Preguntas():

    def __init__(self, enunciado: str, ayuda: str, requerido: bool, alternativas: list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerido = requerido
        self.__lista_alternativas = [Alternativas(alternativa['enunciado'], alternativa['ayuda']) for alternativa in alternativas]

    @property
    def lista_alternativas(self):
        return self.__lista_alternativas

    def mostrar_pregunta(self):
        print(f"Enunciado: {self.enunciado}\n")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}\n")
        for alternativa in self.lista_alternativas:
            alternativa.mostrar_alternativa()
    
