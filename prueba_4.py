from funciones import *
contador_entradas = 500
Entradas_1 = {
    "Conciertos":[
        {
            "nombre" : "thomas",
            "concierto": "Fortificados",
            "tipo_de_entrada": "V",
            "Codigo_de_confirmacion": "Thom12"

        }
        ,
          

        {
            "nombre" : "maximiliano",
            "concierto":"Iluminados",
            "tipo_de_entrada": "V",
            "Codigo_de_confirmacion": "THOm1"
        }
    ]
}

def validar_nombre(mensaje:str):
    while True:
        entrada = input(mensaje).strip()
        repetido = False
        for x in Entradas_1["Conciertos"]:
            if x["nombre"].lower() == entrada.lower():
                print("El nombre se a encontrado por lo tanto no lo puede repetir")
                repetido = True
                break
        if not repetido:
            return entrada


def descontador():
    for x in Entradas_1["Conciertos"]:
        if x["concierto"] == "fortificado" or x["concierto"] == "Iluminados":
            contador_entradas =- 1
            return x

while True:
    print("'''TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1.- Comprar entrada a “los Fortificados”.")
    print("2.- Comprar entrada a “los Iluminados”.")
    print("3.- Stock de entradas para ambos conciertos.")
    print("4.- Salir.")
    opc = validar_opc("ingrese la opcion que desea: ")

    if opc == 1:
        Nombre = validar_nombre("Ingrese su nombre : ")
        Tipo_entrada = validar_general_o_vip("Ingrese su tipo de entrada en mayuscula y solo inicial(G-V): ")
        Codigo = validar_codigo_1("Ingrese su codigo debe contener 6 caracteres alfanumericos:  ")

        agregar_comprador = {
            "nombre" : Nombre,
            "tipo_de_entrada": Tipo_entrada,
            "Codigo_de_confirmacion": Codigo,
            "concierto" : "Fortificados"
        }
        Entradas_1["Conciertos"].append(agregar_comprador)

        print("Comprador agregado con exito...")
    elif opc == 2:
        Nombre = validar_nombre("Ingrese su nombre : ")
        Tipo_entrada = validar_Cancha_o_palco("Ingrese su tipo de entrada en mayuscula y solo inicial(G-V): ")
        Codigo = validar_codigo_2("Ingrese su codigo debe contener 5 caracteres 3 mayusculas y un numero sin espacios:  ")

        agregar_comprador = {
            "nombre" : Nombre,
            "tipo_de_entrada": Tipo_entrada,
            "Codigo_de_confirmacion": Codigo,
            "concierto" : "Iluminados"
        }
        Entradas_1["Conciertos"].append(agregar_comprador)
        print("Comprador agregado con exito...")
    elif opc == 3:
        descontador()
        print(f"las entradas disponibles son :",contador_entradas)
    elif opc == 4:
        print("Programa terminado...")
        break

