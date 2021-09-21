from correos import Mensaje
from data import Data
from archivo import Archivo
from datetime import datetime
from informe import Informe
import time
class Main():
    #Leer desde un archivo debe de ser Carrera Matricula Correo Instrumentacion faltante
    def __init__(self):
        self.enviados = 0
        self.name = "Datos.txt" ##Nombre del archivo
        self.correo = 'serviciosocialsiseti2021@gmail.com' ##Correo de donde se mandaran
        self.psw = 'cuuviellugjnnmhn' ##Clave del correo
        self.Usuario = '18130159' ##Usuario del SISETI
        self.clave = '12345678' ##Clave del SISETI
        self.time = 300 #Intervalo en segundos (5 min de preferencia)
        self.__Pagina__() #Crea el archivo self.nombre con toda la informacion de la pagina
        #self.__Buscar__('21130211') #Recibe una matricula y dice si existe
        self.__Mandar__() #Carrera matricula correo instrumentos
        print("Programa terminado")
    def __Mandar__(self):
        while (self.enviados < 50):
            data = Archivo().Datos(self.name)
            self.enviados += len(data)
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            print(f"Se tardara: {((len(data) * self.time) / 60)} minutos. Se empezo a la hora: {time}")
            Mensaje(data, self.correo, self.psw, self.time)
            Informe(data[0]['Carrera'], len(data))
            time.sleep(60)
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