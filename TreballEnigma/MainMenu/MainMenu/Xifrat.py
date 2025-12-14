separador = 5
TextoSeparado = []
listaABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
lista2 = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',' ']
lista3 = ['V','R','U','Q','O','T','S','P','N','X','Y','W','B','Z', 'A', 'E', 'C', 'D', 'F', 'G', 'K', 'J', 'M', 'H', 'L', 'I',' ']
listaNuevaPosicion = []


def Notches():
    notch2 = input("Introdueix el primer notch (A-Z): ").upper()
    notch3 = input("Introdueix el segon notch (A-Z): ").upper()
    
    Posicionamiento_de_notch(lista2, notch2)
    Posicionamiento_de_notch(lista3, notch3)


def xifrar():
    TextoDescifrar = input("Que vols xifrar: ")
    TextoNuevoDescifrar = TextoDescifrar.replace(" ", "").upper()
    contadorListas = 0
    listaNuevaPosicionFinal = []


    for i in range(0, len(TextoNuevoDescifrar), separador):
        separados = TextoNuevoDescifrar[i:i + separador]
        TextoSeparado.append(separados)

    TextoFinal = " ".join(TextoSeparado)

    TextoFinalUsuario = list(TextoFinal)


    for letra in TextoFinalUsuario:
        if letra not in listaABC:
            print("El text conte caracters no permesos")
            continue

        
        RotarLista(lista2)
        contadorListas += 1

            
        if contadorListas == len(listaABC):
            RotarLista(lista3)
            contadorListas = 0
            RotarLista(lista2)

    
        PosicionLetra = listaABC.index(letra)
        PosicionLetra = lista2[PosicionLetra]
        
        PosicionLetra2 = listaABC.index(PosicionLetra)
        PosicionLetra2 = lista3[PosicionLetra2]
        listaNuevaPosicion.append(PosicionLetra2)
       
          

    listaNuevaPosicionFinal = "".join(listaNuevaPosicion)


    escribeTexto(listaNuevaPosicionFinal)
    print("Text xifrat correctament")
    print("Text xifrat: ", listaNuevaPosicionFinal)     
     

def RotarLista(llista):
    llista.append(llista.pop(0))


def Posicionamiento_de_notch(listas, notch):
    while True:
        if listas[0] != notch:
            RotarLista(listas)
        else:
            break


def escribeTexto(listadeletras):
    archivo = open('Text.txt', 'w')
    archivo.write(listadeletras)


def desxifrar():
    print("Funcio desxifrar en construccio")