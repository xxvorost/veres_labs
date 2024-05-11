from collections import deque


def read_input(file_path):
    with open(file_path, 'r') as file:
        start = tuple(map(int, file.readline().strip().split(',')))
        end = tuple(map(int, file.readline().strip().split(',')))
        dimensions = tuple(map(int, file.readline().strip().split(',')))
        grid = []
        for _ in range(dimensions[0]):
            row = list(map(int, file.readline().strip().replace('[', '').replace(']', '').split()))
            grid.append(row)
    return start, end, grid


def bfs_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    return -1  # If no path is found


def write_output(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


def main():
    start, end, grid = read_input('input1.txt')
    result = bfs_shortest_path(grid, start, end)
    write_output('output1.txt', result)


if __name__ == "__main__":
    main()
