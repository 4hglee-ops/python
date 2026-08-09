def solution(my_string):
    answer = ''
    string = ''

    # 1. 문자열을 하나씩 순회하며 대문자를 소문자로 변환
    for text in my_string:
        if 65 <= ord(text) <= 90:
            string += chr(ord(text) + 32)
        else:
            string += text

    # 2. 소문자로 통일된 문자열을 알파벳 순(오름차순)으로 정렬
    # sorted()의 결과는 각 글자가 담긴 리스트로 반환됩니다.
    text_list = sorted(string)

    # 3. 정렬된 리스트의 글자들을 하나의 문자열로 합치기
    answer = "".join(text_list)

    return answer

# 65
# abcde
# fghij
# klmno
# pqrst
# uvwxy
# z