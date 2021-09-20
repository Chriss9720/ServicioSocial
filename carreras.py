class Carreras:
    def __init__(self, datos):
        self.__CrearArchivoDeCarreras__(datos)
    def __Datos__(self):
        carreras = ["ARQ","IAE","IAG","IEM","IGEM","IGGM","IIGM","IIMC","IIMS","IISL","IM","IMA","ISCM","ISCW",
        "LAMK","LANI","MPIA","MPID","MPIS"]
    def __CrearArchivoDeCarreras__(self, datos):
        f = open("Carreras.txt", "w")
        cont = 0
        enLista = []
        for i in datos:
            if self.__Esta__(i['Carrera'], enLista):
                if cont == 0:
                    f.write(i['Carrera'])
                else:
                    f.write("\n" + i['Carrera'])
                cont += 1
                enLista.append(i['Carrera'])
        f.close()
    def __Esta__(self, dato, lista):
        for i in lista:
            if dato in i:
                return False
        return True