from encuesta import Encuesta

class Usuarios():
    
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self):
        return self.__correo
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad
    
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region):
        self.__region = region

    def contestar_encuesta(self, encuesta: Encuesta, respuestas: list):
        encuesta.agregar_respuestas_listado(respuestas)