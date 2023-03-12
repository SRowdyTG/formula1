import requests

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

newDriver = driver("bottas", 77, "BOT", "alfa", "Valtteri", "Bottas", "1989-08-28", "Finnish" )

response = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json")
print(response.status_code)
print(response.json())
