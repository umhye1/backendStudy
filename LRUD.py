num = int(input())
a_list = list(input().split())

# #동 북 서 남
# #행 기준, 열 이동
# dx = [0,-1,0,1]
# #열 기준, 행 이동
# dy = [1,0,-1,0] 

x,y=1,1

for i in range(int(len(a_list))):
    if a_list[i] == "L" and y-1>0:
        y = y-1
    elif a_list[i] == "R" and y+1<=num:
        y = y+1
    elif a_list[i] == "U" and x-1>0 :
        x = x-1
    elif a_list[i] == "D" and x+1<=num :
        x = x+1
    else :
        continue

print(x,y)