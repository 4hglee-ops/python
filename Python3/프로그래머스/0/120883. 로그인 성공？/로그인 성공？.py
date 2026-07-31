def solution(id_pw, db):
    member = {}
    db_dic = {}
    member[id_pw[0]] = id_pw[1]
    for db_list in db:
        db_dic[db_list[0]] = db_list[1]
        
    if id_pw[0] in db_dic.keys():
        if db_dic[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"
    else :
        return "fail"
