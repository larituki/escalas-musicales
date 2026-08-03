#Programa que pregunta las escalas músicales mayores de forma aleatoria
import random 

def sostenidos(escalaMayoresSostenidos):
    escalaElegida = escalasMayoresSostenidos[random.randint(0,7)]
    i = 0
    print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
    for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
        notaEscala = input()
        if notaEscala != escalaElegida[i]:
            print(f"Nota incorrecta: {escalaElegida[i]}")
        i += 1

def bemoles(escalaMayoresBemoles):
    escalaElegida = escalasMayoresBemoles[random.randint(0,7)]
    i = 0
    print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
    for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
        notaEscala = input()
        if notaEscala != escalaElegida[i]:
            print(f"Nota incorrecta: {escalaElegida[i]}")
        i += 1

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
    


sostenidos(escalasMayoresSostenidos)