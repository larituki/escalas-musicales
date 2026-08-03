#Programa que pregunta las escalas músicales mayores de forma aleatoria
import random 

escalasMayoresSostenidos = [
    ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    ["Sol", "La", "Si", "Do", "Re", "Mi", "Fa#"],
    ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do#"],
    ["La", "Si", "Do#", "Re", "Mi", "Fa#", "Sol#"],
    ["Mi", "Fa#", "Sol#", "La", "Si", "Do#", "Re#"],
    ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol#", "La#"],
    ["Fa#", "Sol#", "La#", "Si", "Do#", "Re#", "Mi#"],
    ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#", "Si#"]
]

escalasMayoresBemoles = [
    ["Fa", "Sol", "La", "Sib", "Do", "Re", "Mi"],
    ["Sib", "Do", "Re", "Mib", "Fa", "Sol", "La"],
    ["Mib", "Fa", "Sol", "Lab", "Sib", "Do", "Re"],
    ["Lab", "Sib", "Do", "Reb", "Mib", "Fa", "Sol"],
    ["Reb", "Mib", "Fa", "Solb", "Lab", "Sib", "Do"],
    ["Solb", "Lab", "Sib", "Dob", "Reb", "Mib", "Fa"],
    ["Dob", "Reb", "Mib", "Fab", "Solb", "Lab", "Sib"]
]

#Poner cuantas veces quiere que se repita, tipo cuantas escalas. O un while hasta que marque salir
def sostenidos(escalaMayoresSostenidos):
    while True:
        escalaElegida = escalasMayoresSostenidos[random.randint(0,7)]
        i = 0
        print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
        for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
            notaEscala = input()
            if notaEscala != escalaElegida[i]:
                print(f"Nota incorrecta: {escalaElegida[i]}")
            i += 1
        print("Pulsa 1 para continuar o 0 para salir")
        continuarEscalas = int(input())
        if continuarEscalas == 0:
            break
        

def bemoles(escalaMayoresBemoles):
    while True:
        escalaElegida = escalasMayoresBemoles[random.randint(0,6)]
        i = 0
        print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
        for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
            notaEscala = input()
            if notaEscala != escalaElegida[i]:
                print(f"Nota incorrecta: {escalaElegida[i]}")
            i += 1
        print("Pulsa 1 para continuar o 0 para salir")
        continuarEscalas = int(input())
        if continuarEscalas == 0:
            break

def combinados(escalasMayoresSostenidos, escalasMayoresBemoles):
    while True:
        eligeSostenidosBemoles = random.randint(1, 2)
        if eligeSostenidosBemoles == 1:
            sostenidos(escalasMayoresSostenidos)
        else:
            bemoles(escalasMayoresBemoles)


def menu():
    opcion = 0
    while True:
        opcion = int(input("Elige la opción correspondiente:\n1.Sostenidos\n2.Bemoles\n3.Combinados\n4.Salir\n"))
        match opcion:
            case 1:
                sostenidos(escalasMayoresSostenidos)
            case 2:
                bemoles(escalasMayoresBemoles)
            case 3:
                combinados(escalasMayoresSostenidos, escalasMayoresBemoles)
            case 4: 
                print("Saliste")
                break

menu()

    

