n = int(input())

a_list = list(input().split())
a_list.sort()

l = int(len(a_list))

count =0 

while l >0 :
    if len(a_list)==0:
        break
    
    m= max(a_list)
    if int(m)> n:
        break

    else:
        for i in range(int(m)):
            a_list.pop()
        count+=1
       

print(count)
