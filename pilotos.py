import requests
import json 

class driver():
    def __init__(self, driverID, permanentNumber, code, team, firstName, lastName, dateOfBirth, nationality):
        self.driverID = driverID
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality
    
    def __str__(self):
        return f"ID: {self.driverID}\nNúmero Permanente: {self.permanentNumber}\nCódigo: {self.code}\nNombre: {self.firstName}\nApellido: {self.lastName}\nFecha de Nacimiento: {self.dateOfBirth}\nNacionalidad: {self.nationality}"
    
    def dict(self):
        return {'id': self.driverID,
                'permanentNumber': self.permanentNumber,
                'code': self.code,
                'team': self.team,
                'firstName': self.firstName,
                'lastname': self.lastName,
                'dateOfBirth': self.dateOfBirth,
                'nationality': self.nationality}

newDriver = driver("IDPRUEBA", 1337, "PRUEB", "equipoPRUEBA", "nombrePrueba", "apellidoPRUEBA", "1989-08-28", "nacioPRUEBA")

response = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json")
print(response.status_code)
print(response.json())

print(newDriver)
