size_of_matrix = int(input())
car = input()
matrix = []
for i in range(size_of_matrix):
    row = input().split(" ")
    matrix.append(row)

end = False
cmd = ''

distance, r, c = 0, 0, 0
stop = False

while True:
    cmd = input()
    stop = False
    if cmd == "End":
        matrix[r][c] = "C"
        break
    if cmd == "left":
        c -= 1
        distance += 10
    elif cmd == "right":
        c += 1
        distance += 10
    elif cmd == "down":
        r += 1
        distance += 10
    elif cmd == "up":
        r -= 1
        distance += 10
    if matrix[r][c] == "F":
        matrix[r][c] = "C"
        end = True
        break
    if matrix[r][c] == "T":
        matrix[r][c] = "."
        for i in range(size_of_matrix):
            if stop:
                break
            for j in range(size_of_matrix):
                if matrix[i][j] == "T":
                    r, c = i, j
                    matrix[r][c] = "."
                    distance += 20
                    stop = True
                    break
                else:
                    if matrix[i][j] != "F":
                        matrix[i][j] = "."

if end:
    print(f"Racing car {car} finished the stage!")
else:
    print(f"Racing car {car} DNF.")

print(f"Distance covered {distance} km.")
for i in range(size_of_matrix):
    print(*matrix[i], sep="")
    