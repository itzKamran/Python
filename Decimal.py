# Decimal To Hex,Bin,Oc
A = (int(input("Enter A Decimal")))
B = bin(A)
C = oct(A)
D = hex(A)

print ("Binary Conversation ",B)
print ("Octal Conversation ",C)
print ("Hexadecimal Conversation",)

#solve logic second
num = int(input ("Enter A Decimal"))
if(num<=2):
    print("Binary Conversation ",bin(num))
elif(num <= 8):
    print("Octal Conversion ",oct(num))
elif(num <= 16):
  print("Hexa Conversation:", hex(num))
