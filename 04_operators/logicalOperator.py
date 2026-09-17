# There are 3 types of logical operator
# and   - Return True if both condition are True
# or    - Return True if at least one condition is True
# not   - Reverse the boolean value

print(123 == 100 and 34 == 34) #-False  #Agar first wala false ho gya toh aage read nhi karega  
print(123 == 100 and 34 == 34 and 35 != 36) #True
print(123 == 100 or 34 == 34) #-True #kam se kam ek condition true honi chahiye  
 
print(not 34 == 34) #-False #ye True ko False & False ko True me convert kar deta hai          



# exercise
print((456 == 456)!=(235 ==236)) # True
print(12<10 or 45==56 or 69>70 or 15 !=13) #true
print(True and bool(0))         #False
print(True and bool(1))         # True