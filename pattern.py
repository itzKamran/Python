 #butterfly + inverte butterfly pattern
n = 4
for i in range(1,n+1):
    stars = "*"*i
    spaces = " "*2*(n-i)
    print(stars + spaces + stars)
for i in range(n,0,-1):
    stars = "*"*i
    spaces = " "*2*(n-i)
    print(stars + spaces + stars)
# ibnverte pyramid pattern 
n = 5
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

