with open("epictxt.txt", "r") as f:
    j = f.readline()
    j = [j]

for line in j:
    print(int(line.split()[0]) * int(line.split()[1]))