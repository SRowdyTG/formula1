import json
import requests
#importing
class driver:
    '''Definición de la clase driver()'''
    #Attributes
    def __init__(self, driverID, permanentNumber, code, team, firstName, lastName, dateOfBirth, nationality):
        self.driverID = driverID
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.firstName = firstName
        self.lastName = lastName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality
    #Dictionary method
    def __dict__(self):
        '''Método de expresión en forma de diccionario'''
        return {
            "ID:" : self.driverID,
            "Permanent Number:" : self.permanentNumber,
            "Code:" : self.code,
            "Team:" : self.team,
            "First Name:" : self.firstName,
            "Last Name:" : self.lastName,
            "DOB:" : self.dateOfBirth,
            "Nationality:" : self.nationality
            }
    #String method
    def __str__(self):
        '''Método de expresión en forma de cadena'''
        return "{\n"f"ID: {self.driverID}\nPermanent Number: {self.permanentNumber}\nCode: {self.code}\nTeam: {self.team}\nFirst Name: {self.firstName}\nLast Name: {self.lastName}\nDOB: {self.dateOfBirth}\nNationality: {self.nationality}\n""}\n"
    #List method
    def __repr__(self):
        '''Método de expresión para lista'''
        return "{\n"f"ID: {self.driverID}\nPermanent Number: {self.permanentNumber}\nCode: {self.code}\nTeam: {self.team}\nFirst Name: {self.firstName}\nLast Name: {self.lastName}\nDOB: {self.dateOfBirth}\nNationality: {self.nationality},\n""}\n"
#Driver class definition

driver_list = []

retrieval = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/f8e2b420a8f9f5a27463eb29e1df63605822be13/drivers.json")
print(retrieval.status_code)
downloaded_list_drivers = retrieval.json()
#Request

def assign_and_save_driverdata():
    '''Construye un nuevo objeto de la clase driver() a partir de la información de cada elemento de la lista descargada por API en retrieval.json() y guarda la lista de objetos de la clase driver() en memoria a un archivo de texto'''
    newDriverID = ""
    newDriverNumber = ""
    newDriverCode = ""
    newDriverTeam = ""
    newDriverfName = ""
    newDriverlName = ""
    newDriverDOB = ""
    newDriverNationality = ""
    #Definitions for placeholder new driver
    for d in downloaded_list_drivers:
        newDriverID = d['id']
        newDriverNumber = d['permanentNumber'] 
        newDriverCode = d['code']
        newDriverTeam =d ['team']
        newDriverfName = d['firstName'] 
        newDriverlName =d ['lastName']
        newDriverDOB = d['dateOfBirth']
        newDriverNationality = d['nationality']
        newDriver = driver(newDriverID, newDriverNumber, newDriverCode, newDriverTeam, newDriverfName, newDriverlName, newDriverDOB, newDriverNationality)
        driver_list.append(newDriver)
    #Convert requested data to objects and add to list

    save_drivers_tofile = open("drivers.txt", "w")
    save_drivers_tofile.write("[")
    for o in driver_list:
        save_drivers_tofile.write(o.__str__())
    save_drivers_tofile.write("]")
    save_drivers_tofile.close()
    #Write downloaded data to file
#convert downloaded list of drivers to objects, append to list and save appended list to file
assign_and_save_driverdata()