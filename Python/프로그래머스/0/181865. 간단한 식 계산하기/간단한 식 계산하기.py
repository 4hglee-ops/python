def solution(binomial):
    b_split_list = binomial.split()
    a = int(b_split_list[0])
    b = int(b_split_list[2])
    op = b_split_list[1]
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b