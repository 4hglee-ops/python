def solution(array, commands):
    answer = []
    for command in commands:
        a_list = []
        start_idx = command[0]-1
        end_idx = command[1]
        find_idx= command[2]-1

        for i in range(start_idx,end_idx):
            a_list.append(array[i])
        a_list.sort()

        answer.append(a_list[find_idx])

    return answer