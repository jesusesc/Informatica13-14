# -*- coding: utf-8 -*-

'''
Distintas rotaciones de un alfabeto
'''

def rotacion1(caracter):
    '''
    Rotación de longitud 1
    '''

    if ('A'<=caracter) and (caracter <= 'Z'): #Es una letra mayúscula
        if (caracter < 'Z'):
            caracter = chr(ord(caracter)+1)
        else:
            caracter = 'A'
    return caracter

def rotacion_n01(caracter, n):
    '''
    Rotación de longitud n
    Versión 1
    '''

    if ('A' <= caracter) and (caracter <= 'Z'): #Es una letra mayúscula
        dim = ord('Z') - ord('A') + 1
        n = n % dim #elimino las vueltas sobrantes
        if (ord(caracter) + n <= ord('Z')):
            caracter = chr(ord(caracter) + n)
        else:
            caracter = chr (ord(caracter) + n - dim)
    return caracter



     
def rotacion_n02(caracter, n):
    '''
    Rotación de longitud n
    Versión 2
    '''

    if ('A' <= caracter) and (caracter <= 'Z'): #Es una letra mayúscula
        dim = ord('Z') - ord('A') + 1
        caracter = chr(ord('A') + ((ord(caracter) - ord('A')) + n) % dim)
    return caracter



def test(n):
    for i in range(ord('A'), ord('Z')+1):
        print chr(i), rotacion1(chr(i)), rotacion_n01(chr(i), n), rotacion_n02(chr(i), n)


def codifica(cadena, n):
    '''
    Codifica la cadena rotando el alfabeto n posiciones
    '''
    s = ''
    i = 0
    while i < len(cadena):
        c = rotacion_n02(cadena[i], n)
        s = s + c
        i += 1
    return s

def main():
    cadena = raw_input('Cadena a codificar = ')
    n = int(raw_input('rotacion = '))
    print codifica(cadena, n)

