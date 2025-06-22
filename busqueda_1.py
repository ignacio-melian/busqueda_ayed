#Una de las tareas mas importantes es la localizacion de datos 
#el primer metodo de busqueda es el metodo lineal 
#vamos a definir donde almacenar nuestros datos, primero sera en una lista
datos = ['A', 'C', 'L', 'D', 'X', 'M', 'm', 'a', 'p', 'H', 'c', 'c'] #un detalle importante es que lo datos que tengo guardados en la que fuere mi estr es que no estan ordenados
                            #y puede ocurrir que esten repetidos
                        
#tengo que pedir un dato de busqueda y recorrer esa estructura determinando si el dato esta o no esta 
#entonces guardo dos variables
encontrado = False #por defecto falsa porque no se si el dato esta
posicion = 0 #corresponde la posicion en la que encontre el dato 
comparaciones = 0 #para saber el numero de comparaciones que hizo

#le pedimos al usuario que ingrese el valor a buscar
a_encontrar = input("ingrese el valor a encontrar -> ")

#el usuario me puede pasar cualquier cosa, por eso no se si no esta o esta en la lista 
#comienzo a buscar


###ENFOQUE1 RECORRE TODA LA LISTA AUNQUE YA HAYA ENCONTRADO EL ELEMENTO
#for dato in datos: #por cada uno de los valores que yo tenga en datos lo comparo con el valor a encontrar
   # comparaciones += 1 
    #if dato == a_encontrar:
     #   encontrado = True
      #  print(F"encontrado en posicion {posicion}")
    #posicion +=1 #si no lo encontro
#si no lo encotro solo ponemos eso

###ENFOQUE2 RECORRE LA LISAT Y CUANDO ENCUENTRA EL ELEMENTO SE DETIENE LA BUSQUEDA 
#for dato in datos: 
#    comparaciones += 1 
#    if dato == a_encontrar:
#        encontrado = True
#        print(F"encontrado en posicion {posicion}")
#        break #rompe el bucle 
#    posicion +=1

###ENFOQUE 3  BUSQUEDA UTILIZANDO INDICES
for i in range(0, len(datos)): #como la lista cambia de voluumen pongo la lingitudo de datos 
    comparaciones += 1 
    if datos[i] == a_encontrar: #cuando comparo cambio los datos por la anotacion del elemento de listas i
        encontrado = True
        print(F"encontrado en posicion {i}")
        break #rompe el bucle 
#la primera vez va a valer 0, 0 es < a len(datos) va a incrementar comparaciones y decir que el dato que esta en la posicion i es igual
#a lo qye estoy buscando? si es asi actualizo encontrado, imprimo la posicoin en la que esta 


if not encontrado:
    print("el dato buscado no se encontro")

print(F"cantidad de comparaciones {comparaciones}") #comparo todas las posibilidades por mas que el dato era el primero 
#recorre todos porque mi lista no esta ordenada 