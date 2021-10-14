from itertools import combinations_with_replacement
# from iterTools import combinations_with_replacement
i = input().split()
s = sorted(i[0])
lst = list(combinations_with_replacement(s,int(i[1])))
lst.sort()
for x in lst:
    print("".join(x))