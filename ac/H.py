import sys
from collections import defaultdict

def solve(n, edges):
    g =defaultdict(list)
    edge_id_map ={}

    for edge_id, u, v in edges:
        g[u].append((v,edge_id))
        g[v].append((u,edge_id))
        edge_id_map[(min(u, v), max(u, v), edge_id)] = edge_id  

    tin = [-1]*n
    low = [-1]*n
    visited =[False]*n
    bridges= set()
    timer =[0]

    def dfs(u, parent_edge_id, parent=-1):
        visited[u] = True
        tin[u] =low[u]=timer[0]
        timer[0]+=1

        for v, edge_id in g[u]:
            if edge_id ==parent_edge_id:
                continue 

            if visited[v]:  
                low[u]=min(low[u], tin[v])
            else:
                dfs(v, edge_id, u)
                low[u]=min(low[u], low[v])

                if low[v]>tin[u]:
                    bridges.add(edge_id)

    dfs(0, -1)

    if not bridges:
        print("-1")
    else:
        print("\n".join(map(str, sorted(bridges)))) 

def main():
    input_data = sys.stdin.read().splitlines()
    n, m = map(int, input_data[0].split())
    edges =[tuple(map(int, line.split())) for line in input_data[1:]]
    solve(n, edges)

if __name__ == "__main__":
    main()
