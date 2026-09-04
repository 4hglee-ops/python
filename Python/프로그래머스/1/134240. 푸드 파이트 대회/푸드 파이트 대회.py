def solution(food):
    answer = ''
    food_even = []
    for num in food:
        if num % 2:
            food_even.append((num-1)//2)
        else:
            food_even.append(num//2)
    for idx,num in enumerate(food_even):
        if num:
            answer += str(idx)*num
    return answer+"0"+answer[::-1]