#crea una nueva tupla llamada t
t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
#imprime t 
print (t)
#imprime el tamaño de t
print (len(t))


print ('=====================================')
#imprime t en la posición 0
print (t[0])
#imprime t en la posición 3
print (t[3])
#imprime t desde la posición 1 hasta la 3
print (t[1:3])
#imprime t en la posición 3(en la posición 1) 
print (t[3][1])


print ('====================================')
#imprime t en la posición 3
print (t[3])
#agrega "lorito" a la lista que está en la posición 3 en t
t[3].append('lorito')
#imprime 3
print (t)

print ('====================================')
#en cada ciclo imprime el elemnto iterador
for elemento in t:
    print (elemento)

print ('====================================')
#en cada ciclo imprime t en la posición del indice 
for index in range(0,len(t)):
    print (t[index])

print ('====================================')
#si "a" está en t imprime "El elemento 'a' esta en la tupla"
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")

print ('====================================')
#lista va a ser igual a t pero será un arreglo y no una tupla
lista=list(t)
#lista en la posición 1 igual a "A"
lista[1]='A'
#imprime lista
print (lista)
#tupla va a ser igual a lista pero será una tupla y no un arreglo
tupla=tuple(lista)
#imprime tupla
print (tupla)

print ('====================================')
#l igual a un arreglo con tuplas dentro
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
#imprime los valores de la lista l e el orden x, y
for x, y in l:
    print (x, ':', y)
