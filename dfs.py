#dfs 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i,visited)
    

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph =[
    [], #index 0
    [2,3,8], #index 1
    [1,7], #index 2
    [1,4,5], #index 3
    [3,5], #index 4
    [3,4], #index 5
    [7], #index 6
    [2,6,8], #index 7
    [1,7] #index 8
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 실행 결과 1 2 7 6 8 3 4 5 


