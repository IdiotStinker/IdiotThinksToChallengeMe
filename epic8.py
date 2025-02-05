with open("epic8.txt","r") as f:
    j = f.readlines()

def toBinary(num):
    L = 0
    if num == 0:
        return "0"
    while True:
        if num - (2**L) >= 0:
            L += 1
            continue
        break
    binaryNum = ""
    for i in range(L - 1, -1, -1):
        if num - 2**i >= 0:
            num -= 2**i
            binaryNum += "1"
        else:
            binaryNum += "0"

    total = 0
    for car in binaryNum:
        total += int(car)
    return total

for line in j:
    op = line.split()
    oPS = []
    for kajd in op:
        oPS.append(int(kajd))
    epic = 0
    for i in range(oPS[0], oPS[1]+1):
        if int(toBinary(i)) % 2 == 0:
            epic += 1
    
    print(epic)
