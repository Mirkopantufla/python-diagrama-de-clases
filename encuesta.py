from pregunta import Preguntas
from listado_respuestas import ListadoRespuestas

class Encuesta():
    def __init__(self, nombre: str, preguntas: list):
        self.nombre = nombre
        #Formato preguntas:
        #enunciado, ayuda, requerido, alternativas
        self.__preguntas = [Preguntas(pregunta['enunciado'],pregunta['ayuda'],pregunta['requerido'],pregunta['alternativas']) for pregunta in preguntas]
        self.__listado_respuestas = []

    def mostrar_encuesta(self):
        print(self.nombre)
        for pregunta in self.__preguntas:
            pregunta.mostrar_pregunta()

    def agregar_respuestas_listado(self, listado_respuestas):
        self.__listado_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):

    def __init__(self, nombre: str, preguntas: list, edad_min: int, edad_max: int):
        super().__init__(nombre, preguntas)

        self.__edad_min = edad_min
        self.__edad_max = edad_max

    #------------------------ Edad minima ------------------------
    @property
    def edad_min(self):
        return self.__edad_min
    
    @edad_min.setter
    def edad_min(self, nuevo_min):
        self.__edad_min = nuevo_min

    #------------------------ Edad maxima ------------------------
    @property
    def edad_max(self):
        return self.__edad_max
    
    @edad_max.setter
    def edad_max(self, nuevo_max):
        self.__edad_max = nuevo_max

    def agregar_respuesta(self, respuestas:list):
        if self.__edad_min <= respuestas.usuario.edad and self.__edad_max >= respuestas.usuario.edad:
            self.__listado_respuestas.append(respuestas)

class EncuestaLimitadaRegion(Encuesta):

    def __init__(self, nombre: str, preguntas: list, regiones: list):
        super().__init__(regiones)

        self.__regiones = regiones

    #------------------------ Edad maxima ------------------------
    @property
    def regiones(self):
        return self.__regiones
    
    @regiones.setter
    def edad_max(self, nuevas_regiones):
        self.__regiones = nuevas_regiones

    def agregar_respuesta(self, respuestas:list):

        #consulto si existe la region del usuario en respuestas, dentro de las regiones de encuesta
        if respuestas.usuario.region in self.__regiones:
            self.__listado_respuestas.append(respuestas)
