from clases import Paciente
from clases import Paciente_infectado
from clases import Paciente_no_infectado
from clases import Paciente_posible_infectado
from clases import Pais
from funciones import nombre_completo
from funciones import edad_paciente
from funciones import direccion
from funciones import estado
from funciones import ciudad
from funciones import doctor
from funciones import numero
from funciones import paises_covid_19
from funciones import mas_infectados
from funciones import selection_sort_recuperados
from funciones import selection_sort_muertos
from funciones import selection_sort_infectados
import requests 

def main():

    pacientes=[]
    print("""       
  
   _____ ______      _______ _____        __  ___    _______ _____            _____ _  ________ _____  
  / ____/ __ \ \    / /_   _|  __ \      /_ |/ _ \  |__   __|  __ \     /\   / ____| |/ /  ____|  __ \ 
 | |   | |  | \ \  / /  | | | |  | |______| | (_) |    | |  | |__) |   /  \ | |    | ' /| |__  | |__) |
 | |   | |  | |\ \/ /   | | | |  | |______| |\__, |    | |  |  _  /   / /\ \| |    |  < |  __| |  _  / 
 | |___| |__| | \  /   _| |_| |__| |      | |  / /     | |  | | \ \  / ____ \ |____| . \| |____| | \ \ 
  \_____\____/   \/   |_____|_____/       |_| /_/      |_|  |_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ 
  
  
  """)

    print("Por favor ingrese los datos del paciente")
    nom=nombre_completo()
    edad= edad_paciente()

    print("Bienvenido {}".format(nom))
    print("Por favor responda a las siguientes preguntas")
    
    cont=0
    while True:
        enter=input("¿Tiene secreciones nasales?(S/N): ").strip()
        if enter.title()=="S":
            cont+=1
            break
        if enter.title()=="N":
            break
        else:
            continue
    
    while True:
        enter=input("¿Tiene dolor de garganta?(S/N):  ").strip()
        if enter.title()=="S":
            cont+=1
            break
        if enter.title()=="N":
            break
        else:
            continue

    while True:
        enter=input("¿tiene tos?(S/N)").strip()
        if enter.title()=="S":
            cont+=1
            break
        if enter.title()=="N":
            break
        else:
            continue

    while True:
        enter=input("¿Dificultad para respirar? (S/N)").strip()
        if enter.title()=="S":
            cont+=1
            break
        if enter.title()=="N":
            break
        else:
            continue
    
    if cont==4:
        print("Infectado")
        dire=direccion()
        city=ciudad()
        state=estado()
        doc=doctor()
        pacie_infect=Paciente_infectado(nom,edad,dire,city,state,doc)
        pacientes.append(pacie_infect)
        print("""     
        Esta infectado, comuniquese con su doctor de confianza.
        Paciente:
        Nombre: {}
        Edad: {}
        Direccion: {}
        Ciudad: {}
        Estado: {}
        Medico tratante: {}
        """.format(pacie_infect.nombre_completo,pacie_infect.edad,pacie_infect.direccion,pacie_infect.ciudad,pacie_infect.estado,pacie_infect.doctor))

    elif cont>=2:
        print("Posible infectado")
        dire=direccion()
        city=ciudad()
        state=estado()
        pacie_posible= Paciente_posible_infectado(nom,edad,dire,city,state)
        pacientes.append(pacie_posible)
        print("""     
        Posible infectado, mantengase en cuarentena. 
        Paciente:
        Nombre: {}
        Edad: {}
        Direccion: {}
        Ciudad: {}
        Estado: {}
        """.format(pacie_posible.nombre_completo,pacie_posible.edad,pacie_posible.direccion,pacie_posible.ciudad,pacie_posible.estado))
        

    elif cont >=1:
        print("En revision")
        number= numero()
        revision= Paciente_no_infectado(nom,edad,number)
        pacientes.append(revision)
        print("""     
        Posible infectado, mantengase en cuarentena. 
        Paciente:
        Nombre: {}
        Edad: {}
        telefono: {}
        """.format( revision.nombre_completo,revision.edad,revision.telefono))

    else:
        print("No infectado")
        number= numero()
        revision= Paciente_no_infectado(nom,edad,number)
        pacientes.append(revision)
        print("""     
        Posible infectado, mantengase en cuarentena. 
        Paciente:
        Nombre: {}
        Edad: {}
        telefono: {}
        """.format( revision.nombre_completo,revision.edad,revision.telefono))

    while True:
        print("Bienvenido/a a la zona de estadisticas")
        entrada=input("""
        1) Buscador de Paises
        2) Top 10 de paises con mas infectados, muertes y recuperados
        3) Cerrar el programa 
        >>>> """)
        if entrada== "1":
            paises_covid_19()
            continue
        if entrada=="2":
            mas_infectados()
            continue
        else:
            break







main()