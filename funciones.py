from clases import Paciente
from clases import Paciente_infectado
from clases import Paciente_no_infectado
from clases import Paciente_posible_infectado
import requests
from clases import Pais

#MODULO 1 

def nombre_completo():
    """ Esta funcion se encarga de pedir el nombre completo del usuario.
    
    Returns:
        String -- Nombre completo ingresedo por el usuario.
    """
    resp=True
    while resp==True:
        nombre= (input(" por favor ingrese su nombre: ")).strip()
        if nombre.isalpha():
            break
        if len(nombre) < 2 or nombre.isdigit() or " " in nombre:
            print("no valido")
            continue
        
    while True:    
        nombre2=(input(" ingrese su segundo nombre (si tiene): ")).strip()
        if nombre2=="":
            break
        if nombre2.isalpha():
            break
        if len(nombre2) < 2 or nombre2.isdigit() or " " in nombre2:
            print("no valido")
            continue
    resp2=True
    while resp2:
        apellido= (input(" ingrese su apellido: ")).strip()
        if len(apellido) < 2 or apellido.isdigit() or " " in apellido:
            print("No valido")
            continue
        if apellido.isalpha():
            break
    
    while True:
        apellido2= (input(" ingrese su segundo apellido (opcional): ")).strip()
        if apellido2=="":
            break
        if len(apellido2) < 2 or apellido2.isdigit() or " " in apellido2:
            print('No valido')
            continue
        if apellido2.isalpha():
            break

    Full_name=(" {} {} {} {}".format(nombre.title(),nombre2.title(),apellido.title(),apellido2.title()))
    return Full_name

def edad_paciente():
    """Esta funcion se encarga de pedir la edad al paciente.
    
    Returns:
        String -- Edad ingresada por el paciente.
    """
    resp= True
    while resp:
        edad= (input(" Ingrese su edad: ")).strip()
        if not edad.isdigit():
            print("Por favor ingresa tu edad")
        elif int(edad) <1 or int(edad)>140:
            print("intenta otra vez ")
        else: 
            return edad

def direccion():
    """[Esta funcion se encarga de pedir la direccion del paciente.]
    
    Returns:
        [string] -- [Direccion ingresada por el paciente.]
    """
    while True:
        direccion=input("Ingrese su direccion: ").strip()
        if direccion.isdigit():
            continue
        if len(direccion) > 100:
            print("muy largo")
        if len(direccion) < 15:
            continue
        else:
            break
    return direccion


def estado():
    """[Esta funcion se encarga de pedir el estado en el que se encuentra el paciente. ]
    
    Returns:
        [string] -- [Estado ingresado por el paciente]
    """
    estados_vzla=["Amazonas","Anzoategui","Apure","Aragua", "Barinas","Bolivar","Carabobo","Cojedes","Delta Amacuro","Distrito Capital","Falcon","Guarico","Lara","Merida","Miranda","Monagas","Nueva Esparta","Portuguesa","Sucre","Tachira","Trujillo", "Vargas", "Yaracuy","Zulia"]      
    while True:
        estado=input("En que estado vive: ").strip()
        estado.title()
        if estado.title() in estados_vzla:
            break
    return estado.title()

def ciudad():
    """[Esta funcion se encarga de pedir la ciudad en la que vive el paciente.]
    
    Returns:
        [string] -- [La ciudad ingresada por el paciente. ]
    """
    while True: 
        ciudad=input("Ingrese la ciudad en donde vive: ").strip()
        if ciudad.isalpha():
            break
    return ciudad


    



def doctor():
    """ Esta funcion se encarga de pedir el nombre completo del doctor.
    
    Returns:
        String -- Nombre completo del doctor ingresedo por el paciente.
    """
    resp=True
    while resp:
        nombre= (input(" por favor ingrese el nombre de su doctor: ")).strip()
        if nombre.isalpha():
            break
        if len(nombre) < 2 or nombre.isdigit() or " " in nombre:
            print("no valido")
            continue
        
    while True:    
        nombre2=(input(" ingrese su segundo nombre (opcional): ")).strip()
        if nombre2=="":
            break
        if nombre2.isalpha():
            break
        if len(nombre2) < 2 or nombre2.isdigit() or " " in nombre2:
            print("no valido")
            continue
    resp2=True
    while resp2:
        apellido= (input(" ingrese su apellido: ")).strip()
        if len(apellido) < 2 or apellido.isdigit() or " " in apellido:
            print("No valido")
            continue
        if apellido.isalpha():
            break
        
    while True:
        apellido2= (input(" ingrese su segundo apellido (opcional): ")).strip()
        if apellido2=="":
            break
        if len(apellido2) < 2 or apellido2.isdigit() or " " in apellido2:
            print('No valido')
            continue
        if apellido2.isalpha():
            break

    Full_name=(" {} {} {} {}".format(nombre.title(),nombre2.title(),apellido.title(),apellido2.title()))
    return Full_name

