from drivers import *
#importing
class constructor:
    '''Definición de la clase constructor()'''
    def __init__(self,  cID, cName, cNationality, cDrivers):
        self.cID = cID
        self.cName = cName
        self.cNationality = cNationality
        self.cDrivers = cDrivers

    def add_drivers(self, driver_list):
        '''Añade pilotos correspondientes a cada objeto de la clase constructor()'''
        for element in driver_list:
            if element.team.replace(" ", "").lower() == self.cID.replace(" ", "").lower():
                self.cDrivers.append(element.driverID)

    def dict(self):
        '''Método de expresión en forma de diccionario'''
        return {
            "ID" : self.cID,
            "Name" : self.cName,
            "Nationality" : self.cNationality,
            "Drivers" : self.cDrivers
        }
    
    def __str__(self):
        '''Método de expresión en forma de cadena'''
        return "{\n"f"ID: {self.cID}\nName: {self.cName}\nNationality: {self.cNationality}\nDrivers: {self.cDrivers}\n""},\n"

    def __repr__(self):
        '''Método de expresión para lista'''
        return "{\n"f"ID: {self.cID}\nName: {self.cName}\nNationality: {self.cNationality}\nDrivers: {self.cDrivers}\n""},\n"

cretrieval = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/f8e2b420a8f9f5a27463eb29e1df63605822be13/constructors.json")
print(cretrieval.status_code)
downloaded_list_constructors = cretrieval.json()
#Request
constructor_list = []
#list definition
def assign_constructordata():
    '''Construye un nuevo objeto de la clase constructor() a partir de la información de cada elemento de la lista descargada por API en cretrieval.json()'''
    newConstructorID = ""
    newConstructorName = ""
    newConstructorNationality = ""
    newDrivers = []
    #Definitions for placeholder new constructor
    for e in downloaded_list_constructors:
        newConstructorID = e['id']
        newConstructorName = e['name']
        newConstructorNationality = e['nationality']
        newDrivers = []
        newConstructor = constructor(newConstructorID, newConstructorName, newConstructorNationality, newDrivers)
        constructor_list.append(newConstructor)
    #Convert requested data to objects and add to list
#Convert downloaded list of elements to objects and append to list
def save_constructordata():
    '''Guarda la lista de objetos de la clase constructor() en memoria a un archivo de texto'''
    save_constructors_tofile = open("constructors.txt", "w")
    save_constructors_tofile.write("[")
    for e in constructor_list:
        save_constructors_tofile.write(e.__str__())
    save_constructors_tofile.write("]")
    save_constructors_tofile.close()
    #Write downloaded data to file
#save appended list to file

assign_constructordata()
for c in constructor_list:
    c.add_drivers(driver_list)
save_constructordata()