### Tuples ###

my_tuple = tuple()
my_other_tuple =()

my_tuple = (25, 1.67, "Jean Marco","Pacha", "Quispe", "Quispe")
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4])  IndexError
#print(my_tuple[-6])  IndexError


print(my_tuple.count("Quispe"))
print(my_tuple.index("Pacha"))
print(my_tuple.index("Quispe"))


my_tuple[1]= 1.80 
print(my_tuple)


