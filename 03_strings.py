### Strings ### 

my_string = "Mi string"
my_other_string = 'Mi otro String'

print (len(my_string))
print (len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print (my_new_line_string )

my_tab_string = "\tEste es un String con tabulacion"
print (my_tab_string )

my_scape_string = "\\tEste es un String con \\n escapado"
print (my_scape_string )

## Formateo

name, surname, age = "Jean Marco","Pacha", 25

print ("Mi nombre es {}{} y mi edad es {}".format(name, surname, age))
print ("Mi nombre es %s %s y mi edad es %d"%(name, surname, age))
print (f"Mi nombre es {name} {surname} y mi edad es {age}")
#print ("Mi nombre es " + " " + {surname} + " y mi edad es " + str(age))


# Desempaquetado de carateres 
language = "Python"
a,b,c,d,e,f = language
print(a)
print(e)


#Division

language_slice = language[1:3]
print (language_slice)

language_slice = language[1:]
print (language_slice)

language_slice = language[-2]
print (language_slice)

language_slice = language[0:6:2]
print (language_slice)

# Reverse

reversed_language = language[::-1]
print (reversed_language)

# Funciones

print( language.capitalize())
print( language.upper()) # poner mayusculas
print( language.count("t")) # contar
print( language.isnumeric()) # es un numero
print( "1".isnumeric()) 
print( language.lower()) # minusculas
print( language.upper().isupper()) # transformacion de izquierda a derecha

