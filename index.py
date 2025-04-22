# Trabajo Práctico Integración Nº1

#Conversión de Número binario a decimal y viceversa. 

#Se solicita al usuario que eliga la opción de conversión
option = int(input("Elige la opción deseada: \n 1: Conversión de número binario a decimal. \n 2: Conversión de número decimal a binario. \n\n"))

#Conversión de binario a decimal
if option == 1:
    #Se solicita número binario
    binario = int(input("Ingrese el número binario a convertir: \n"))
    position = 0
    decimal = 0

    while binario > 0:
        #extrae el ultimo dígito
        num = binario % 10
        #quita del número el ultimo dígito, para que el while no sea infinito.
        binario //= 10
        #operación de multiplicación y suma a decimal
        decimal += num * (2 ** position)
        #suma la posición
        position += 1

    print(f"El número convertido a decimal es: {decimal}")
#Conversión de decimal a binario
elif option == 2:
    #Se solicita número decimal
    decimal = int(input("Ingrese el número decimal a convertir: \n"))
    position = 0  
    binario = 0


    while decimal / 2 > 0:
        #calcular el resto 
        resto = decimal % 2
        #operacion de suma y multiplicacion para armar num binario
        binario += resto * (10 ** position)
        #divide el decimal por base binaria
        decimal //= 2
        #suma la posición
        position += 1 

    print(f"El número convertido a binario es: {binario}")



