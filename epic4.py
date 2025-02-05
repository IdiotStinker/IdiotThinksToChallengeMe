with open("epic4.txt","r") as f:
    j = f.readlines()

times = []
for thing in j:
    actual = thing.split()
    times.append(float(actual[1]) / float(actual[2]))

print(f"{j[times.index(min(times))].split()[0]} {min(times)}")

name = j[times.index(min(times))].split()[0]
