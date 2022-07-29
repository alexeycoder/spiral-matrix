def print_matrix(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            print(arr_2d[i][j], end='\t')
        print('\n')

n = int(input("Введите натуральное число: "))

if (n <= 0):
    print("Некорректный ввод!")

array2d = [[0]*n for i in range(n)]

num_of_items = n * n

u = 0
v = 0
u_min = 0
u_max = n - 1
v_min = 0
v_max = n - 1

i = 1

while (i <= num_of_items):

    # go right
    for u in range(u_min, u_max + 1):
        array2d[v][u] = i
        i += 1
    v_min += 1

    # go down
    for v in range(v_min, v_max + 1):
        array2d[v][u] = i
        i += 1
    u_max -= 1

    # go left
    for u in range(u_max, u_min - 1, -1):
        array2d[v][u] = i
        i += 1
    v_max -= 1

    # go up
    for v in range(v_max, v_min - 1, -1):
        array2d[v][u] = i
        i += 1
    u_min += 1

print_matrix(array2d)
