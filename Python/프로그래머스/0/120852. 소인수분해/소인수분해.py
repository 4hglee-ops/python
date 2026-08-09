def solution(n):
    answer = []
    ans_set = set()
    i = 2
    while n > 1:
        if n%i == 0:
            ans_set.add(i)
            n = n//i
            i = 2
        else:
            i+=1
    answer = sorted(list(ans_set))
    return answer

test_cases = [
    12,
    17,
    20,
    30,
    49,
    84,
    100,
    210,
    997,
    420
]

for n in test_cases:
    print(n, solution(n))