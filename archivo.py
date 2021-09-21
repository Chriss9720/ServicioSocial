from carreras import Carreras
class Archivo:
    def Datos(self, nombre, mov):
        file = open(nombre, "r")
        data =[]
        for x in file:
            dato = x.split(" ")
            faltantes = ""
            for y in range(3, len(dato)):
                if (len(faltantes) == 0):
                    faltantes = f"{dato[y]}"
                else:
                    faltantes = f"{faltantes} {dato[y]}"
            data.append(
                {
                    'Carrera' : dato[0],
                    'Matricula' : f'{dato[1]}@e-itesca.edu.mx',
                    'Correo': dato[2],
                    'Faltantes' : faltantes
                }
            )
        if (mov != True): return data
        carrera = Carreras().iniciarBusqueda(data)
        filtro = []
        print(f"Se seleciono {carrera}")
        for x in data:
            if x['Carrera'] in carrera:
                filtro.append(
                    {
                        'Carrera' : x['Carrera'],
                        'Matricula' : x['Matricula'],
                        'Correo': x['Correo'],
                        'Faltantes' : x['Faltantes']
                    }
                )
        print(f"Salieron {len(filtro)} objetos de {carrera}")
        return filtro