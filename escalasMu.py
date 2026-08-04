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
def preguntaEscala(lista):
    inicio = time.time()
    escalaElegida = random.choice(lista)
    print(f"Escribe la escala correspondiente: {escalaElegida[0]} Mayor")
    aciertos = 0
    grado = 1
    for nota in escalaElegida: #Nota ya tiene el valor, no el indice 
        print(f"{grado}: ")
        notaEscala = input().capitalize()
        if notaEscala == nota:
            aciertos += 1
        else:
            print(f"Nota incorrecta. Corrección: {nota}")
        grado += 1
    

    final = time.time()
    print(f"\nAciertos: {aciertos}/7")
    print(f"Tiempo: {final - inicio:.2f} segundos") #Tiempo de finalizacion, podria pasar a minutos ig
    return
        

def combinados():
        eligeSostenidosBemoles = random.randint(1, 2)
        if eligeSostenidosBemoles == 1:
            preguntaEscala(escalasMayoresSostenidos)
        else:
            preguntaEscala(escalasMayoresBemoles)

def loop(function, algo):
    while True:
        function(algo)
        print("Pulsa 1 para continuar o 0 para salir")
        try:
            continuarEscalas = int(input())
        except:
            print("=================================")
            print("Elige una de las opciones válidas")
            print("==================================")
        else:
            if continuarEscalas == 0:
                break

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
                    loop(preguntaEscala, escalasMayoresSostenidos)
                case 2:
                    loop(preguntaEscala, escalasMayoresBemoles)
                case 3:
                    loop(combinados)
                case 4: 
                    print("Saliste")
                    break

print("======================================")
print("            ESCALAS MAYORES")
print("======================================")
menu()



    

