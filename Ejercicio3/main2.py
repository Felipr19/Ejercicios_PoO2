from unidad import *

a=int(input("1.decimal \n2.binario \n3.hexal \n4.octal"))
    
if a == 1:
    contador = Unidad()
elif a == 2:
    contador = binario()
elif a == 3:
    contador = hexal()
elif a == 4:
    contador = octal()
else:
    print("no es una opcion valida")
    
if 1<=a<=4:
    n=int(input("hasta cuanto quieres contar?(introducir valor decimal)"))
    for i in range(n):
        contador.avanzar()
        print(contador.valor)
        
