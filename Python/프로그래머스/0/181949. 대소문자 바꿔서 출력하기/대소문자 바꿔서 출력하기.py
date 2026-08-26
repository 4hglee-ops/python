str = input()
answer = ''
for text in str:
    if ord(text) < 97:
        answer += text.lower()
    else:
        answer += text.upper()
print(answer)
        