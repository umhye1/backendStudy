s = list(input())

result =1


for i in range(int(len(s))):

    if len(s)>20:
        break
    
    elif int(s[i-1]) == 0:
        result+=int(s[i])
    
    else :
        result*=int(s[i])

print(result)