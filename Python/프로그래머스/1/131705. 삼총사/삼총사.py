def solution(number):
    answer = 0
    for idx1 in range(len(number)):
        for idx2 in range(idx1+1,len(number)):
            for idx3 in range(idx2+1,len(number)):
                if number[idx1]+number[idx2]+number[idx3] == 0:
                    answer+=1
    return answer
# 아래 풀이는 케이스 2개 실패, 이유: index()는 같은 숫자일경우 앞의 인덱스를 반환함

# def solution(number):
#     answer = 0
#     number = sorted(number)
#     for idx1,num1 in enumerate(number):
#         for idx2,num2 in enumerate(number[number.index(num1)+1:]):
#             for idx3,num3 in enumerate(number[number.index(num2)+1:]):
#                 if num1+num2+num3 == 0:
#                     answer += 1
#     return answer