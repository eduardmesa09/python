huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}


#imprime el diccionario huespedes
print (huespedes)
#imprime cada item del diccionario junto con su valor dentro de una lista  
print (huespedes.items())
#imprie solo las llaves del diccionario
print (huespedes.keys())
#imprime cada llave del diccionario por separado
for key in huespedes:
    print (key)
#imprime solo los valores del diccionario dentro de una lista
print (huespedes.values())
#imprime los valores de cada llave por separado
for key in huespedes:
    print (huespedes[key])
#imprime un salto de linea
print()
#en cada ciclo, imprime la llave, :, y el valor de la llave
for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion])
#imprime un salto de linea
print()
#en cada ciclo imprime la llave, :, el valor de la ultima llave
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huespedes[key])
#en cada ciclo imprime el número del índice, la llave, :, el valor de la llave
for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key])
#imprime un salto de linea
print()
#imprime el valor de la llave 105
print (huespedes[105])
print (huespedes.get(105))
#imprime una secuencia de =
print ('====================================')
#crea una nueva llave llamada 102 con el valor "Fanny lu"
huespedes[102]='Fanny Lu'
#crea una nueva llave llamada 107 con el valor "Don omar"
huespedes[107]='Don Omar'
#vuelve "109" la llave por defecto
huespedes.setdefault('109','Luis Miguel')
#en cada ciclo imprime la llave, :, el valor de la llave
for huesped in huespedes.items():
    print (habitacion,':',huesped)
print()
#crea un nuevo diccionario llamado registroshoy
registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
#agrega registroshoy al diccionario huespedes
huespedes.update(registroshoy)
#en cada ciclo imprime la llave, : el valor de la llave
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped)
print("xxxxxx")

print ('====================================')
#cambia el valor de la llave 107 por Ricky Martin
huespedes[107]='Ricky Martin'
#imprime el diccionario 
print (huespedes)

print ('====================================')

#elimina la llave 102
del huespedes[102]
#elimina la llave 202
huespedes.pop(202)
#imprime el diccionario
print(huespedes)

print ('====================================')
#crea una copia de el diccionario huespedes llamada copia1
copia1=huespedes.copy()
#imprime copia 1
print ('copia1: ',copia1)
#crea un diccionario vácio llamado copia2
copia2={}
#agrega todos los valores de huespedes a copia2 .
copia2.update(huespedes)
#imprime copia2 
print ("copia2: ",copia2)

print ('====================================xxx')
#crea una arreglo llamada lista
lista=[2,5,7,1]
#crea un ciccionario llamado diccio, donde las llaves son los items en lista, y el valor de cada llave es "xxx" 
diccio=dict.fromkeys(lista,"xxx")
#imprime diccio
print(diccio)

print ('====================================')
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)
inventario["cartera"].sort()
print(inventario)
inventario["cartera"].remove("Monedas")
print(inventario)
print(inventario.get("plata")[0])
