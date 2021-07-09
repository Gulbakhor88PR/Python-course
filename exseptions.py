    
#Exceptions

try:
    x = int(input("1-son: "))
    y = int(input("2-son: "))  
    print(x / y)

except:
    print("xatolik bor, yana urinib ko‘ring: ")


#Exceptions-1.
try:
    x = int(input("1-son: "))
    y = int(input("2-son: "))  
    print(x / y)

except ZeroDivisionError:
    print("sonni nolga bo‘lib bo‘lmaydi!")

except ValueError:
    print("sonni TEXTga bo‘lib bo‘lmaydi!")




#Exceptions-2.
try:
    x = int(input("1-son: "))
    y = int(input("2-son: "))  
    print(x - y)


except ValueError:
    print("sondan TEXTni ayirib bo‘lmaydi!")




 