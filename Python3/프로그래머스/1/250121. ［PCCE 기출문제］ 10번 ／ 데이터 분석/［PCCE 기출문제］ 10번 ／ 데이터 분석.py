'''
data =   정렬한 데이터들이 담긴 이차원 정수 리스트
ext = 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 (code, date, maximun, remain)
val_ext = 뽑아낼 정보의 기준값을 나타내는 정수
sort_by = 정보를 정렬할 기준이 되는 문자열 (code, date, maximun, remain)

data에서 ext 값이 val_ext 보다 작은 데이터만 뽑은 후 sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여
retrun하도록 solution 함수 완성
'''
def solution(data, ext, val_ext, sort_by):
    answer = []
    h = len(data) # 행 저장 변수
    extsave = ['code','date','maximum','remain'] #ext, sory_by 값 리스트 저장
    for i in range(h) : #행만큼 반복
        if val_ext > data[i][extsave.index(ext)] :
            answer.append(data[i])
    answer.sort(key=lambda x:x[extsave.index(sort_by)])
    return answer