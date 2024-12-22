# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    roate_size=[(max(w,h),min(w,h)) for w,h in sizes]
    max_w=max([w for w,h in roate_size])
    max_h=max([h for w,h in roate_size])
    
    answer=max_w*max_h
    return answer