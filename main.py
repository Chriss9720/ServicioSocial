from correos import Mensaje
from data import Data
from archivo import Archivo
class Main():
    #Leer desde un archivo debe de ser Carrera Matricula Correo Instrumentacion faltante
    def __init__(self):
        self.name = "Datos.txt" ##Nombre del archivo
        self.correo = 'serviciosocialag2021@gmail.com' ##Correo de donde se mandaran
        self.psw = 'qqsrpxfbhsxiqjjf' ##Clave del correo
        self.Usuario = '18130159' ##Usuario del SISETI
        self.clave = '12345678' ##Clave del SISETI
        self.__Pagina__() #Crea el archivo self.nombre con toda la informacion de la pagina
        #self.__Buscar__('21130211') #Recibe una matricula y dice si existe
        self.__Mandar__() #Carrera matricula correo instrumentos
    def __Mandar__(self):
        data = Archivo().Datos(self.name)
        Mensaje(data, self.correo, self.psw)
    def __Pagina__(self):
        Data(self.name, self.Usuario, self.clave)
    def __Buscar__(self, mat):
        data = Archivo().Datos(self.name)
        datos = ""
        for i in data:
            if (mat in i["Matricula"]):
                datos = i
        if (len(datos) > 0):
            print(datos)
        else:
            print("No esta en la lista de faltantes")
Main()