print(0//2)
numbers= range(1,1001)
coins=[]
for a in numbers :
    if (a/15).is_integer() == True :
        a= a*10
    elif (a/5).is_integer() == True :
        a= a*3
    elif (a/3).is_integer() == True :
        a= a*2
    else :
        a= a*1    
    coins.append(a)

print(sum(coins))