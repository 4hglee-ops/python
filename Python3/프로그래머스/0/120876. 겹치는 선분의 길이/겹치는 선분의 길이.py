def solution(lines):
    answer = 0
    line1 = []
    line2 = []
    line3 = []
    set_line = set()

    line12 = []
    line13 = []
    line23 = []

 
    for i in range(lines[0][1]-lines[0][0]):
        line1.append((lines[0][0]+i,lines[0][0]+i+1))
        #print(f"line0 {line}, {line1}")

    for i in range(lines[1][1]-lines[1][0]):
        line2.append((lines[1][0]+i,lines[1][0]+i+1))
        #print(f"line1 {line}, {line2}")
        
    for i in range(lines[2][1]-lines[2][0]):
        line3.append((lines[2][0]+i,lines[2][0]+i+1))
        #print(f"line1 {line}, {line2}")

    print(line1)
    print(line2)
    print(line3)

    for line in line1:
        if line in line2:
            line12.append(line)
        if line in line3:
            line13.append(line)
    for line in line2:
        if line in line3:
            line23.append(line)
    
    set_line.update(line12,line13,line23)

    answer = len(set_line) 

    return answer