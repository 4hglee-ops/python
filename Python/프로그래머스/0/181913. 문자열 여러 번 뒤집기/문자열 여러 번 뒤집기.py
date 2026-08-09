def solution(my_string, queries):
    for querie in queries:
        start_idx, end_idx = querie
        m_string = my_string[start_idx:end_idx+1]
        my_string = my_string[:start_idx]+m_string[::-1]+my_string[end_idx+1:]
        
    return my_string