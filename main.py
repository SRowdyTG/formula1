from carreras import *
from venta_entradas import *
from pilotos import *
from circuitos import *

import time
import random

class admin():
    def __init__(self):
        pass
    
    def finalize_race():
        #random de pilots
        pass

    def set_podium():
        #organizar pilotos
        pass

    def set_driver_champ():
        pass

    def set_constructor_champ():
        #comparar equipos con nombre de pilotos
        pass

class search(admin):
    admin.__init__()
    def __init__(self):
        pass
    def schConstructorByCountry():
        pass
    def schDriverByConstructor():
        pass
    def schRaceByCircuitCountry():
        pass
    def schRaceByMonth():
        pass

def main():
    choice = 0
    while True:
        print ("Bienvenido a la app de Gestión de F1.\n")
        print("[1]Gestionar carreras, equipos y pilotos\n[2]Gestionar venta de entradas\n[3]Gestionar asistencia a carreras\n[4]Gestionar restaurantes\n[5]Gestionar ventas en restaurantes\n[6]Estadísticas")
        while choice == 0:
            choice = input("Decide qué hacer a continuación:\n")
            if choice == 1:
                #entrar a menu de carreras
            elif choice == 2:
                #entrar a menu de ventas
            elif choice == 3:
                #entrar a menu de asistencia
            elif choice == 4:
                #entrar a menu de restaurantes
            elif choice == 5:
                #entrar a menu de ventas en restaurantes
            elif choice == 6:
            elif choice == 7:





