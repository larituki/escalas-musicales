#Programa que pregunta las escalas músicales mayores de forma aleatoria
#Deberia hacer manejo de errores xd
#Y algo sobre la capitalizacion de las letras YA LO HICE WOO
import random 
import time 

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
def sostenidos():
    inicio = time.time()
    escalaElegida = escalasMayoresSostenidos[random.randint(0,7)]
    print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
    aciertos = 0
    for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
        notaEscala = input().capitalize()
        if notaEscala == nota:
            aciertos += 1
        else:
            print(f"Nota incorrecta. Corrección: {nota}")

    final = time.time()
    print(f"\nAciertos: {aciertos}/7")
    print(f"Tiempo: {final - inicio:.2f} segundos") #Tiempo de finalizacion, podria pasar a minutos ig
        

def bemoles():
    inicio = time.time()
    escalaElegida = escalasMayoresBemoles[random.randint(0,6)]
    print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
    aciertos = 0
    for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
        notaEscala = input().capitalize()
        if notaEscala == nota:
            aciertos += 1
        else:
            print(f"Nota incorrecta. Corrección: {nota}")

    final = time.time()
    print(f"\nAciertos: {aciertos}/7")
    print(f"Tiempo: {final - inicio:.2f} segundos")

def combinados():
        eligeSostenidosBemoles = random.randint(1, 2)
        if eligeSostenidosBemoles == 1:
            sostenidos()
        else:
            bemoles()


def menu():
    opcion = 0
    while True:
        try:
            opcion = int(input("Elige la opción correspondiente:\n1.Sostenidos\n2.Bemoles\n3.Combinados\n4.Salir\n"))
        except:
             print("=================================")
             print("Elige una de las opciones válidas")
             print("==================================")
        else:
            match opcion:
                case 1:
                    while True:
                        sostenidos()
                        print("Pulsa 1 para continuar o 0 para salir")
                        continuarEscalas = int(input())
                        if continuarEscalas == 0:
                            break
                case 2:
                    while True:
                        bemoles()
                        print("Pulsa 1 para continuar o 0 para salir")
                        continuarEscalas = int(input())
                        if continuarEscalas == 0:
                            break
                case 3:
                    while True:
                        combinados()
                        print("Pulsa 1 para continuar o 0 para salir")
                        continuarEscalas = int(input())
                        if continuarEscalas == 0:
                            break
                case 4: 
                    print("Saliste")
                    break

print("======================================")
print("            ESCALAS MAYORES")
print("======================================")
menu()


    

