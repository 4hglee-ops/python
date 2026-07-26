def solution(numbers):
    answer = ""
    stack = ""
    num_dic = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
        "zero" : "0"
    }
    for text in numbers:
        stack += text
        if stack in num_dic:
            answer += num_dic[stack]
            stack = ""     
    answer = int(answer)
    
    
    return answer