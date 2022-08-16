
from itertools import count
from re import A
import time


#print("calculo de Horas")
#print("")
#nombre= input("Digite  ")

#NUMERO1= int(input ("digiste la cantida de hora trabajada= "))

#while  NUMERO1 == 0:
  #  NUMERO1= int(input ("digiste la cantida de hora trabajada= "\n))
#NUMERO2= int(input("digiste el precio por hora= "\n))

#SUMA=NUMERO1 *  NUMERO2
#print(nombre,"Tiene un total de  ",SUMA,"De hora trabajada")

#numeroSecreto = 777
#numero = int(input("Digite un numero entero"))

#while numero !=numeroSecreto:
    
 #   print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
  #  numero = int(input("Digite un numero entero"))

#print("usted Adivino la carta")
#for i in range (2, 9):
 #   print("El valor de i es actualmente", i)

  
# Indicar al usuario que ingrese una palabra
palabra =  input("Digite una palabra ")
palabra = palabra.upper()
# y asignarlo a la variable userWord.

for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or  letra == "O"  or letra == "U":
        continue
    else:
        time.sleep(1)

    print(letra)
    
    
    # Completa el cuerpo del ciclo for.j