def numero():
    while True:
        cell=input("Ingrese su numero de telefono: ")
        if len(cell) > 11:
            print("no es un numero valido")
            continue
        elif cell.isdigit():
            print("yes")
            break
    return cell 

def paises_covid_19():
    """[Esta funcion imprime las estadistas sobre el Covid-19 del pais que ingrese la persona]
    
    """
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    pais=input("Ingrese un pais: ")
    querystring = {"country":pais}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "7f40582e5fmshf4cf807610f4775p16b455jsnef71e2e4b914"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    dic=response.json()
    datos_pais=dic["data"] ["covid19Stats"]  
    
    confirmados=0
    curados=0
    muertos=0 
    for dicci in datos_pais:
        confirmados+=dicci["confirmed"]
        curados+= dicci["recovered"]
        muertos+= dicci["deaths"]
    print("""
    Pais: {}   
    Confirmados: {}
    Curados: {}
    Muertos: {}
    """.format(pais,confirmados,curados,muertos))



def mas_infectados():
    """[Se encarga de imprimir el top 10 de paises con mas infectados, mas muertes y mas recuperados]
    """
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    
    

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "7f40582e5fmshf4cf807610f4775p16b455jsnef71e2e4b914"
        }
    response = requests.request("GET", url, headers=headers)
    dic=response.json()
    datos_pais=dic["data"] ["covid19Stats"]
    #print(datos_pais)
    datos_pais_util={}
    for ditionari in datos_pais:
        if not ditionari["country"] in datos_pais_util: 
            datos_pais_util[ditionari["country"]]= {"Infectados":ditionari["confirmed"],"Muertos":ditionari["deaths"],"Recuperados":ditionari["recovered"]}
        if ditionari["country"] in datos_pais_util:
            datos_pais_util[ditionari["country"]]["Infectados"]+=ditionari["confirmed"]
            datos_pais_util[ditionari["country"]]["Muertos"]+=ditionari["deaths"]
            datos_pais_util[ditionari["country"]]["Recuperados"]+= ditionari["recovered"]
    
    lista_paises_object= []
    for pais,datos in datos_pais_util.items():
        lista_paises_object.append(Pais(pais,datos["Infectados"],datos["Muertos"],datos["Recuperados"]))
    top_infectados=selection_sort_infectados(lista_paises_object)[0:10]
    top_muertos=selection_sort_muertos(lista_paises_object)[0:10]
    top_recuperados=selection_sort_recuperados(lista_paises_object)[0:10]

    print("<>"*10)
    print("top Infectados")
    for pais in top_infectados:
        print("""Pais: {} - Infectados: {}""".format(pais.nombre_pais,pais.infectados))

    print("<>"*10)
    print("Top Muertes")
    for pais in top_muertos:
        print("Pais: {} - Muertos: {}".format(pais.nombre_pais,pais.muertos))

    print("<>"*10)
    print("Top Recuperados")
    for pais in top_recuperados:
        print("Pais: {} - Recuperados: {}".format(pais.nombre_pais,pais.recuperados))
    print("<>"*10)
    
 



def selection_sort_infectados (arr): 
    """[esta funcion se encarga de ordenar de mayor a menor la cantidad de infectados que hay por pais]
    
    Arguments:
        arr {[lista]} -- [ lista de infectados por pais ]

    Returns:
        [lista] - [Lista ordenada de mayor a menor numero de infectados ]

    """       
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j].infectados < arr[minimum].infectados:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr[::-1]

def selection_sort_muertos (arr): 
    """[esta funcion se encarga de ordenar de mayor a menor la cantidad de muertes que hay por pais]
    
    Arguments:
        arr {[lista]} -- [lista de muertes por pais ]


    Returns:
        [lista] - [Lista ordenada de mayor a menor numero de muertes]
    """       
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j].muertos < arr[minimum].muertos:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr[::-1]

def selection_sort_recuperados (arr): 
    """[esta funcion se encarga de ordenar de mayor a menor la cantidad de recuperados que hay por pais]
    
    Arguments:
        arr {[lista]} -- [Lista  de recuperados  por pais]
    
    Returns:
        [lista] -- [lista ordenada de mayor a menor de pacientes recuperados]
    """
     
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j].recuperados < arr[minimum].recuperados:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr[::-1]

   



    



#paises_covid_19()


