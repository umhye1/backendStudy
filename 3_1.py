# 3. dfs / bfs
# 음료수 얼려 먹기 - dfs

graph = []
count = 0

n,m = map(int,input().split())
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    if graph[x][y]==0:
        graph[x][y] = 1
        dfs(x-1, y)     #상
        dfs(x, y-1)     #하
        dfs(x+1, y)     #좌
        dfs(x, y+1)     #우
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)
    