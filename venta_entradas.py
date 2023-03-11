listaDeClientes = []

def cliente():
    def __init__(self, name, clientID, age, race, ticketType):
        self.name = name
        self.clientID = clientID
        self.age = age
        self.race = race 
        self.ticketType = ticketType 
        
def mostrar_clientes():
    print("\nLISTA DE CLIENTES\n")
    print(listaDeClientes)

def esOndulante(clientID):
    if (len(clientID) <= 2):
        return False
    for i in range(2, len(clientID)):
        if (clientID[i - 2] != clientID[i]):
            return False 
    return True

def agregar_cliente(cliente):
    nameinput = ""
    clientIDinput = ""
    ageinput = ""
    raceinput = ""
    ticketTypeinput = ""
    while True:
        nuevoCliente = None
        while not nameinput.isalpha():
            if not nameinput.isalpha():
                nameinput = input("Introduzca el nombre del cliente:\n")
        while not clientIDinput.isnumeric():
            if not clientIDinput.isnumeric():

                clientIDinput = input("Introduzca número de identidad o cédula del cliente:\n")

                if (esOndulante(clientIDinput)):
                    print("\n¡Su entrada tiene un %50 de descuento!\n")
                else:
                    print("\nSu entrada no disfruta de ningún descuento.\n")  

        while not ageinput.isnumeric():
            if not ageinput.isnumeric():
                ageinput = input("Introduzca la edad del cliente:\n")
        while not raceinput.isalnum():
            if not raceinput.isalnum():
                raceinput = input("Introduza el nombre de la carrera que desea atender:\n")
        while not ticketTypeinput.isalpha():
            if not ticketTypeinput.isalpha():
                ticketTypeinput = input("Introduza el tipo de entrada que desea comprar:\n")
        break
    nuevoCliente = cliente(nameinput, clientIDinput, ageinput, raceinput, ticketTypeinput)
    listaDeClientes.append(nuevoCliente)


agregar_cliente()
mostrar_clientes()