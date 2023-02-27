### Lists ### 

my_list = list()
my_other_list = []

print (len(my_list))

my_list =[35, 14 ,40,25,62,30,30,17]

print(my_list)
print(len(my_list)) # contar 

my_other_list = [25, 1.67, "Jean Marco","Pacha"]
print(type(my_other_list))
print(type(my_list))

# Acceso a elementos y busqueda

print(my_other_list[-1]) 
print(my_other_list[0]) # Empezamos en 0 
print(my_other_list[2]) 
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count("Pacha")) # para ver cuantas veces se repite
print(my_list.count(30))

#print(my_other_list[-5])
#print(my_other_list[4])

print(my_other_list.index("Pacha"))

age, height, name , surname = my_other_list
print(name)
name , age, height, surname = my_other_list[2], my_other_list[0], my_other_list[1], my_other_list[3]
print(name)

# Concatenacion

print(my_list+ my_other_list)
#print(my_list- my_other_list)

# Creacion , insercion, actualizacion y eliminacion

my_other_list.append("Madara") # añadir al final
print(my_other_list)

my_other_list.insert(1,"Cafe")  # añadir segun la posicon, valor
print(my_other_list)


my_other_list[1]= "expresso"
print(my_other_list)

my_other_list.remove("expresso") #eliminar valor que encuentra
print(my_other_list)



my_list.remove(30) # elimina solo el primero 

print(my_list)
print(my_list.pop()) # elimina por defecto el ultima, pero puedes ponerle un indice
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element) # eliminar el indice
print(my_list) 


del my_list[2] # eliminar por indice
print(my_list)

#Operaciones con listas 

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)


my_new_list.reverse() # poner la lista de reversed
print(my_new_list)


my_new_list.sort() # ordenacion de  menor a mayor
print(my_new_list)

# sublistas

print(my_new_list[1:3])

# Cambio de tipo 

my_list = "Hola Python"
print(my_list)
print(type(my_list))




