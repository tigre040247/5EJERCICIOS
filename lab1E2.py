#Ingresar un valor en libras y transformarlo a kilos y gramos


libra= float(input('Ingrese el valor en libras: '))

kilogramo = libra / 2.2046
print('EL valor en kilogramos es:  {} ' .format(kilogramo))

gramo= libra * 453.592
print('EL valor en gramos es:  {} ' .format(gramo))