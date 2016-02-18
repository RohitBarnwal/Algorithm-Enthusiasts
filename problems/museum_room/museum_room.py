def room_to_graph(room):
    g = {}
    n_row, n_col = len(room), len(room[0])
    for i in range(n_row):
        for j in range(n_col):
            if room[i][j] > 0:
                neighbors = []
                if i - 1 >= 0 and room[i - 1][j] > 0:
                    neighbors.append((i - 1, j))
                if i + 1 < n_row and room[i+1][j] > 0:
                    neighbors.append((i + 1, j))
                if j - 1 >= 0 and room[i][j - 1] > 0:
                    neighbors.append((i, j - 1))
                if j + 1 < n_col and room[i][j + 1] > 0:
                    neighbors.append((i, j + 1))
                if neighbors:
                    g[(i, j)] = neighbors
    return g


def get_guard_positions(room):
    guard_positions = []
    n_row, n_col = len(room), len(room[0])
    for i in range(n_row):
        for j in range(n_col):
            if room[i][j] == 2:
                guard_positions.append((i, j))
    return guard_positions


def get_shortest_distance(g, src, guards_positions):
    queue = [src]
    visited = [src]
    level_dict = {src: 0}

    while queue:
        node = queue.pop(0)

        if node in guards_positions:
            print(node, level_dict[node])
            return level_dict[node]

        for vertex in (n for n in g[node] if n not in visited):
            visited.append(vertex)
            queue.append(vertex)
            level_dict[vertex] = level_dict[node] + 1
    return 0


def find_shortest_distance_to_guards(room):
    if not isinstance(room, list) and not isinstance(room[0], list):
        return None

    g = room_to_graph(room)
    guards_positions = get_guard_positions(room)
    print(g)
    print(guards_positions)
    n_row, n_col = len(room), len(room[0])

    # store final result, each value is the shortest distance to a guard
    shortest_path_matrix = [[0 for x in range(n_col)] for y in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            if room[i][j] == 1 and (i, j) in g:
                shortest_path_matrix[i][j] = get_shortest_distance(g, (i, j), guards_positions)
    return shortest_path_matrix

if __name__ == '__main__':
    room1 = [
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 2, 1, 0],
        [0, 0, 0, 0]
    ]

    room2 = [
        [0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 2, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 1, 0, 2],
        [2, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0]
    ]

    print(find_shortest_distance_to_guards(room1))
