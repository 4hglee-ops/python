# 에러사항
# 실수로 나오는 부분
# 약분

import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = math.lcm(denom1,denom2)
    numer = numer1 * denom//denom1 + numer2 * denom//denom2
    g = math.gcd(numer,denom)
    return [numer//g, denom//g]