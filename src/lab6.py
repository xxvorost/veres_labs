def calculate_max_experience(levels):
    for i in range(len(levels) - 2, -1, -1):
        for j in range(len(levels[i])):
            levels[i][j] += max(levels[i + 1][j], levels[i + 1][j + 1])
    return levels[0][0]


def main():
    with open("career.in", "r") as file:
        L = int(file.readline().strip())
        levels = []
        for _ in range(L):
            level = list(map(int, file.readline().strip().split()))
            levels.append(level)
    result = calculate_max_experience(levels)
    with open("career.out", "w") as file:
        file.write(str(result))


if __name__ == "__main__":
    main()
