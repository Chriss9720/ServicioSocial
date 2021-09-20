from datetime import datetime
class Informe():
    def __init__(self, carrera, total):
        self.__Reescribir__(self.__Leer__(carrera, total))
    def __Leer__(self, carrera, total):
        datos = []
        try:
            f = open("Informe.txt", "r")
            for x in f:
                datos.append(x.replace("\n", ""))
        except:
            print("No hay datos")
        now = datetime.today().strftime("%d/%m/%Y")
        datos.append(f"{now}->{carrera}->{total}")
        return datos
    def __Reescribir__(self, datos):
        f = open("Informe.txt", "w")
        for x in range (0, len(datos)):
            if (x == 0):
                f.write(datos[x])
            else:
                f.write(f"\n{datos[x]}")
        f.close()
        print("Informe listo")