#ascii코드로 숫자구분해서 +- 하기
#ord() 문자를 숫자로, 숫자를 문자로 chr(), 대문자 65~90 / 소문자 97~122
def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if 65<=ord(my_string[i])<=90:
            answer+=chr(ord(my_string[i])+32)
        elif 97<=ord(my_string[i])<=122:
            answer+=chr(ord(my_string[i])-32)
    return answer