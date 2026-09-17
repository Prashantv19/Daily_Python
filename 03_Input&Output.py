#OUTPUT
# name = "Prashant"
# age = 23
# print (name, age)

#formated string = f"My name is {name} and I am {age} years old."

# print(f"my name is {name} and I am {age} years old.")

#INPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))        #iska default data type string hota hai.
print(f"my name is {name} and i am {age} years old.") 

print(type(age))  #<class 'str'> aayega by default

#so we have to do type conversion to convert string to int


num = input("Type Your Age: ")
print(f"age: {num}")