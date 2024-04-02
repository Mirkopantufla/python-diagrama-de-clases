from usuario import Usuarios

class ListadoRespuestas():

    def __init__(self, listado_respuestas, usuario):
        self.__listado_respuestas = listado_respuestas
        self.__usuario = usuario # correo: str || edad: int || region: int

    @property
    def listado_respuestas(self):
        return self.__listado_respuestas
    
    @property
    def usuario(self):
        return self.__usuario