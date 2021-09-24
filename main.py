from correos import Mensaje
from data import Data
from archivo import Archivo
from datetime import datetime
from informe import Informe
import time
class Main():
    #Leer desde un archivo debe de ser Carrera Matricula Correo Instrumentacion faltante
    def __init__(self):
        self.name = "Datos.txt" ##Nombre del archivo
        self.correo = 'serviciosocialsiseti2021@gmail.com' ##Correo de donde se mandaran
        self.psw = 'cuuviellugjnnmhn' ##Clave del correo
        self.Usuario = '18130159' ##Usuario del SISETI
        self.clave = '12345678' ##Clave del SISETI
        self.Intervalo = 300 #Intervalo en segundos (5 min de preferencia)
        #self.__Pagina__() #Crea el archivo self.nombre con toda la informacion de la pagina
        bander = True
        while (bander):
            try:
                print("***********Menu principal****************")
                op = int(input("Que desea hacer:\n1.Buscar por matricula\n2.Mandar correos\n3.Salir\nOpcion: "))
                print("***********************************")
                if (op == 1):
                    while (op == 1):
                        print("***********Ingrese****************")
                        matricula = str(input("Matricula: "))
                        self.__Buscar__(matricula) #Recibe una matricula y dice si existe
                        op = int(input("Volver a buscar: \n1.Si \n2.No\nOpcion: "))
                        print("***********************************")
                elif (op == 2):
                    self.__Mandar__() #Carrera matricula correo instrumentos
                elif (op == 3):
                    bander = False
                else:
                    bander = True
                    print("Opcion invalida")
                    print("***********************************")
            except Exception as e:
                bander = True
                print(f"Main.py 40. Opcion invalida: {e}")
                print("***********************************")
        print("Programa terminado")
    def __Mandar__(self):
        bM = True
        Cont = True
        newData = Archivo().Datos(self.name, True)
        now = datetime.now()
        moment = now.strftime("%H:%M:%S")
        while (Cont):
            try:
                print("***********Menu correos****************")
                print(f"Se tardara: {((len(newData) * self.Intervalo) / 60)} minutos.")
                op = int(input("Desea continuar\n1.Si\n2.No\nOpcion: "))
                if(op == 1):
                    bM = True
                    Cont = False
                elif (op == 2):
                    bM = False
                    Cont = False
                else:
                    bM = False
                    Cont = True
                    print("Opcion invalida")
                print("***********************************")
            except Exception as e:
                bM = False
                Cont = True
                print(f"Main.py 68. Opcion invalida: {e}")
                print("***********************************")
        if (bM):
            print(f"***********Se empezo a la hora: {moment}****************")
            Mensaje(newData, self.correo, self.psw, self.Intervalo)
            Informe(newData[0]['Carrera'], len(newData))
            time.sleep(60)
            print("***********************************")
    def __Pagina__(self):
        Data(self.name, self.Usuario, self.clave)
    def __Buscar__(self, mat):
        data = Archivo().Datos(self.name, False)
        datos = ""
        print("***********Resultado****************")
        for i in data:
            aux = i["Matricula"].replace('@e-itesca.edu.mx', '')
            if (mat == aux):
                datos = f"{i['Faltantes']}{i['Carrera']}"
        if (len(datos) > 0):
            print(datos)
        else:
            print("No esta en la lista de faltantes")
        print("***********************************")
Main()