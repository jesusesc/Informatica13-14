# -*- coding: utf-8 -*-
'''
Ejemplos de Entrada / Salida
'''
from math import pi

def circle_length(radius):
    return 2*pi*radius

def half(valor):
    return valor/2

def main():
    '''
    Lectura de datos desde el teclado: raw_input
    Debemos especificar qué tipo de datos queremos leer
    '''
    #Leemos el radio desde el teclado
    rad = float(raw_input())
    print circle_length(rad)

    #mejor: mensaje introductorio
    rad = float(raw_input("radio = "))
    print circle_length(rad)

def main2():
    #Cuidado con qué quieres leer
    x = raw_input("dato = ")
    y = int(raw_input("dato = "))
    z = float(raw_input("dato = "))

    #print mitad(x), mitad(y), mitad(z)
    print half(y), half(z)

def main3():
    #mejorando print
    r = float(raw_input("radius = "))
    print "The circle length is", circle_length(r)
    #puede mostrar distintos mensajes separados por comas
    #otra forma
    print "The circle length is", 
    print circle_length(r)

def main4():
    #SALIDA CON FORMATO
    n = int(raw_input("n = "))
    #presentamos por pantalla sin ningún tipo de formato
    for k in range(2, 11):
        print n, "elevado a", k, "es igual a", n**k
    print '='*10
    #presentamos por pantalla utilizando un formato de salida
    for k in range(2, 11):
        print '%d elevado a %d es igual a %d' % (n, k, n**k)
    print '='*10

    '''
    %<numero>d --> formato enteros
    %<numero1.numero2>f --> formato flotantes
    %s --> cadenas
    '''
    #Con un buen formato, mejoramos la presentación
    for k in range(2, 11):
        print '%d elevado a %2d es igual a %9d' % (n, k, n**k)
    print '='*10
    #Podemos mezclar reales y enteros
    for k in range(1, 10):
        print 'la circunferencia de radio %d tiene longitud %f' % (k, circle_length(k))
    print '='*10
    
    for k in range(1, 10):
        print 'la circunferencia de radio %d tiene longitud %5.1f' % (k, circle_length(k))
    print '='*10

    for k in range(1, 10):
        r = 1.0/k
        print 'la circunferencia de radio %4.2f tiene longitud %5.1f' % (r, circle_length(r))
