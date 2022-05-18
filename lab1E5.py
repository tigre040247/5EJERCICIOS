opcion = float (input('***Menú***\n1 Cálculo de longitud a metros \n2 Cálculo de longitud a kilometros \n Escoja la opción a calcular: ' ))
if opcion ==1:
    print('------------------------------')
    centimetros= float(input('Ingrese la cantidad de la longitud en centímetros: '))
    metros= centimetros * 0.01
    print('Los ', centimetros, ' centímetros equivalen a : ', metros, ' metros')
elif opcion ==2:
    print('------------------------------')
    cent= float (input('Ingrese la cantidad de la longitud en centímetros: '))
    kilometros = cent * 0.00001 
    print('Los ', cent, ' centímetros equivalen a : ', kilometros, ' kilometros')
else: 
    print('Ingrese una opcion valida.')

