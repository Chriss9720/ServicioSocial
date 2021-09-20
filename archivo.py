from carreras import Carreras
class Archivo:
    def Datos(self, nombre):
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
        carrera = Carreras().iniciarBusqueda(data)
        filtro = []
        print(f"Se seleciono {carrera}")
        for x in data:
            if x['Carrera'] in carrera:
                filtro.append(
                    {
                        'Carrera' : dato[0],
                        'Matricula' : f'{dato[1]}@e-itesca.edu.mx',
                        'Correo': dato[2],
                        'Faltantes' : faltantes
                    }
                )
        print(f"Salieron {len(filtro)} objetos")
        return filtro