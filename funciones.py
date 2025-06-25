

def validar_opc(mensaje:str):
    while True:
        try:
            entrada = int(input(mensaje))
            if entrada <= 0 :
                print("Ingresa un numero entero positivo..")
                continue
            elif entrada > 4 :
                print("Ingresa una opcion valida")
                continue
            return entrada
        except ValueError:
            print("Ingrese un valor valido..")
            return entrada
        

        


def validar_general_o_vip(mensaje:str):
    while True:
        entrada = input(mensaje).upper()
        if entrada == "G" or entrada == "V":
            return entrada
        else:
            print("Ingrese lo que se le a pedido")
            continue

def validar_Cancha_o_palco(mensaje:str):
    while True:
        entrada = input(mensaje).upper()
        if entrada == "CV" or entrada == "PAL":
            return entrada
        else:
            print("Ingrese lo que se le a pedido")
            continue


def validar_codigo_1(mensaje:str):
    while True:
        serial = input(mensaje).strip()
        if len(serial) == 6:
            return serial
        else:
            print("Ingrese un codigo valido")
            continue 

def validar_codigo_2(mensaje:str):
    while True:
        serial = input(mensaje).strip()
        if len(serial) == 5:
            return serial
        else:
            print("Ingrese un codigo valido")
            continue    


