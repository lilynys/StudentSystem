def Avg_(s1,s2,s3):
    return (s1+s2+s3) / 3

def Grade(a) :
    if a >= 100 :
        return 'A+'
    elif a >= 90 :
        return 'A'
    elif a >= 80 :
        return 'B'
    elif a >= 70:
        return 'C'
    elif a >= 60:
        return 'D'
    else :
        return 'F'
#리스트내의 최고 점수를 반환하는 함수
def Find_max(score_list) :
    a=-1
    for index in (score_list):
        if index > a:
            a = index
        else :
            a = a
    return a
#리스트내의 최저 점수를 반환하는 함수
def Find_min(score_list) :
    a= 1000
    for index in (score_list):
        if index < a:
            a = index
        else :
            a = a
    return a
         
