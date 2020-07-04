"""
    RETO 3: Diseña un programa que elimine de una lista todos los elementos de valor
    par y muestre por pantalla el resultado.
    (Ejemplo: si trabaja con la lista [1, -2, 1, -5, 0, 3], ésta pasará a ser [1, 1, -5, 3].)
"""

def oddNumbers(array): #saca los elementos impares
    oddArray = []

    for index in array:
        if index % 2 == 0: #si el residuo al dividirlo entre 2 es 0, es par
            continue
        else:
            oddArray.append(index)

    return oddArray


def main():
    array = [1, -2, 1, -5, 0, 3] #el array en el que quieres sacar los números impares
    
    oddArray = oddNumbers(array)
    print("\n\n the new array with odd numbers is: {} \n" .format(oddArray))

if __name__ == "__main__":
    main()