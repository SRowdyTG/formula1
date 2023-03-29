from races import race_list
from uuid import uuid4
import time
import sys
client_list = []

class client:
    def __init__(self, clientName, clientID, clientAge, desiredRace, ticketType, clientTicketCost, uniqueID):
        self.clientName = clientName
        self.clientID = clientID
        self.clientAge = clientAge
        self.desiredRace = desiredRace
        self.ticketType = ticketType 
        self.clientTicketCost = clientTicketCost
        self.uniqueID = uniqueID

    def __str__(self):
        return f"Nombre: {self.clientName}\nCédula: {self.clientID}\nEdad: {self.clientAge}\nCarrera: {self.desiredRace}\nTipo de Entrada: {self.ticketType}\nCosto Total: ${self.ticketCost}\nID Único: {self.uniqueID}"

def show_clients():
    s_choice = 0
    while True:
        s_choice = input("¿Mostrar clientes en memoria[1] o mostrar clientes guardados en archvivo[2]?")
        if s_choice == 1:
            print("\n*LISTA DE CLIENTES*\n")
            for c in client_list:
                print(c)
            break
        elif s_choice == 2:
            try:
                show_cfile = open("clients.txt", "r")
                show_cfile.read()
                break
            except:
                print("*ARCHIVO NO ENCONTRADO*")
                break

def esOndulante(clientID):
    if (len(clientID) <= 2):
        return False
    for i in range(2, len(clientID)):
        if (clientID[i - 2] != clientID[i]):
            return False 
    return True

def add_clients():
    clientNameInput = ""
    clientIDinput = ""
    clientAgeInput = ""
    clientRaceInput = ""
    ticketTypeinput = ""
    ticketCost = None
    newUniqueID = None
    while True:
        newClient = None
        while not clientNameInput.isalpha():
            if not clientNameInput.isalpha():
                clientNameInput = input("Introduzca el nombre del cliente:\n")

        while not clientIDinput.isnumeric():
            if not clientIDinput.isnumeric():
                clientIDinput = input("Introduzca número de identidad o cédula del cliente:\n")  
        while not clientAgeInput.isnumeric():
            if not clientAgeInput.isnumeric():
                clientAgeInput = input("Introduzca la edad del cliente:\n")
        while not clientRaceInput.isalnum():
            if not clientRaceInput.isalnum():
                print("Carreras disponibles:")
                for r in race_list:
                    print (r.raceName)
                clientRaceInput = input("Introduzca el nombre de la carrera que desea atender(escribiendo un nombre de la lista):\n")
        while not ticketTypeinput.isalpha():
            if not ticketTypeinput.isalpha():
                ticketTypeinput = input("Introduzca el tipo de entrada que desea comprar('General' o 'VIP'):\n")
        if ticketTypeinput == "General":
            ticketCost = 150
        elif ticketTypeinput == "VIP":
            ticketCost == 340
        ticketCost = ticketCost + (ticketCost(16//100))
        if (esOndulante(clientIDinput)):
            ticketCost = ticketCost // 50
        break
    print()
    print("*RECIBO*")
    print(clientNameInput,"\n",clientIDinput,"\n", clientAgeInput,"\n", clientRaceInput,"\n", ticketTypeinput,"\n", ticketCost)
    print("IVA(16%): \n$", ticketCost(16//100))
    print("Descuento:")
    if (esOndulante(clientIDinput)):
        print("¡Su entrada tiene un %50 de descuento!")
    else:
        print("\nSu entrada no disfruta de ningún descuento.")
    choices = [1, 2]
    ticket_continue = 0
    while ticket_continue not in choices:
        ticket_continue = input("¿Registrar compra de entradas y continuar? [1]Sí [2]No\n")
        try:
            ticket_continue = int(ticket_continue)
            break
        except ValueError:
            print("Inválido: Necesitas introducir un número correspondiente a una opción.")
    if ticket_continue == 1:
        newUniqueID = str(uuid4())
        newClient = client(clientNameInput, clientIDinput, clientAgeInput, clientRaceInput, ticketTypeinput, ticketCost, newUniqueID)
        client_list.append(newClient)
        print("Compra registrada. Tus asientos son: ...")
    elif ticket_continue == 2:
        newClient = None

def save_clients():
    save_clients_tofile = open("clients.txt", "w")
    save_clients_tofile.write("[")
    for c in client_list:
        save_clients_tofile.write(c.__dict__)
    save_clients_tofile.write("]")
    save_clients_tofile.close()
