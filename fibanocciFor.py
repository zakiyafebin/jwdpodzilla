def fibanocci(num):
    fib1 = 0
    fib2 = 1
    fibList = list()
    fibList.append(fib1)
    fibList.append(fib2)
    #print(fib1,fib2,end="  ")
    for i in range(2,num):
        fib3 = fib1 + fib2
        fibList.append(fib3)
        #print(fib3,end="  ")
        fib1 = fib2
        fib2 = fib3
    return fibList
        
        
n = int(input("Enter the num: "))
print(fibanocci(n))
