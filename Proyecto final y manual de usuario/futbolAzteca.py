import random
#Variables globales
#Equipos disponibles
equipos= ["Manchester City", "Manchester United", "Real Madrid", "FC Barcelona", "Liverpool FC", "Juventus"]
#Jugadores disponibles
jugadores= ["Diego Armando Maradona",
"Lionel Messi", "Pelé", "Johan Cruyff", "Cristiano Ronaldo", "Alfredo Di Stefano", "Franz Beckenbauer", "Zinedine Zidane", "Ferenc Puskas", "Ronaldo Nazario", "Garrincha", "Michel Platini", "Marco van Basten", "George Best", "Franco Baresi", "Zico", "Gerd Muller", "Giuseppe Meazza", "Bobby Charlton", "Paolo Maldini", "Romario", "Lev Yashin", "Eusebio", "Ronaldinho", "Carlos Alberto", "Valentino Mazzola", "Bobby Moore", "Socrates", "Raymond Kopa", "Lothar Matthaus", "José Manuel Moreno", "Paolo Rossi", "Gunter Netzer", "Stanley Matthews", "Luis Suárez", "Paco Gento", "Ruud Gullit", "Gianni Rivera", "Nandor Hidegkuti", "Kenny Dalglish", "Gianluigi Buffon", "Matthias Sindelar", "Fritz Walter", "Didí", "Oleg Blokhin", "Juan Alberto Schiaffino", "Roberto Rivellino", "Michael Laudrup", "Nilton Santos", "Xavi Hernández", "Jairzinho", "Roberto Baggio", "Gaetano Scirea", "Gunnar Nordahl", "Dino Zoff", "Daniel Passarella", "Karl-Heinz Rummenigge", "Adolfo Pedernera", "Andrés Iniesta", "Kevin Keegan", "Peter Schmeichel", "Dixie Dean", "Gordon Banks", "Johan Neeskens", "Jimmy Johnstone", "Teófilo Cubillas", "Florian Albert", "Samdro Mazzola", "Dennis Bergkamp", "Paul Breitner", "John Charles", "José Andrade", "Omar Sivori", "Josef Masopust", "Cafú", "Denis Law", "Frank Rijkaard", "Just Fontaine", "Gigi Riva", "Thierry Henry", "Dragan Dzajic", "Hugo Sánchez", "Ryan Giggs", "Giacinto Facchetti", "Uwe Seeler", "Gabriel Batistuta", "Javier Zanetti", "Allan Simonsen", "Hristo Stoichkov", "Roberto Carlos", "Sepp Maier", "Sandor Kocsis", "Philipp Lahm", "Zlatan Ibrahimovic", "Djalma Santos", "Obdulio Varela", "Neymar", "Mario Kempes", "Mario Coluna", "Gheorghe Hagi", "Falcao García", "James Rodrigues"]
#Posiciones disponibles
posiciones= ["Portero", 
"Carrilero", "Líbero", "Central", "Lateral", "Pivote", "Interior", "Volante", "Segundo Delantero", "Delantero Centro", "Tercer delantero", "Portero", "Central", "Lateral", "Volante", "Delantero Centro", "Pivote"]
#partidos para cada equipo en cada jornada. Cada número representa a un equipo, el número 1 será el equipo principal elejido por el usuario, el resto de números se asigna según el orden de creación de cada equipo secundario.
listaPartidos= [[1, 2], [3, 4], [5, 6]], [[1, 6], [2, 4], [3, 5]], [[1, 5], [2, 3], [4, 6]], [[1, 3], [2, 6], [4, 5]], [[1, 4], [2, 5], [3, 6]]
#Datos iniciales del campeonato       
diccionarioCampeonato= {"fecha" : 1, "campeon": False, "jornadas": {}, "equiposSecundarios": {}, "equipoPrincipal": {}}#En este diccionario se irá guardando TODA la información del campeonato separa da por secciones
#CREANDO LA CLASE
class futbolAzteca:
    def __init__(self):
        self.menuInicial()

    def menuInicial(self):
        opcion= 1
        while opcion!=0:
            opcion= int (input("\n"+"="*45+" FUTBOL  AZTECA "+"="*45+"\n"+
                "\n1. Iniciar un campeonato. \n"+
				"0. Salir del programa\n\n-> "))
            print("="*106)
            if 0<=opcion<=1:
                if opcion==1:
                    #Creando los equipos y jugadores.    
                    self.crearEquipos()
                    #Este bucle le asignará un equipo a cada número en la listaPartidos. 
                    for i in range(5):
                        diccionarioCampeonato["jornadas"][str(i+1)]= []
                        numero= int(diccionarioCampeonato["equipoPrincipal"]["numeroEquipo"])
                        nombre= str(diccionarioCampeonato["equipoPrincipal"]["nombre"])
         
                        for j in listaPartidos[i]:
                            
                            j= [nombre if index== numero else index for index in j]
                            
                            for k in diccionarioCampeonato["equiposSecundarios"]:
                                nombre= str(diccionarioCampeonato["equiposSecundarios"][k]["nombre"])
                                numero= int(diccionarioCampeonato["equiposSecundarios"][k]["numeroEquipo"])
                                j= [nombre if index== numero else index for index in j]
                            
                            diccionarioCampeonato["jornadas"][str(i+1)].append(j)
                        
                        #este bucle va a agregar un -1 al final de cada lista de partidos.
                        #el -1 indica que no se ha jugado el partido
                        #el 0 indica que el partido quedó empatado
                        #si hay otro número significa que ganó el equipo al que le corresponda tal número
                        for l in range (3):    
                            diccionarioCampeonato["jornadas"][str(i+1)][l].append(-1)
                    
                    #Despliegue del menú principal del campeonato
                    self.menuPrincipal()

            else:
                print("Opción no válida\n")

    def menuPrincipal(self):
        Match= False
        x= 1
        while x!=0:
            #Resultado del partido del equipo principal en la jornada
            if Match== True:
                print("\n"+("=")*40+" CAMPEONATO FUTBOL AZTECA "+("=")*40
                ,"\n\nEquipo principal:", diccionarioCampeonato["equipoPrincipal"]["nombre"], " "*(32-len(diccionarioCampeonato["equipoPrincipal"]["nombre"])), "|", end= " ")

                if diccionarioCampeonato["fecha"]<=5:
                    rPartido= diccionarioCampeonato["jornadas"][str(diccionarioCampeonato["fecha"]-1)][0][2]
                else:
                    rPartido= diccionarioCampeonato["jornadas"]["5"][0][2]

                if rPartido== diccionarioCampeonato["equipoPrincipal"]["nombre"]:
                    print ((" ")*4+"Tu equipo ha GANADO en la jornada #"+ str(diccionarioCampeonato["fecha"]-1))
                elif rPartido== -1:
                    print((" ")*4+"Tu equipo ha EMPATADO en la jornada #"+ str(diccionarioCampeonato["fecha"]-1))
                else: 
                    print((" ")*4+"Tu equipo ha PERDIDO en la jornada #"+ str(diccionarioCampeonato["fecha"]-1))
                
                print("\n"+"="*106+"\n1. Terminar el campeonato") if diccionarioCampeonato["fecha"]>5 else print("\n"+"="*106+"\n1. Avanzar a la siguiente jornada")
                
                x=int(input("2. Mostrar la tabla de posiciones.\n"+
                "3. Mostar la tabla de goleadores.\n"+
                "4. Mostrar todos los resultados de la jornada.\n\n-> "))
                
                if 1<=x<=4:
                    if x== 1:
                        if diccionarioCampeonato["fecha"]>5:
                            Match= True
                            x= 0
                        else:
                            x=6
                    elif x== 2:
                        x= 3
                    elif x== 3:
                        x= 4
                    elif x== 4:
                        x= 5
                    print("="*106)
                else:
                    x=7
            #caso en el que aún no se haya jugado el partido
            elif Match== False:
                partido= diccionarioCampeonato["jornadas"][str(diccionarioCampeonato["fecha"])]
                #Este print muestra los partidos que se disputarán en la jorada
                print("\n"+("=")*40+" CAMPEONATO FUTBOLAZTECA "+("=")*41
                ,"\n\nEquipo principal: ", diccionarioCampeonato["equipoPrincipal"]["nombre"]
                ,"\n\nJornada", diccionarioCampeonato["fecha"]
                ,":\n12:00", partido[0][:-1]
                ,"\n14:00", partido[1][:-1]
                ,"\n16:00", partido[2][:-1],"\n")
                #Menú que se muestra antes de comenzar el partido    
                if diccionarioCampeonato["fecha"]>1:
                    x= int(input("="*106+"\n1. Jugar partido\n"+
                    "2. Administar equipo\n"+"3. Mostrar la tabla de posiciones de la jornada anterior\n"+
                    "4. Mostar la tabla de goleadores de la jornada anterior\n"+
                    "5. Mostrar resultados de la jornada anterior\n"+
                    "0. Terminar campeonato"+
                    "-> "))  
                else:
                    x= int(input("="*106+"\n1. Jugar partido\n"+
                    "2. Administar equipo\n\n-> "))
                    print("="*106)
                    if x > 2:
                        x= 7

            if 0<=x<=6:
                if x==1:
                    self.jugarPartido()
                    Match= True
                if x==2:
                    self.menuAdministrarEquipo()
                if x==3:
                    self.mostrarTablaDePosiciones()
                if x==4:
                    self.mostrarTablaDeGoleadores()
                if x==5:
                    self.mostrarResultadosJornada()
                if x==6:
                    Match= False
                if x==0:
                    print("\nEL CAMPEONATO DE FUTBOL AZTECA HA FINALIZADO     ", end="")
                    print("|   FELICIDADES TU EQUIPO HA QUEDADO CAMPEÓN!") if diccionarioCampeonato["campeon"] else print("   |    Tu equipo no ha quedado campeón")
            else:
                print("\nOpción no válida\n")
    #Esta opción estará dispoible antes de jugarse un partido.
    def menuAdministrarEquipo(self):
        opcion=1
        while opcion!=0:
            opcion= int(input("\n"+"="*44+"ADMINISTRAR EQUIPO"+"="*44+"\n"+
				"1. Ver jugadores y sus posiciones. \n"+
				"2. Cambiar de posición un jugador.\n"+
				"3. Sustituir jugador.\n"+
				"4. Elejir un nuevo capitan.\n"+
				"0. Volver al menú principal.\n\n-> "))
            print("="*106)
            if 0<=opcion<=4:
                if opcion==1:
                    self.verJugadores()
                if opcion==2:
                    self.cambiarPosiciones()
                if opcion==3:
                    self.sustituirJugador()
                if opcion==4:
                    self.cambiarCapitan()
            else:
                print("Opción no válida\n")
    #Los equipos y sus jugadores son asignados aleatoriamente, el ususario solo debe seleccionar al equipo principal
    def crearEquipos(self):
        equiposDisponibles= equipos.copy()
        jugadoresDisponibles= jugadores.copy()

        #creación de los equipos
        for i in range(6):
            diccionarioJugadores={}
            #equipo principal
            if i==0:
                validacion= False
                while validacion== False:
                    #elección del equipo principal
                    nEquipo= int(input("\n¿Con qué equipo desea jugar?\n"+ "\n0."+ equiposDisponibles[0]+ "\n1."+ equiposDisponibles[1]+ "\n2."+ equiposDisponibles[2]+ "\n3."+ equiposDisponibles[3]+ "\n4."+ equiposDisponibles[4]+ "\n5."+ equiposDisponibles[5]+ "\n\n-> "))
                    #Validación para que no lance error
                    if 0<=nEquipo<=5:
                        diccionarioCampeonato["equipoPrincipal"]["nombre"]= equiposDisponibles[nEquipo]
                        diccionarioCampeonato["equipoPrincipal"]["estadoEquipo"]= "Descansando"
                        diccionarioCampeonato["equipoPrincipal"]["numeroEquipo"]= i+1
                        #el número representa la jornada. ejp: "1" = jornada #1.
                        diccionarioCampeonato["equipoPrincipal"]["estadisticas"]= {}
                        equipo= diccionarioCampeonato["equipoPrincipal"]["estadisticas"]
                        for i in range(1, 6):
                            equipo[str(i)]= {}
                            equipo[str(i)]["partidosJugados"]= 0    
                            equipo[str(i)]["partidosGanados"]= 0
                            equipo[str(i)]["partidosPerdidos"]= 0
                            equipo[str(i)]["partidosEmpatados"]= 0
                            equipo[str(i)]["golesAFavor"]= 0
                            equipo[str(i)]["golesEnContra"]= 0
                            equipo[str(i)]["puntos"]= 0

                        #bucle para añadir los jugadores al equipo con la función random
                        for z in range(17):
                            x= random.randint(0, (len(jugadoresDisponibles)-1))
                            diccionarioJugadores[(jugadoresDisponibles[x])]= {}
                            jugador= diccionarioJugadores[(jugadoresDisponibles[x])]
                            jugador["posicion"]= posiciones[z]
                            jugador["nombre"]= jugadoresDisponibles[x]
                            jugador["dorsal"]= str(z+1)
                            if z<11: 
                                jugador["estado"]= "Titular"
                            else:
                                jugador["estado"]= "Suplente"
                            if z==0:
                                jugador["capitan"]= True
                            else:
                                jugador["capitan"]= False
                            jugador["asistencias"]= 0
                            jugador["goles"]= {}
                            goles= jugador["goles"]
                            goles["cabeza"]= 0
                            goles["penalti"]= 0
                            goles["tiroLibre"]= 0
                            goles["totalGoles"]= 0
                            jugadoresDisponibles.pop(x)

                        diccionarioCampeonato["equipoPrincipal"]["jugadores"]= diccionarioJugadores
                        equiposDisponibles.pop(nEquipo)
                        validacion= True
                    else:
                        print("\nopción no válida")
            #resto de los equipos
            else:
                diccionarioEquipo= {}
                diccionarioEquipo["nombre"]= equiposDisponibles[0]
                diccionarioEquipo["estadoEquipo"]= "Descansando"
                diccionarioEquipo["numeroEquipo"]= i+1
                #el número representa la jornada. ejp: "1" = jornada #1.
                diccionarioEquipo["estadisticas"]= {}
                equipo= diccionarioEquipo["estadisticas"]
                for i in range(1, 8):
                    equipo[str(i)]= {}
                    equipo[str(i)]["partidosJugados"]= 0    
                    equipo[str(i)]["partidosGanados"]= 0
                    equipo[str(i)]["partidosPerdidos"]= 0
                    equipo[str(i)]["partidosEmpatados"]= 0
                    equipo[str(i)]["golesAFavor"]= 0
                    equipo[str(i)]["golesEnContra"]= 0
                    equipo[str(i)]["puntos"]= 0

                for i in range(17):
                    x= random.randint(0, (len(jugadoresDisponibles)-1))
                    diccionarioJugadores[(jugadoresDisponibles[x])]= {}
                    jugador= diccionarioJugadores[(jugadoresDisponibles[x])]
                    diccionarioJugadores[(jugadoresDisponibles[x])]["posicion"]= posiciones[i]
                    diccionarioJugadores[(jugadoresDisponibles[x])]["nombre"]= jugadoresDisponibles[x]
                    diccionarioJugadores[(jugadoresDisponibles[x])]["dorsal"]= i+1
                    if i<11:
                        diccionarioJugadores[(jugadoresDisponibles[x])]["estado"]= "Titular"
                    else:
                        diccionarioJugadores[(jugadoresDisponibles[x])]["estado"]= "Suplente"
                    if i==0:
                        diccionarioJugadores[(jugadoresDisponibles[x])]["capitan"]= True
                    else:
                        diccionarioJugadores[(jugadoresDisponibles[x])]["capitan"]= False 
                    jugador["asistencias"]= 0
                    jugador["goles"]= {}
                    goles= jugador["goles"]
                    goles["cabeza"]= 0
                    goles["penalti"]= 0
                    goles["tiroLibre"]= 0
                    goles["totalGoles"]= 0
                    jugadoresDisponibles.pop(x)

                diccionarioEquipo["jugadores"]= diccionarioJugadores
                diccionarioCampeonato["equiposSecundarios"][equiposDisponibles[0]]={}
                diccionarioCampeonato["equiposSecundarios"][equiposDisponibles[0]]= diccionarioEquipo
                equiposDisponibles.pop(0)
    
    #formato de lista de jugadores : [1]-> dorsal, "neymar"-> nombre, (delantero centro)-> posición en el campo, [=C=]-> capitán
    def verJugadores(self):

        titular= []
        suplente= []
        print("\nTitulares:                                                    Suplentes: \n")   
		
        for i in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:
            #acceso directo al jugador en la posición i
            jugador= diccionarioCampeonato["equipoPrincipal"]["jugadores"][i]
            if jugador["estado"]=="Titular":
                if jugador["capitan"]:
                    titular.append("["+str(jugador["dorsal"])+"] "+str(jugador["nombre"])+" ("+str(jugador["posicion"])+")"+"[=C=]")
                else:   
                    titular.append("["+str(jugador["dorsal"])+"] "+str(jugador["nombre"])+" ("+str(jugador["posicion"])+")")
					
            else:
                suplente.append("["+str(jugador["dorsal"])+"] "+str(jugador["nombre"])+" ("+str(jugador["posicion"])+")")
        #bucle para imprimir la lista de suplentes y titulares
        for i in range(6):
            t=titular.pop(0)
            if len(t) < 47:
                jugador= 47-len(t)
                for i in range(jugador):
                    t+= " "
                print(t, "             ",suplente.pop(0))

        for i in range(len(titular)):    
            print(titular[i])

    def cambiarPosiciones(self):
        self.verJugadores()
        nombre= input("\n¿Qué Jugador desea cambiar de posición? (Pede poner el nombre o el número del dorsal)\n->")

        for i in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:
                
            jugador= diccionarioCampeonato["equipoPrincipal"]["jugadores"][i]

            if nombre== jugador["dorsal"] or nombre== jugador["nombre"]: 
                
                posicion= int(input("\nElija la nueva posición del jugador:\n\n1. portero\n2. carrilero\n3. Líbero\n4. Central\n5. Lateral\n6. Pivote\n7. Interior\n8. Volante\n9. Segundo delantero\n10. Delantero centro\n11. Tercer delantero\n-> "))

                if 0<=posicion<=11:
                    jugador["posicion"]= "Portero" if posicion==1 else "Carrilero" if posicion==2 else "Líbero" if posicion==3 else "Central" if posicion==4 else "Lateral" if posicion==5 else "Pivote" if posicion==6 else "Interior" if posicion==7 else "Volante" if posicion==8 else "Segundo delantero" if posicion==9 else "Delantero centro" if posicion==10 else "Tercer delantero" if posicion==11 else jugador["posicion"]
                    print("\nSe ha cambiado la posicón del jugador!")

                else:
                    print("\nNo se ha cambiado la posición del jugador.")

    def sustituirJugador(self):
        self.verJugadores()

        titular= input("\n¿Qué Jugador titular va a sustituir? (Puede poner el nombre o el número del dorsal)\n-> ")
        for i in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:

            jugadorI= diccionarioCampeonato["equipoPrincipal"]["jugadores"][i]

            if (titular== jugadorI["dorsal"] or titular== jugadorI["nombre"]) and jugadorI["estado"]== "Titular":

                suplente= input("\n¿Qué jugador suplente va a ingresar? (Puede poner el nombre o el número del dorsal)\n-> ")

                for j in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:

                    jugadorJ= diccionarioCampeonato["equipoPrincipal"]["jugadores"][j]

                    if jugadorJ["dorsal"]== suplente or jugadorJ["nombre"]== suplente:
                        if jugadorJ["posicion"]== "Portero":
                            jugadorJ["capitan"]= True
                            jugadorJ["estado"]= "Titular"
                        else:
                            jugadorJ["estado"]= "Titular"

                        if jugadorI["capitan"]:
                            jugadorI["capitan"]= False
                            jugadorI["estado"]= "Suplente"
                        else:
                            jugadorI["estado"]= "Suplente"

                        print("\nEl jugador", "[", jugadorI["dorsal"], "] ", jugadorI["nombre"], "ha sido sustituido por ", "[", jugadorJ["dorsal"], "] ", jugadorJ["nombre"])

    def cambiarCapitan(self):
        self.verJugadores()
        capitan= input("\n¿Qué Jugador va a ser el nuevo capitan? (Puede poner el nombre o el número del dorsal)\n-> ")
        for i in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:
            jugador= diccionarioCampeonato["equipoPrincipal"]["jugadores"][i]
            
            if jugador["capitan"]== True:
                jugador["capitan"]= False

            if capitan== jugador["dorsal"] or capitan== jugador["nombre"]:
                jugador["capitan"]= True
                print("\nEl jugador", "[", jugador["dorsal"], "]", jugador["nombre"], "ahora es el capitán!")

    def cambiarEstadoEquipo(self):
        diccionarioCampeonato["equipoPrincipal"]["estadoEquipo"]= "Jugando"
        if diccionarioCampeonato["equipoPrincipal"]["estadoEquipo"]== "Jugando":
            print("El equipo ahora está JUGANDO!")
        else: 
            print("El equipo ahora está DESCANSANDO")

    def mostrarTablaDePosiciones(self):
        #fecha en la que va el campeonato
        fecha= diccionarioCampeonato["fecha"] if diccionarioCampeonato["fecha"]<= 5 else 5
        
        #lista para saber la posición en la tabla de cada equipo
        printList= []
        print("\nEquipo                     |Partidos  |Partidos  |Partidos  |Partidos  |Goles     |Goles     |Puntos")
        print("                           |jugados   |ganados   |perdidos  |empatados |a favor   |en contra |")
        print("---------------------------|----------|----------|----------|----------|----------|----------|-------")
        
        #proceso para obtener las estadísticas del equipo principal

        #Este será un acceso directo al nombre del equipo principal guardado en el diccionarioCampeonato
        equipo= diccionarioCampeonato["equipoPrincipal"]["nombre"]
        #Este es un acceso directo a las estadisticas del equipo principal según la fecha guardada en el diccionarioCampeoato
        estadisticas= diccionarioCampeonato["equipoPrincipal"]["estadisticas"][str(fecha)]

        printEquipo=str(equipo)+(" "*(24-(len(str(equipo)))))+"|"
        
        for i in estadisticas:
            if i != "puntos":
                printEquipo+= " "+str(estadisticas[i])+(" "*(9-(len(str(estadisticas[i])))))+"|"
            else: 
                printEquipo+= " "+str(estadisticas[i])
            
        printList.append(printEquipo)

        #proceso para obtener las estadísticas de los demás equipos
        for i in diccionarioCampeonato["equiposSecundarios"]:
            #Este será un acceso directo al nombre del equipo secundario guardado en el diccionarioCampeonato
            equipo= diccionarioCampeonato["equiposSecundarios"][i]["nombre"]
            #Este es un acceso directo a las estadisticas del equipo secundario según la fecha guardada en el diccionarioCampeoato 
            estadisticas= diccionarioCampeonato["equiposSecundarios"][i]["estadisticas"][str(fecha)]
            
            #Este será el string (por equipo) que se va a imprimir en la tabla de posiciones 
            printEquipo=str(equipo)+(" "*(24-(len(str(equipo)))))+"|"
        
            for j in estadisticas:
                if j != "puntos":
                    printEquipo+= " "+str(estadisticas[j])+(" "*(9-(len(str(estadisticas[j])))))+"|"
                else: 
                    printEquipo+= " "+str(estadisticas[j])

            #Este for acomodará a los equipos de menor a mayor según la cantidad de puntos obtenidos
            for k in range(len(printList)):
                if int(estadisticas["puntos"]) > int(printList[k][-2:]):
                    if k==len(printList)-1:
                        printList.append(printEquipo)
                        break

                elif int(estadisticas["puntos"]) <= int(printList[k][-2:]):
                        printList.insert(k, printEquipo)
                        break

        #Este for imprime la tabla de posiciones
        for k in range (1, len(printList)+1):
            print(str(k)+".", printList[-k])
            if fecha>=5 and k ==1:
                diccionarioCampeonato["campeon"]= True if printList[-k][:17]== diccionarioCampeonato["equipoPrincipal"]["nombre"] else False
                print(printList[-k][:17], diccionarioCampeonato["campeon"])
             
    def mostrarTablaDeGoleadores(self):
        #lista para saber la posición en la tabla de cada jugador
        printList= []
        print("\nJugador                    |Equipo                 |Asistencias     |Goles           |Goles           |Goles de        |Total")
        print("                           |                       |                |de cabeza       |de penalti      |tiro libre      |de goles")
        print("---------------------------|-----------------------|----------------|----------------|----------------|----------------|---------")

        cont= 0
        for i in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:
            jugador= diccionarioCampeonato["equipoPrincipal"]["jugadores"][i]
            equipo= diccionarioCampeonato["equipoPrincipal"]["nombre"]
            goles= diccionarioCampeonato["equipoPrincipal"]["jugadores"][i]["goles"]

            printJugador= str(jugador["nombre"])+(" "*(24-(len(str(jugador["nombre"])))))+"| "+str(equipo)+(" "*(22-(len(str(equipo)))))+"| "+str(jugador["asistencias"])+(" "*(15-(len(str(jugador["asistencias"])))))+"| "+str(goles["cabeza"])+(" "*(15-(len(str(goles["cabeza"])))))+"| "+str(goles["penalti"])+(" "*(15-(len(str(goles["penalti"])))))+"| "+str(goles["tiroLibre"])+(" "*(15-(len(str(goles["tiroLibre"])))))+"| "+str(goles["totalGoles"])

            if cont== 0:
                printList.append(printJugador)
                cont+=1
            
            else:
                for j in range(len(printList)):
                    if int(goles["totalGoles"]) > int(printList[j][-2:]):
                        if j==len(printList)-1:
                            printList.append(printJugador)
                            break

                    if int(goles["totalGoles"]) <= int(printList[j][-2:]):
                            printList.insert(j, printJugador)
                            break

        for i in diccionarioCampeonato["equiposSecundarios"]:
            for j in diccionarioCampeonato["equiposSecundarios"][i]["jugadores"]:
                jugador= diccionarioCampeonato["equiposSecundarios"][i]["jugadores"][j]
                equipo= diccionarioCampeonato["equiposSecundarios"][i]["nombre"]
                goles= jugador["goles"]

                printJugador= str(jugador["nombre"])+(" "*(24-(len(str(jugador["nombre"])))))+"| "+str(equipo)+(" "*(22-(len(str(equipo)))))+"| "+str(jugador["asistencias"])+(" "*(15-(len(str(jugador["asistencias"])))))+"| "+str(goles["cabeza"])+(" "*(15-(len(str(goles["cabeza"])))))+"| "+str(goles["penalti"])+(" "*(15-(len(str(goles["penalti"])))))+"| "+str(goles["tiroLibre"])+(" "*(15-(len(str(goles["tiroLibre"])))))+"| "+str(goles["totalGoles"])

                for k in range(len(printList)):
                    if int(goles["totalGoles"]) > int(printList[k][-2:]):
                        if k==len(printList)-1:
                            printList.append(printJugador)
                            break

                    if int(goles["totalGoles"]) <= int(printList[k][-2:]):
                            printList.insert(k, printJugador)
                            break
        
        for i in range (1, 10):
            print(str(i)+".", printList[-i])

    def jugarPartido(self):
        #Lista de los goles disponibles para asiganar a cada delantero
        listaDeGoles= ["cabeza", "penalti", "tiroLibre"]
        validation= False
        while validation== False:    
            opc= int(input("\n¿Qué desea hacer?\n1. Resultados aleatorios\n2. Ingresar los resultados de la fecha\n\n-> "))
            #rellenado de los datos para los 3 partidos de la jornada
            if 1<=opc<=2:    
                for i in range(3):
                    #rellenado automático y manual de las estadisticas para el equipo principal y su rival en la fecha jugada
                    if i==0:    
                        partido= diccionarioCampeonato["jornadas"][str(diccionarioCampeonato["fecha"])][i]

                        resultado= partido[random.randint(0, 2)] if opc== 1 else int(input("\n"+"="*100+"\n"+str(partido[:-1])+"\n\nIngrese el resultado del partido # "+ str(i+1)+":\n\n1. GANA el "+str(partido[0])+"\n2. GANA el "+str(partido[1])+"\n3. Hay EMPATE\n-> "))

                        resultado= partido[0] if (resultado== 1 and opc== 2) else partido[1] if (resultado== 2 and opc== 2) else -1 if (resultado== 3 and opc== 2) else resultado

                        equipoPrin= diccionarioCampeonato["equipoPrincipal"]["nombre"]

                        equipoSec= partido[1]

                        partido[2]= resultado

                        #variable que serán los goles a favor para el equipo ganador y goles en contra para el perdedor
                        gfGanador= random.randint(1,5) if opc== 1 else int(input(" "*100+"\n"+"Ingrese el marcador:\n\n"+str(resultado)+": ")) if opc== 2 and resultado != -1 else None
                        #lista de delanteros del equipo principal
                        listaDelanterosPrin= []
                        #bucle para agregar a los delanteros titulares a la lista del equipo principal
                        for h in diccionarioCampeonato["equipoPrincipal"]["jugadores"]:
                            #accseo directo a los jugadores del equipo principal
                            jugadorPrin= diccionarioCampeonato["equipoPrincipal"]["jugadores"][h]
                            if jugadorPrin["estado"]== "Titular": 
                                if jugadorPrin["posicion"]== "Segundo Delantero" or jugadorPrin["posicion"]== "Delantero Centro" or jugadorPrin["posicion"]== "Tercer delantero":
                                    listaDelanterosPrin.append(jugadorPrin)
                        #variable que serán los goles en contra para el equipo ganador y goles a favor para el equipo perdedor
                        gfPerdedor= random.randint(0, gfGanador-1) if opc== 1 else int(input(str(partido[0])+": ")) if opc== 2 and partido[0]!= resultado and resultado!= -1 else int(input(str(partido[1])+": ")) if opc==2 and partido[1] != resultado and resultado != -1 else None
                        #lista de  delansteros de CADA EQUIPO SECUNDARIO
                        listaDelanterosSec= []
                        #bucle para agregar a los delanteros titulares a la lista del equipo secundario    
                        for l in diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"]:
                            #acceso directo a los jugadores del los demas equipos secundarios  
                            jugadorSec= diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][l]
                            if jugadorSec["estado"]== "Titular": 
                                if jugadorSec["posicion"]== "Segundo Delantero" or jugadorSec["posicion"]== "Delantero Centro" or jugadorSec["posicion"]== "Tercer delantero":
                                    listaDelanterosSec.append(jugadorSec)
                        
                        #caso en el que el equipo principal gana     
                        if resultado== equipoPrin:
                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (gfGanador):
                                jugador= listaDelanterosPrin[random.randint(0, (len(listaDelanterosPrin)-1))]
                                diccionarioCampeonato["equipoPrincipal"]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equipoPrincipal"]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1

                            #bucle para asignarla a un jugador al azar de la lista de delanteros, cada gol anotado en el partido por el equipo perdedor
                            for k in range (gfPerdedor):
                                #elige un jugador al azar de la lista de delanteros del equipo
                                jugador= listaDelanterosSec[random.randint(0, len(listaDelanterosSec)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1

                            for j in range (diccionarioCampeonato["fecha"], 6):                      
                                #Rellenado de las estadisticassd del equipo principal
                                
                                #acceso directo a las estadisticas del equipo princpal
                                estadisticas= diccionarioCampeonato["equipoPrincipal"]["estadisticas"][str(j)]
                                estadisticas["partidosJugados"]+=1
                                estadisticas["partidosGanados"]+=1
                                estadisticas["golesAFavor"]+= gfGanador
                                estadisticas["golesEnContra"]+= gfPerdedor
                                estadisticas["puntos"]+=3

                                #rellenado de las estadisticas del equipo secundario

                                #acceso directo a las estadisticas del equipo secundario
                                estadisticasSec= diccionarioCampeonato["equiposSecundarios"][equipoSec]["estadisticas"][str(j)]
                                estadisticasSec["partidosJugados"]+=1
                                estadisticasSec["partidosPerdidos"]+=1
                                estadisticasSec["golesAFavor"]+=gfPerdedor
                                estadisticasSec["golesEnContra"]+= gfGanador
                        
                        #caso en el que el equipo principal pierde
                        elif resultado== equipoSec:
                            #bucle para asignarla a un jugador al azar de la lista de delanteros, cada gol anotado en el partido por el equipo perdedor
                            for k in range (gfPerdedor):
                                jugador= listaDelanterosPrin[random.randint(0, len(listaDelanterosPrin)-1)]
                                diccionarioCampeonato["equipoPrincipal"]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equipoPrincipal"]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1
                            
                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (gfGanador):
                                #elige un jugador al azar de la lista de delanteros del equipo
                                jugador= listaDelanterosSec[random.randint(0, len(listaDelanterosSec)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1
                            
                            for j in range (diccionarioCampeonato["fecha"], 6):                   
                                #acceso directo a las estadisticas del equipo secundario
                                estadisticasSec= diccionarioCampeonato["equiposSecundarios"][equipoSec]["estadisticas"][str(j)]
                                #acceso directo a las estadisticas del equipo princpal
                                estadisticas= diccionarioCampeonato["equipoPrincipal"]["estadisticas"][str(j)]
                                estadisticas["partidosJugados"]+=1
                                estadisticas["partidosPerdidos"]+=1
                                estadisticas["golesAFavor"]+= gfPerdedor
                                estadisticas["golesEnContra"]+= gfGanador

                                estadisticasSec["partidosJugados"]+=1
                                estadisticasSec["partidosGanados"]+=1
                                estadisticasSec["golesAFavor"]+= gfGanador
                                estadisticasSec["golesEnContra"]+= gfPerdedor 
                                estadisticasSec["puntos"]+= 3
                        #caso en el que el equipo principal empata
                        else:
                            goles= random.randint(0, 5) if opc== 1 else int(input("\nIngrese el número de goles para ambos equipos:\n->")) if opc== 2 and resultado== -1 else None

                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (goles):
                                jugador= listaDelanterosPrin[random.randint(0, len(listaDelanterosPrin)-1)]
                                diccionarioCampeonato["equipoPrincipal"]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equipoPrincipal"]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1
                            
                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (goles):
                                #elige un jugador al azar de la lista de delanteros del equipo
                                jugador= listaDelanterosSec[random.randint(0, len(listaDelanterosSec)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipoSec]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1
                            
                            #Bucle para rellenar las estadisticas de cada fecha
                            for j in range (diccionarioCampeonato["fecha"], 6):   
                                #acceso directo a las estadisticas del equipo secundario
                                estadisticasSec= diccionarioCampeonato["equiposSecundarios"][equipoSec]["estadisticas"][str(j)]
                                #acceso directo a las estadisticas del equipo princpal
                                estadisticas= diccionarioCampeonato["equipoPrincipal"]["estadisticas"][str(j)]                
                                estadisticas["partidosJugados"]+=1
                                estadisticas["partidosEmpatados"]+=1
                                estadisticas["golesAFavor"]+= goles
                                estadisticas["golesEnContra"]+= goles
                                estadisticas["puntos"]+=1

                                estadisticasSec["partidosJugados"]+=1
                                estadisticasSec["partidosEmpatados"]+=1
                                estadisticasSec["golesAFavor"]+= goles
                                estadisticasSec["golesEnContra"]+= goles 
                                estadisticasSec["puntos"]+= 1
                    #rellenado automático y manual de las estadisticas para el resto de los equipos en la fecha jugada
                    else:
                        partido= diccionarioCampeonato["jornadas"][str(diccionarioCampeonato["fecha"])][i]

                        resultado= partido[random.randint(0, 2)] if opc== 1 else int(input("\n"+"="*100+"\n"+str(partido[:-1])+"\n\nIngrese el resultado del partido #"+str(i+1)+":\n\n1. GANA el "+str(partido[0])+"\n2. GANA el "+str(partido[1])+"\n3. Hay EMPATE\n-> "))

                        resultado= partido[0] if resultado== 1 and opc!= 1 else partido[1] if resultado== 2 and opc!= 1 else -1 if resultado== 3 and opc!= 1 else resultado

                        #asignación del equipo #1
                        equipo1= partido[0]

                        #asignación del equipo #2
                        equipo2= partido[1]

                        #variable que serán los goles a favor para el equipo ganador y goles en contra para el perdedor
                        gfGanador= random.randint(1,5) if opc== 1 else int(input("\nIngrese el marcador:\n\n"+str(resultado)+": ")) if (opc== 2 and resultado != -1) else None
                        #lista de delanteros del equipo #1
                        listaDelanterosE1= []
                        #bucle para agregar a los delanteros titulares a la lista del equipo #1
                        for l in diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"]:
                            #accseo directo a los jugadores del equipo #1
                            jugadorE1= diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][l]
                            if jugadorE1["estado"]== "Titular": 
                                if jugadorE1["posicion"]== "Segundo Delantero" or jugadorE1["posicion"]== "Delantero Centro" or jugadorE1["posicion"]== "Tercer delantero":
                                    listaDelanterosE1.append(jugadorE1)                
                        
                        #variable que serán los goles en contra para el equipo ganador y goles a favor para el equipo perdedor
                        gfPerdedor= random.randint(0, gfGanador-1) if opc== 1 else int(input(str(partido[0])+": ")) if opc== 2 and partido[0]!= resultado and resultado!= -1 else int(input(str(partido[1])+": ")) if opc== 2 and partido[1]!= resultado and resultado!= -1 else None 
                        #lista de delanteros del equipo #2
                        listaDelanterosE2= []
                        #bucle para agregar a los delanteros titulares a la lista del equipo #2
                        for m in diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"]:
                            #accseo directo a los jugadores del equipo #2
                            jugadorE2= diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][m]
                            if jugadorE2["estado"]== "Titular": 
                                if jugadorE2["posicion"]== "Segundo Delantero" or jugadorE2["posicion"]== "Delantero Centro" or jugadorE2["posicion"]== "Tercer delantero":
                                    listaDelanterosE2.append(jugadorE2)
                        
                        #caso en el que el equipo #1 gana     
                        if resultado== equipo1:
                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (gfGanador):
                                jugador= listaDelanterosE1[random.randint(0, len(listaDelanterosE1)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+= 1
                                diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1
                            
                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (gfPerdedor):
                                jugador= listaDelanterosE2[random.randint(0, len(listaDelanterosE2)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1

                            for j in range (diccionarioCampeonato["fecha"], 6):                      
                                #acceso directo a las estadisticas del equipo #1
                                estadisticas1= diccionarioCampeonato["equiposSecundarios"][equipo1]["estadisticas"][str(j)]
                                #acceso directo a las estadisticas del equipo #2
                                estadisticas2= diccionarioCampeonato["equiposSecundarios"][equipo2]["estadisticas"][str(j)]
                                
                                estadisticas1["partidosJugados"]+=1
                                estadisticas1["partidosGanados"]+=1
                                estadisticas1["golesAFavor"]+= gfGanador
                                estadisticas1["golesEnContra"]+= gfPerdedor
                                estadisticas1["puntos"]+=3
                                
                                estadisticas2["partidosJugados"]+=1
                                estadisticas2["partidosPerdidos"]+=1
                                estadisticas2["golesAFavor"]+=gfPerdedor
                                estadisticas2["golesEnContra"]+= gfGanador
                        
                        #caso en el que el equipo #2 gana
                        elif resultado== equipo2:
                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (gfGanador):
                                jugador= listaDelanterosE2[random.randint(0, len(listaDelanterosE2)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1

                            #bucle para asignarle a un jugador al azar de la lista de delanteros, cada gol anotado en el partido
                            for k in range (gfPerdedor):
                                jugador= listaDelanterosE1[random.randint(0, len(listaDelanterosE1)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1

                            for j in range (diccionarioCampeonato["fecha"], 6):                   
                                #acceso directo a las estadisticas del equipo #1
                                estadisticas1= diccionarioCampeonato["equiposSecundarios"][equipo1]["estadisticas"][str(j)]
                                #acceso directo a las estadisticas del equipo #2
                                estadisticas2= diccionarioCampeonato["equiposSecundarios"][equipo2]["estadisticas"][str(j)]
                                
                                estadisticas2["partidosJugados"]+=1
                                estadisticas2["partidosGanados"]+=1
                                estadisticas2["golesAFavor"]+= gfGanador
                                estadisticas2["golesEnContra"]+= gfPerdedor 
                                estadisticas2["puntos"]+= 3
                                
                                estadisticas1["partidosJugados"]+=1
                                estadisticas1["partidosPerdidos"]+=1
                                estadisticas1["golesAFavor"]+= gfPerdedor
                                estadisticas1["golesEnContra"]+= gfGanador

                        #caso en el que hay empate
                        else:
                            goles= random.randint(0, 5) if opc== 1 else int(input("\nIngrese el número de goles para ambos equipos:\n->")) if opc== 2 and resultado== -1 else None

                            for k in range (goles):
                                jugador= listaDelanterosE1[random.randint(0, len(listaDelanterosE1)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipo1]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1
                            
                            for k in range (goles):
                                jugador= listaDelanterosE2[random.randint(0, len(listaDelanterosE2)-1)]
                                diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][jugador["nombre"]]["goles"]["totalGoles"]+=1
                                diccionarioCampeonato["equiposSecundarios"][equipo2]["jugadores"][jugador["nombre"]]["goles"][listaDeGoles[random.randint(0,2)]]+= 1

                            for j in range (diccionarioCampeonato["fecha"], 6):   
                                #acceso directo a las estadisticas del equipo #1
                                estadisticas1= diccionarioCampeonato["equiposSecundarios"][equipo1]["estadisticas"][str(j)]
                                #acceso directo a las estadisticas del equipo #2
                                estadisticas2= diccionarioCampeonato["equiposSecundarios"][equipo2]["estadisticas"][str(j)]                
                                
                                estadisticas1["partidosJugados"]+=1
                                estadisticas1["partidosEmpatados"]+=1
                                estadisticas1["golesAFavor"]+= goles
                                estadisticas1["golesEnContra"]+= goles
                                estadisticas1["puntos"]+=1
                                
                                estadisticas2["partidosJugados"]+=1
                                estadisticas2["partidosEmpatados"]+=1
                                estadisticas2["golesAFavor"]+= goles
                                estadisticas2["golesEnContra"]+= goles 
                                estadisticas2["puntos"]+= 1
                
                if diccionarioCampeonato["fecha"]<= 5:
                    diccionarioCampeonato["fecha"]+=1
                validation= True
            else:
                print("\nOpción no válida")
    
    def mostrarResultadosJornada(self):
        fecha= diccionarioCampeonato["fecha"]-1 if diccionarioCampeonato["fecha"]< 5 else 5 

        for i in range(3):    
            equipo1= diccionarioCampeonato["jornadas"][str(fecha)][i][0]
            equipo2= diccionarioCampeonato["jornadas"][str(fecha)][i][1]
            estadisticasP= diccionarioCampeonato["equipoPrincipal"]["estadisticas"]
            estadisticasE1= diccionarioCampeonato["equiposSecundarios"][equipo1]["estadisticas"] if equipo1 != diccionarioCampeonato["equipoPrincipal"]["nombre"] else estadisticasP
            estadisticasE2= diccionarioCampeonato["equiposSecundarios"][equipo2]["estadisticas"]

            if fecha != 1:    
                r1= estadisticasP[str(fecha)]["golesAFavor"] - estadisticasP[str(fecha-1)]["golesAFavor"] if equipo1== diccionarioCampeonato["equipoPrincipal"]["nombre"] else estadisticasE1[str(fecha)]["golesAFavor"] - estadisticasE1[str(fecha-1)]["golesAFavor"]

                r2= estadisticasE2[str(fecha)]["golesAFavor"] - estadisticasE2[str(fecha-1)]["golesAFavor"]
            else:
                r1= estadisticasP[str(fecha)]["golesAFavor"] if equipo1== diccionarioCampeonato["equipoPrincipal"]["nombre"] else estadisticasE1[str(fecha)]["golesAFavor"]

                r2= estadisticasE2[str(fecha)]["golesAFavor"]
        
        
            print("\n"
                 +"|-----------------------------------------------------------------|")
            print("|", equipo1," "*(25-len(equipo1)), "|", r1,"¦", r2, "|", " "*(25-len(equipo2)), equipo2, "|")
            print("|-----------------------------------------------------------------|")

futbolAzteca()