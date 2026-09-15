#Int -> String
a = 23
print(type(a), a)
a = str(a)
print(type(a), a)

#String -> Int
b = "23" 
print(type(b), b)
b = int(b)
print(type(b), b)


c = "abc"
#we can not convert string to int if it does not contain numbers
#c = int(c) #ValueError: invalid literal for int() with base 10


d = 10
d = bool(d) #true
print(type(d), d)
# there are only 7 falsy values that means only 7 things will be converted to false rest True. 

# type conversion
# implicit type conversion (type coercion) -> python automatically converts one data type to another data type when we perform operations on different data types.
#ex.
e = 6
print(e/2) #3.0 implicitly converts it into float.

# explicit type conversion (type casting) -> we can manually convert one data type to another data type using built-in functions like int(), str(), float(), bool() etc.
 