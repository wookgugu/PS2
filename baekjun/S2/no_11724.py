# 연결 요소의 개수
# 방향 없는 그래프가 주어졌을 때, 
# 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
# 첫째 줄에 연결 요소의 개수를 출력한다.

N, M = map(int, input().split())
graph = [[]*(N+1)for _ in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

print(graph)