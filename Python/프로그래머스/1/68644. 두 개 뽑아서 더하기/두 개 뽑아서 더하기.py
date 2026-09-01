# set으로 처리하면 될듯

def solution(numbers):
    answer = set()
    for idx1,num1 in enumerate(numbers[:-1]):
        for num2 in numbers[idx1+1:]:
            answer.add(num1+num2)
    return sorted(list(answer))