#pip install PyMails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#pip install smtplib
import smtplib
import time
from datetime import datetime
from Internet import Con
class Mensaje:
    def __init__(self, lista, correo, psw, intervalo):
        self.lista = lista
        self.intento = 0
        self.Correo = correo
        self.Psw = psw
        self.esperar = intervalo
        self.mandar()
    def mandar(self):
        Errores = []
        vuelta = 0
        for i in range(0, len(self.lista)):
            try:
                Con()
                to = [self.lista[i]["Correo"], self.lista[i]["Matricula"]]
                mensaje = f"""
Hola, esperamos que te encuentres bien:
Somos compañeros de ITESCA que estamos haciendo el servicio social en el seguimiento al SISETI (Si sé de ti, construiremos un futuro). En la revisión, hemos visto que te faltan por responder los siguientes instrumentos: {self.lista[i]['Faltantes']}
Te recordamos que es necesario que los contestes todos para que se logre el objetivo y seas tomado en cuenta cuando se elaboren programas de apoyo.
Te invitamos a entrar al siguiente link para realizar los instrumentos;
https://app.itesca.edu.mx/accounts/login/
Si surge alguna duda, revisa este enlace:
https://youtu.be/dHc6uMguLvU
Si aún surge alguna duda estaremos disponibles para asesorarte.
¡Saludos!
"""
                msg = MIMEMultipart()
                password = self.Psw
                msg["From"] = self.Correo
                msg["To"] = ', '.join(to)
                msg["Subject"] = "Instrumetación SISETI"
                msg.attach(MIMEText(mensaje, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                server.login(msg["From"], password)
                server.sendmail(msg["From"], to, msg.as_string())
                try:
                    server.quit()
                except:
                    print("Fallo al cerrar el servidor")
                vuelta += 1
            except Exception as e:
                print(e)
                print(i)
                Errores.append(
                    {
                        'Carrera' : self.lista[i]["Carrera"],
                        'Matricula' : self.lista[i]['Matricula'],
                        'Correo': self.lista[i]['Correo'],
                        'Faltantes' : self.lista[i]['Faltantes']
                    }
                )
            now = datetime.now()
            moment = now.strftime("%H:%M:%S")
            print(f"Han pasado: {(i * self.esperar) / 60} minutos. {(vuelta)} correos. Se mando a {self.lista[i]['Matricula']}. Enviado a las {moment}.")
            time.sleep(self.esperar)
        self.__Datos__(Errores)
        print(f"En este intento {self.intento} se mandaron {vuelta} y hubo {len(Errores)} errores")
        self.intento += 1
        print(f"Extras: {(((len(Errores)) * self.esperar) / 60)} minutos")
        self.__Recuperacion__(Errores)
    def __Recuperacion__(self, Errores):
        while (len(Errores) > 0):
            now = datetime.now()
            moment = now.strftime("%H:%M:%S")
            print(f"Recuperando: {len(Errores)}. Se tardara: {((len(Errores) * self.esperar) / 60)} minutos. Se empezo a la hora: {moment}")
            vuelta = 0
            ERRORESAUX = []
            for i in range(0, len(Errores)):
                try:
                    Con()
                    to = [Errores[i]["Correo"], Errores[i]["Matricula"]]
                    mensaje = f"""
Hola, esperamos que te encuentres bien:
Somos compañeros de ITESCA que estamos haciendo el servicio social en el seguimiento al SISETI (Si sé de ti, construiremos un futuro). En la revisión, hemos visto que te faltan por responder los siguientes instrumentos: {self.lista[i]['Faltantes']}
Te recordamos que es necesario que los contestes todos para que se logre el objetivo y seas tomado en cuenta cuando se elaboren programas de apoyo.
Te invitamos a entrar al siguiente link para realizar los instrumentos;
https://app.itesca.edu.mx/accounts/login/
Si surge alguna duda, revisa este enlace:
https://youtu.be/dHc6uMguLvU
Si aún surge alguna duda estaremos disponibles para asesorarte.
¡Saludos!
"""
                    msg = MIMEMultipart()
                    password = self.Psw
                    msg["From"] = self.Correo
                    msg["To"] = ', '.join(to)
                    msg["Subject"] = "Instrumetación SISETI"
                    msg.attach(MIMEText(mensaje, 'plain'))
                    server = smtplib.SMTP('smtp.gmail.com: 587')
                    server.starttls()
                    server.login(msg["From"], password)
                    server.sendmail(msg["From"], to, msg.as_string())
                    try:
                        server.quit()
                    except:
                        print("Fallo al cerrar el servidor")
                    vuelta += 1
                except Exception as e:
                    print(e)
                    print(i)
                    ERRORESAUX.append(
                        {
                            'Carrera' : Errores[i]["Carrera"],
                            'Matricula' : Errores[i]['Matricula'],
                            'Correo': Errores[i]['Correo'],
                            'Faltantes' : Errores[i]['Faltantes']
                        }
                    )
                now = datetime.now()
                moment = now.strftime("%H:%M:%S")
                print(f"Han pasado: {((i * self.esperar) / 60)} minutos. {(vuelta)} correos. Se mando a {Errores[i]['Matricula']}. Enviado a las {moment}")
                time.sleep(self.esperar)
            self.__Datos__(ERRORESAUX)
            print(f"En este intento {self.intento} se mandaron {vuelta} y hubo {len(ERRORESAUX)} errores")
            print(f"Extras: {(((len(ERRORESAUX)) * self.esperar) / 60)} minutos")
            self.intento += 1
            Errores = ERRORESAUX
        print("Se terminaron de mandar todos correos")
    def __Datos__(self, data):
        for i in data:
            print(f"{i['Carrera']} {i['Matricula']} {i['Correo']} {i['Faltantes']}")