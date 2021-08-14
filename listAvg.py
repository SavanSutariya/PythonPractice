n = int(input())
student_marks = {}
def avg(lst):
    return sum(lst)/len(lst)
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print("%.2f"%avg(student_marks[input()]))