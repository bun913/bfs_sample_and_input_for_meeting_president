"""
以下の形式で入力値が与えられる
N（頂点の数。今回は500で固定）
頂点の名前1
頂点の名前2
...
頂点の名前500(頂点の名前。今回は500個の名前が与えられるので、500行の入力がある)
M（辺の数。今回は800で固定。ここから辺で繋がっている頂点の情報が出力される）
辺で繋がっている頂点の要素番号 辺で繋がっている頂点の要素番号
...M個分どの頂点とどの頂点が辺で繋がっているか出力される
"""
from collections import deque

# 入力の受け取り
N = int(input())
names = [input() for _ in range(N)]  # 頂点の名前を500個受け取る
M = int(input())  # 辺の数を受け取る（今回は800で固定）
# グラフの生成
graphs = [[] for _ in range(N)]
for _ in range(M):
    # どの頂点同士が繋がっているか受け取る
    v1, v2 = map(int, input().split())
    # 辺で繋がっている頂点同士は互いに行き来ができるので双方向に繋げる
    graphs[v1].append(v2)
    graphs[v2].append(v1)

# 私の要素番号を取得（スタート地点）
start = names.index("私")
# 社長の要素番号を取得（ゴール地点）
goal = names.index("社長")
q = deque([start])
# 各頂点までの最短距離を管理する配列
dist_list = [-1] * N
dist_list[start] = 0
# 経路を復元するために、特定の頂点に辿り着く前にどの頂点を通ってきたかを記録する配列
prev_nodes = [-1] * N

while len(q) > 0:
    # 次に探索する頂点をキューから取り出す
    cur_node = q.popleft()
    # 次に探索する頂点がゴールなら終了
    if cur_node == goal:
        print("やっと会えましたね！ここまでくるのに{}人に紹介してもらいましたよ。".format(dist_list[cur_node]))
        break
    for next_node in graphs[cur_node]:
        # 距離が-1（初期値）ではないなら、すでに訪れている頂点なのでスキップ
        if dist_list[next_node] != -1:
            continue
        dist_list[next_node] = dist_list[cur_node] + 1
        prev_nodes[next_node] = cur_node
        q.append(next_node)
# 経路を復元する
route_list = []
cur_node = goal
while cur_node != start:
    route_list.append(cur_node)
    cur_node = prev_nodes[cur_node]
route_list.reverse()
print("ここまでの経路は")
for node in route_list:
    name = names[node]
    print(name)
print("です")

