##n = int(input("Enter the number of the last term:"))

n = 10

def F() :
    n1, n2, n3 = 0,1,1
    while True:
        yield n1
        n1 , n2 , n3 = n2 , n3, n1 + n2 + n3

for i , f in zip(range(1,n+1) , F()):
    if i%10 == 0:
        print(i ,"th number" , ":" , f)
    elif i%10 == 1 and i != 11:
        print(i ,"st number" , ":" , f)
    elif i%10 == 2 and i != 12:
        print(i ,"nd number" , ":" , f)
    elif i%10 == 3 and i != 13:
        print(i ,"rd number" , ":" , f)
    else:
        print(i ,"th number" , ":" , f)

F(n)       
##print(input("Press enter to exit.",))
