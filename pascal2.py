n = int(input("enter no:"))
pasc = 0
no=n
for i in range(0,n):
    pasc = 11**i
    j=no;
    while int(j/2) >0 :
        print(" ",end="")
        j-=1
    no-=1
    
    
    convpasc = str(pasc)
    print(" ".join(convpasc))
    
    
