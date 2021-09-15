#pip install selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
class Data:
    def __init__(self, name, user, psw):
        self.__datos__(name, user, psw)
    def __datos__(self, name, nombre, clave):
        browser = webdriver.Chrome()
        browser.get('https://app.itesca.edu.mx/')
        user = browser.find_element_by_id('id_username')
        user.send_keys(nombre)
        psw = browser.find_element_by_id('id_password')
        psw.send_keys(clave)
        psw.submit()
        content = browser.find_element_by_xpath("/html/body").text.split("\n")
        bandera = False
        f = open(name, "w")
        cont = 0
        for i in content:
            if (bandera and len(i) > 8):
                if "ARQ" in i or "LA" in i:
                    if cont == 0:
                        f.write(i)
                    else:
                        f.write("\n" + i)
                    cont += 1
            if (i == 'Mayores de 18 años' and not bandera):
                bandera = True
        f.close()
        browser.quit()
        print(f"Se escribieron {cont} lineas")