#https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    pok=set(nums)
    if len(pok)>=(len(nums)//2):
        answer=(len(nums)//2)
    else:
        answer=len(pok)
    return answer