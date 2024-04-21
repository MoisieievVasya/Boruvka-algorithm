def find_set(parent, i):
    if parent[i] == i:
        return i
    return find_set(parent, parent[i])

def union_set(parent, rank, x, y):
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1