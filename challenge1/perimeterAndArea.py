"""
    RETO: Diseña un programa que, 
    a partir del valor de los dos lados de un rectángulo (4 y 6 metros, respectivamente), muestre el 
    valor de su perímetro (en metros) y el de su área (en metros cuadrados).
    (El perímetro debe darte 20 metros y el área 24 metros cuadrados.)

    Modifica el programa anterior de forma que el programa pueda recibir de un usuario el tamaño de los 
    lados del rectángulo como parámetros y pueda hacer los calculos para cualquier tipo de rectangulo.
"""

def whileInt(question): # crea un bucle si el usuario no tipea un numero entero o decimal
    value = input(question)
    try: 
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            print(" please enter only NUMBERS")
            print(" ")
            return whileInt(question) 


def calculatePerimeterAndArea(base,height): #calcula el perimetro y el area y lo retorna en un diccionario
    area = base * height
    perimeter = (base * 2) + (height * 2)

    return {
        "area": area,
        "perimeter": perimeter,
    }


def main():
    print(" ")
    print(" C A L C U L A T E  P E R I M E T E R  A N D  A R E A")
    print("                  - of a rectangle :D - \n\n\n")
      
    base = whileInt(" What is the base of your rectangle?: ")
    print(" ")
    height = whileInt(" Thanks ^^, now what is the height of your rectangle?: ")

    result = calculatePerimeterAndArea(base,height)

    print(" \n")
    print(" - calculated -")
    print("  area= {}m²" .format(result["area"]))
    print("  perimeter= {}m" .format(result["perimeter"]))
    print(" ")


if __name__ == "__main__":
    main()