for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()

for i in range(1, 10):
    row = []
    for j in range(1, 10):
        row.append(f"{i} * {j} = {i * j}")
    print("\t".join(row))