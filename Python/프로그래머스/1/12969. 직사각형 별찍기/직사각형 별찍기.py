a, b = map(int, input().strip().split(' '))
for y in range(b):
    answer_print = ''
    for x in range(a):
        answer_print += "*"
    print(answer_print)