#user 3 greatest num

A = int(input("Enter a num 1:"))
B = int(input("Enter a num 2:"))
C = int(input("Enter a num 3:"))

if( A >= B and A >=C ):
 print("First is largest :",A)
elif(B>=C):
 print("second is largest :",B)
else:
 print("Third is largest :", C)