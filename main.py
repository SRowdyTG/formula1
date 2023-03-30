from drivers import *
from constructors import *
from races import *
from circuits import * 
from sales import *
import sys
import time
import random
import os


def search_const_bycountry():
    '''Búsqueda de constructores por nacionalidad, comparando el término de búsqueda con el atributo "cNationality" del objeto constructor()'''
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

def search_drivers_byconstructor():
    '''Búsqueda de pilotos por constructor, comparando el término de búsqueda con el atributo "team" del objeto driver()'''
    dbc_query = ""
    while not dbc_query.isalnum():
        dbc_query = input("Enter the constructor by which to filter drivers:\n")
    print(f"Pilotos del constructor {dbc_query}:\n")
    try:
        for dq in driver_list:
            if dbc_query == dq.team:
                print (dq)
    except:
        print("No se encontraron pilotos con ese constructor.")
def search_race_bycircuitcountry():
    '''Búsqueda de carreras por país del circuito, comparando el término de búsqueda con el atributo raceCircuit[country] del objeto race()'''
    rbcc_query = ""
    while not rbcc_query.isalnum():
        rbcc_query = input("Enter the circuit country by which to filter races:\n")
    try:
        for rq in race_list:
            if rbcc_query == rq.raceCircuit['country']:
                print (rq.raceName)
    except:
        print("No se encontraron circuitos con ese país.")
def search_race_bymonth():
    '''Búsqueda de carreras por mes, comparando el término de búsqueda con el atributo "date" del objeto race()'''
    month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    rbm_query = ""
    while rbm_query not in month_list:
        rbm_query = input("Enter the month by which to filter races(format: mm):\n")
    try:
        for rm in race_list:
            if rbm_query == rm.raceDate[4:-3]:
                print (rm)
    except:
        print("No se encontró ninguna carrera en ese mes.")   

def main():
    '''Función básica de inicio del programa'''
    mainmenu()
    
def mainmenu():
    '''Inicia el menú principal, dando a elegir entre el menú de búsqueda, podios, registro de entradas, registro de compras en restaurantes, estadísticas y salida del programa'''
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
            print("Opción 2: Finalizar carreras y crear podios de ganadores")
            racemenu()
        elif user_input == 3:
            print("Opción 3: Registrar compra de entradas/registro de cliente")
            sales_menu()
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
    '''Inicializa el menú de búsqueda, donde se elige entre filtar diferentes elementos como constructores, pilotos y carreras, así como la opción para volver al menú anterior'''
    while True:
        s_menu_options = [1, 2, 3, 4, 5]
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
def sales_menu():
    '''Inicializa el menú de compra de entradas, donde se pueden registrar nuevas compras, mostrar la lista de clientes, guardar esta lista y volver al menú anterior'''
    while True:
            c_menu_options = [1, 2, 3, 4]
            c_user_input = 0
            print("\n*MENÚ DE ENTRADAS*")
            print("Opciones")
            print("[1]Registrar la compra de una entrada/nuevo cliente")
            print("[2]Mostrar lista de clientes")
            print("[3]Guardar lista de clientes a archivo")
            print("[4]Validar entrada para asistir a una carrera")
            print("[5]Volver al menú principal")

            while c_user_input not in c_menu_options:
                c_user_input = input("Introduzca una opción:\n")
                try:
                    c_user_input = int(c_user_input)
                    break
                except ValueError:
                    print("Inválido: Necesitas introducir un número correspondiente a una opción.")

            if c_user_input == 1:
                print("Opción 1:Registrar la compra de una entrada/nuevo cliente")
                add_clients()
            elif c_user_input == 2:
                print("Opción 2:Mostrar lista de clientes")
                show_clients()
            elif c_user_input == 3:
                print("Opción 3:Guardar lista de clientes a archivo")
                save_clients()
            elif c_user_input == 4:
                verif_UniqueID = None
                print("Opción 4:Validar entrada para asistir a una carrera")
                while verif_UniqueID == None:
                    verif_UniqueID = input("Por favor introduzca su código único de validación:\nIntroduzca 'x' para cancelar.\n")
                    if verif_UniqueID != "x":
                        uniqueIDvalidation(verif_UniqueID)
                    elif verif_UniqueID == "x":
                        print("Cancelado. Volviendo al menú anterior...")
                        break
                verif_UniqueID = None
            elif c_user_input == 5:
                print("Volviendo al menú anterior...")
                time.sleep(2)
                break        
def racemenu():
    '''Inicializa el menú de gestión de carreras, donde se pueden finalizar podios de pilotos, constructores, y suma de puntajes'''
    r_menu_options = [1, 2, 3, 4]
    while True:
        r_user_input = 0
        print("\n*MENÚ DE CARRERAS*")
        print("Opciones")
        print("[1]Finalizar una carrera")
        print("[2]Finalizar una temporada")
        print("[3]Volver al menú principal")
        while r_user_input not in r_menu_options:
            r_user_input = input("Introduzca una opción:\n")
            try:
                r_user_input = int(r_user_input)
                break
            except ValueError:
                print("Inválido: Necesitas introducir un número correspondiente a una opción.")
        if r_user_input == 1:
            print("Opción 1: Finalizar una carrera")
            select_race()
            finish_race()
        elif r_user_input == 2:
            print("Opción 2: Finalizar una temporada")
            for x in range(10):
                races_results = []
                select_race()
                finish_race()
                races_results.append(finish_race())
            finish_season()
        elif r_user_input == 3:
            print("Volviendo al menú anterior...")
            time.sleep(2)
            break  
main()



