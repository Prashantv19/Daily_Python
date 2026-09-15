str = "prashant  12347890  @#$%^"
print(type(str))

a = "A"
print(ord(a)) #ord() function gives the ASCII value (Unicode) of "a" character (ex. A -> 65)

print(chr(65)) #chr() function gives the character of a ASCII value (ex. 65 -> A)

#indexing
#1. positive indexing  -> 0,1,2,3,4,5
#2. negative indexing  -> -1,-2,-3,-4,-5

b = "PRAS"
print(b[0]) #P
print(b[3]) #S

print(b[-1]) #S
print(b[-4]) #P

#Slicing
c = "PRASHANT"
print(c[0:5:1]) #PRASH   [start:stop:step]
print(c[0:5])   #PRASH   [start:stop]
print(c[0:7:2]) #PAHN
print(c[::2])   #PAHN
print(c[1::2])  #RSAT
print(c[1::]) #RASHANT
print(c[::]) #PRASHANT
#Note: stop value se ek kam tak result aayega, ex. 0:3 me 0,1,2 charactyer hi print hoga.
