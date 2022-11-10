#Punto rios
rios= {"Danubio": "Alemania", "Rin": "Suiza", "Sena": "Francia", "Volga": "Rusia", "Ebro": "España"}

#a
for i in rios:
    print("• El rio", i, "recorre a", rios[i], "")

#b
print("\nLista de rios:\n")
for i in rios:
    print("•", i)

#c
print("\nLista de paises:\n")
for i in rios:
    print("•", rios[i])


#Punto Glosario
glosario= {"Bucle": "Un bucle es una secuencia que repite varias veces un mismo trozo de código, hasta que la condición asignada al bucle deja de cumplirse.",

"Arreglo": "es una colección ordenada de datos. Los arreglos se emplean para almacenar multiples valores en una sola variable.", 

"Variable": "Una variable es donde se almacenan y se recuperan los datos de un programa.", 

"Función": "Una función es un bloque de código que realiza alguna operación. Una función puede definir opcionalmente parámetros de entrada que permiten a los llamadores pasar argumentos a la función. Una función también puede devolver un valor como salida.", 

"librería": "Las librerías son trozos de código hechas por terceros. Esto nos facilita mucho la programación y hace que nuestro programa sea más sencillo de hacer y luego de entender."}

print("\nLista de significados\n")
for i in glosario:
    print("•", i, ":\n", glosario[i], "\n")