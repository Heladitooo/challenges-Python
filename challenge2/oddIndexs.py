"""
    RETO 2: Diseña un programa que elimine de una lista todos los elementos de índice par 
    y muestre por pantalla el resultado.
    (Ejemplo: si trabaja con la lista [1,2,1,5,0,3], ésta pasará a ser [2,5,3].)
"""

def oddIndexs(array): #saca los índices impares, o sea no el número si no la posición en la que esta el número
    oddArray = []

    for i in range(len(array)):
        if i % 2 == 0: #si el residuo al dividirlo entre 2 es 0, es par
            continue
        else:
            oddArray.append(array[i])

    return oddArray


def main():
    array = [1,2,1,5,0,3] #el array en el que quieres sacar los índices impares
    
    oddArray = oddIndexs(array)
    print("\n\n the new array with odd indexs is: {} \n" .format(oddArray))

if __name__ == "__main__":
    main()