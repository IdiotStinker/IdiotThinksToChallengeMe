with open("epic3.txt", "r") as f:
    j = f.readlines()

#print(j)

for k, line in enumerate(j):
    delta = []
    epic1 = line.split()
    for l, spot in enumerate(epic1):
        if l == 0:
            continue
        #print(spot)
        if spot[0] == "-":
            epic = -int(spot[1:])
        else:
            epic = int(spot)
        if epic1[l-1][0] == "-":
            other = -int(epic1[l-1][1:])
        else:
            other = int(epic1[l-1])
        delta.append(other - epic)
    final = []
    #print(delta)
    currentNum = int(epic1[0])
    final.append(currentNum)
    for t, thing in enumerate(delta):

        currentNum += thing
        final.append(currentNum)
    nextFinal = []
    #print(final)
    for thing2 in final:
        nextFinal.append(str(thing2))
    print(" ".join(nextFinal))