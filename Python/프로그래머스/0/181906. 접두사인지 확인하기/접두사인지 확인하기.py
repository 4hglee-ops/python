def solution(my_string, is_prefix):
    my_string_list = []

    for idx, text in enumerate(my_string):
        my_string_list.append(my_string[:idx])
    if is_prefix in my_string_list:
        return 1
        
    return 0