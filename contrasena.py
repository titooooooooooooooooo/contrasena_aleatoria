import random as rd

def generar_contrasena(cantidad):

    #Defino los caracteres aleatorios a utilizar
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    #Agrupo los caraceteres a utilizar
    caracteres = MAYUS + MINUS + NUMS + CHARS

    #Genero lista vacia para la nueva contraseña
    contrasena = []

    #Genero contraseña aleatoria
    for i in range(cantidad):
        caracter_random = rd.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    c_contrasena = int(input("Indica cuantos caracteres necesitas para la contraseña: "))
    contrasena = generar_contrasena(c_contrasena)
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run() 