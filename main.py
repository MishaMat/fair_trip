names = []
while True:
    name = input("type name or 0 to end: ")
    if name == '0':
        break
    names.append(name)
info = dict()
for i in names:
    info[i] = int(input(f"{i} spent: "))
mid_sum = int(sum(info.values()) / len(names))
for i in names:
    info[i] -= mid_sum
for i in names:
    if info[i] < 0:
        for j in names:
            if info[j] > 0:
                if abs(info[i]) > info[j] and (info[j] != 0):
                    info[i] += info[j]
                    print(f"{i} should give {j}: {info[j]} UAH")
                    info[j] = 0
                elif abs(info[i]) < info[j] and (info[i] != 0):
                    info[j] += info[i]
                    print(f"{i} should give {j}: {abs(info[i])} UAH")
                    info[i] = 0
