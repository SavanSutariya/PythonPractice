# Solution 2
n = int(input())
arr = list(set(map(int, input().split())))
arr.remove(max(arr))
print(max(arr))

# Solution 1
# n = int(input())
# arr = sorted(list(set(map(int, input().split()))))[-2]
# print(arr)

# Solution 0
#n = int(input())
#arr = list(map(int, input().split()))
# mxcount = arr.count(max(arr))
# for i in range(mxcount):
#     arr.remove(max(arr))
# print(max(arr))
