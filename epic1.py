with open("epic2.txt", "r") as f:
    j = f.readlines()

for line in j:
    print(int(line) * 0.299792)