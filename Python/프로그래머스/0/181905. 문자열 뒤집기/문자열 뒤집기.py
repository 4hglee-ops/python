def solution(my_string, s, e):
    save_string = my_string[s:e+1][::-1]
    return my_string[:s]+save_string+my_string[e+1:]