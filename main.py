from drivers import *
from constructors import *
from races import *
from circuits import * 

import sys
import time
import random
import os

#Busqueda de constructor por nacionalidad
def search_const_bycountry():
    cbc_query = ""
    while not cbc_query.isalnum():
        cbc_query = input("Enter the nationality by which to filter constructors:\n")
    print(f"Constructores de la nacionalidad {cbc_query}:")
    try:
        for cq in constructor_list:
            if cbc_query == cq.cNationality:
                print(cq.cName)
    except:
        print("No se encontró ningún constructor con esa nacionalidad.")

#Busqueda de pilotos por constructor
def search_drivers_byconstructor():
    dbc_query = ""
    while not dbc_query.isalnum():
        dbc_query = input("Enter the constructor by which to filter drivers:\n")
    try:
        for dq in driver_list:
            if dbc_query == dq.team:
                print(f"Pilotos del constructor {dq.team}:\n")
                print (dq)
    except:
        print("No se encontraron pilotos con ese constructor.")
def search_race_bycircuitcountry():
    rbcc_query = ""
    while not rbcc_query.isalnum():
        rbcc_query = input("Enter the circuit country by which to filter races:\n")
    for rq in race_list:
        if rbcc_query == rq.raceCircuit['country']:
            print (rq.raceName)

def search_race_bymonth():
    rbm_query = ""
    while rbm_query == "":
        rbm_query = input("Enter the month by which to filter races(format: mm):\n")
    for rm in race_list:
        if rbm_query == rm.raceDate[4:-3]:
            print (rm)

def main():
    mainmenu()

def mainmenu():
    while True:
        menu_options = [1, 2, 3, 4, 5, 6]
        user_input = 0
        print("\n*MENÚ PRINCIPAL*")
        print("*GESTIÓN DE FÓRMULA 1*")
        print("Opciones")
        print("[1]Buscar y filtar información de carreras")
        print("[2]Finalizar carreras y crear podios de ganadores")
        print("[3]Registrar compra de entradas/registro de cliente")
        print("[4]Registrar compra en restaurantes/buscar productos")
        print("[5]Mostrar estadísticas")
        print("[6]Salir del programa")

        while user_input not in menu_options:
            user_input = input("Introduzca una opción:\n")
            try:
                user_input = int(user_input)
                break
            except ValueError:
                print("Inválido: Necesitas introducir un número correspondiente a una opción.")
        
        if user_input == 1:
            print("Opción 1: Buscar y filtrar información de carreras")
            searchmenu()
        elif user_input == 2:
            print("Opción 2")
        elif user_input == 3:
            print("Opción 3")
        elif user_input == 4:
            print("Opción 4")
        elif user_input == 5:
            print("Opción 5")
        elif user_input == 6:
            print("Opción 6: Salir del Programa")
            print("SALIENDO...")
            time.sleep(2)
            sys.exit()
def searchmenu():
    while True:
        s_menu_options = [1, 2, 3, 4, 5, 6]
        s_user_input = 0
        print("\n*MENÚ DE BÚSQUEDAS*")
        print("Opciones")
        print("[1]Filtrar constructores por país")
        print("[2]Filtrar pilotos por constructor")
        print("[3]Filtrar carreras por país de circuito")
        print("[4]Filtrar carreras por mes")
        print("[5]Volver al menú principal")

        while s_user_input not in s_menu_options:
            s_user_input = input("Introduzca una opción:\n")
            try:
                s_user_input = int(s_user_input)
                break
            except ValueError:
                print("Inválido: Necesitas introducir un número correspondiente a una opción.")

        if s_user_input == 1:
            print("Opción 1:Filtrar constructores por país")
            search_const_bycountry()
        elif s_user_input == 2:
            print("Opción 2:Filtrar pilotos por constructor")
            search_drivers_byconstructor()
        elif s_user_input == 3:
            print("Opción 3:Filtrar carreras por país de circuito")
            search_race_bycircuitcountry()
        elif s_user_input == 4:
            print("Opción 4:Filtrar carreras por mes")
            search_race_bymonth()
        elif s_user_input == 5:
            print("Volviendo al menú anterior...")
            time.sleep(2)
            break
        
main()



