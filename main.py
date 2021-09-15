from correos import Mensaje
from data import Data
from archivo import Archivo
class Main():
    def __init__(self):
        #Comentar lo que no se vaya a usar
        self.__Archivo__('Datos.txt')
        #self.__Pagina__()
    def __Archivo__(self, nombre):
        #Leer desde un archivo debe de ser Carrera Matricula Correo Instrumentacion faltante
        data = Archivo().Datos(nombre)
        Mensaje(data)
    def __Pagina__(self):
        #Leer desde la pagina
        Data().datos()
Main()