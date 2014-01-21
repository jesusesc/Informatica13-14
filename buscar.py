# -*- coding: utf-8 -*-
'''
Diversas funciones para manejar listas
'''

def buscar(valor, lista):
    '''
    Busca el elemento 'valor' en la lista.
    Si está, devuelve su índice.
    Si no está, devuelve -1
    '''
    encontrado = False #bandera booleana
    i = 0
    while (not encontrado) and (i < len(lista)) :
        encontrado = (lista[i] == valor)
        print i, valor, lista[i] #traza de la ejecución
        i += 1
    if encontrado:
        return i - 1
    else:
        return -1

# creación de una lista aleatoria
def random_list(size):
    '''
    Creo una lista aleatoria de enteros de tamaño size
    '''
    from random import randint
    # randint(a, b) devuelve un entero aleatorio N, 
    #a <= N <= b
    data = []
    i = 0
    while i < size:
        data.append(randint(-10, 10))
        i += 1
    return data 
    
def main():
    '''
    Programa de prueba
    '''
    from random import randint    
    lista = random_list(20)
    print lista
    #buscamos un valor
    valor = randint(-10, 10)
    print 'Buscamos el valor', valor, 'en la lista'
    resultado = buscar(valor, lista)
    if resultado >= 0:
        print 'El valor', valor, 'esta en la posicion', resultado
    else:
        print 'El valor', valor, 'no esta en la lista'
      

