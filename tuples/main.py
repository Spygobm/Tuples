#creating tuple / packing tuple

address = ("57 pizzaroad","london","England","LO53ES")

#upacking tuple

area,city,country,postcode = address 

print(area,city,country,postcode)

#creating a tuple without parenthesis and diffirent data types

timetables = 20,40.5,"three",True

print(timetables)

#nested tuple

n_tuples = ("Hello",[7678,728,9],(True,87878,"w"))

print(n_tuples[1])
print(n_tuples[0])
print(n_tuples[1][1])
print(n_tuples[2][1])
print(n_tuples[0][4])

my_tuples = ("p","r","o","g","r","a","m","m","i","n","g")

#using slice opporator (slice opporator = :)

print(my_tuples[2:7])
print(my_tuples[4:])
print(my_tuples[:5])

my_tuples[2]="x"
#the main difference betwwen a list or tuple is that in lists you can replace or assighn