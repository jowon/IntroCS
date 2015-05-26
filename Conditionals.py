#Conditionals Key-Words
# if (argument) 
    #action
# else 
    #action

# if (argument1) 
    #action
# elif (argument2)
    #action
# elif (argument3)
    #action
# else 
    #action 
    
#Operators for Conditionals
# Less Than : <
# Greater Than : >
# Equal : ==
# Not Equal : !=
# Less Than or Equal To : <=
# Greater Than or Equal To : >=

#Example
print "Bar"
age = input("What is the age of the customer? ")

if age >= 18: 
    print "The customer is legally allowed to drink liquor"
    print "You may serve"
else:
    print "The customer is NOT legally allowed to drink liquor"
    print "Do not serve this person alcohol"
