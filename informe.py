from datetime import datetime
class Informe():
    def __init__(self, carrera, total):
        self.__Reescribir__(self.__Leer__(carrera, total), carrera)
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
    def __Reescribir__(self, datos, carrera):
        f = open("Informe.txt", "w")
        for x in range (0, len(datos)):
            if (x == 0):
                f.write(datos[x])
            else:
                f.write(f"\n{datos[x]}")
        f.close()
        self.__NuevaUltima__(carrera)
        print("Informe listo")
    ##Escribir la ultima carrera
    def __NuevaUltima__(self, dato):
        f = open("Ultima.txt", "w")
        f.write(dato)
        f.close()