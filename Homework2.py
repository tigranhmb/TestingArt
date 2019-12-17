name='tigran'
lastname='Hambardzumyan'
test=name+lastname
for i, c in enumerate(test):
    print (i, c)
    #capitalize first letter
print(name.capitalize())
##returns true or false if all text is lowercase returns True if no returns false
print(lastname.islower())
#Returns true or false if all text is highercase returns true if no false
print(name.isupper())
##Replace name with other
replace=name.replace('tigran','Norayr')
print(replace, lastname)
## type everything with uppercase
Upper=name.upper()
print(Upper)
##lowercase all
print(lastname.lower())
##
