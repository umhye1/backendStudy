d = list(input())
dy = ord(d[0])-96
dx = int(d[1])
nx,ny,count = 0,0,0


#1. 수평으로 두 칸 이동 -> 수직 한 칸
if (dx+2)>0 and (dx+2)<9 :
    nx = dx + 2 

    if (dy+1)>0 and (dy+1)<9:
        ny = dy + 1
        count += 1

    if (dy-1)>0 and (dy-1)<9:
        ny = dy - 1
        count+=1
        
elif (dx-2)>0 and (dx-2)<9:
    nx = dx - 2 

    if (dy+1)>0 and (dy+1)<9:
        ny = dy + 1
        count += 1

    if (dy-1)>0 and (dy-1)<9:
        ny = dy - 1
        count += 1

#2. 수직으로 두 칸 이동 -> 수평 한 칸 
if (dy+2)>0 and (dy+2)<9 :
    ny = dy + 2

    if (dx+1)>0 and (dx+1)<9 :
        nx = dx + 1 
        count += 1
    
    if (dx-1)>0 and (dx-1)<9 :
        nx = dx - 1 
        count += 1

elif (dy-2)>0 and (dy-2)<9 :
    ny = dy - 2

    if (dx+1)>0 and (dx+1)<9 :
        nx = dx + 1 
        count += 1
    
    if (dx-1)>0 and (dx-1)<9 :
        nx = dx - 1 
        count += 1

print(count)

