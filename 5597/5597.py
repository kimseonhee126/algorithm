students = list(range(1, 31))

for i in range(28):
    submit = int(input())
    students.remove(submit)

for student in students:
    print(student)