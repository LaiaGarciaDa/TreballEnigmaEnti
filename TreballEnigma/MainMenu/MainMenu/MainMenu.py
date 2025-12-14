import Xifrat


def mostrar_pantalla():
    print("Enigma")
    print("1. Notches")
    print("2. Xifrar")
    print("3. Borrar")
    print("4. Sortir")


def opcio_1():
    Xifrat.Notches()


def opcio_2():
    Xifrat.xifrar()


def opcio_3():
    archivo = open('Text.txt', 'w')
    archivo.write(" ")
    print("Text esborrat correctament")

while True:
    mostrar_pantalla()
    opcio = input("Selecciona que vols fer (1-3)")

    if(opcio == '1'):
        opcio_1()
    elif(opcio == '2'):
        opcio_2()
    elif(opcio == '3'):
        opcio_3()
    elif(opcio == '4'):
        print("Sortir")
        break
    else:
        print("No es una opcio valida")
      

