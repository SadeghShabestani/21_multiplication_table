row = int(input("Enter Row: "))
col = int(input("Enter column: "))

a = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    print()
    for j in range(col):
        a[i][j] = i * j

for i in range(row):
    print()
    for j in range(col):
        print(a[i][j], end="\t")
