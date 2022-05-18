#Ingresar dos números y realizar todas las operaciones aritméticas

num1= float(input('Ingrese un valor: '))
num2= float(input('Ingrese un valor: '))

#Operaciones Aritmeticas
#suma
suma = num1 + num2
#resta
resta = num1 - num2
#multiplicacion
mult = num1 * num2
#division
div= num1 / num2
#potencia
pot= num1 ** num2
print('El resultado de la suma es:  {} ' .format(suma))
print('El resultado de la resta es:  {} ' .format(resta))
print('El resultado de la multiplicación es:  {} ' .format(mult))
print('El resultado de la division es:  {} ' .format(div))
print('El resultado de la potenciación es:  {} ' .format(pot))