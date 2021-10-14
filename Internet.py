import requests
import time
class Con():
    def __init__(self):
        b = True
        while (b):
            try:
                request = requests.get("https://www.google.com/", timeout=5)
            except (requests.ConnectionError, requests.Timeout):
                print("No se encontro conecion a internet")
                time.sleep(180)
                b = True
            else:
                b = False
Con()