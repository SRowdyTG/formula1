def constructores():
    def __init__(self, name, team, nationality):
        self.name = name
        self.team = team
        self.nationality = nationality 

def carreras():
    def __init__(self, round, name, circuit):
        self.round = round
        self.name = name
        self.circuit = circuit

def circuitos():
    def __init__(self, circuitID, name, country, locality, lat, lon):
        self.circuitID = circuitID
        self.name = name
        self.country = country
        self.locality = locality
        self.lat = lat
        self.long = lon

def pilotos():
    def __init__(self, driverID, permanentNumber, code, team, firstName, lastName, dateOfBirth, nationality):
        self.driverID = driverID
        self.permanentNumber = permanentNumber
        self.code = code
        self.team = team
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality

parameters = [{
    "id": 0
}
]

import requests
req = requests.get("https://github.com/Algorimtos-y-Programacion-2223-2/api-proyecto/blob/f8e2b420a8f9f5a27463eb29e1df63605822be13/drivers.json", parameters)
print(req.status_code)
print(req.json())
