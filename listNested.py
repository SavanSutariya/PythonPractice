lst = []
secondLastLst = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name,score])
secondLastVal =  sorted((list(set(dict(lst).values()))))[1]
for l in lst:
    if l[1] == secondLastVal:
        secondLastLst.append(l[0])

for name in sorted(secondLastLst):
    print(name)