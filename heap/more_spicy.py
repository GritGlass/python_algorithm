# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq

def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    
    while len(scoville)>=2:
        minimum=heapq.heappop(scoville)
        if minimum<K:
            minimum2=heapq.heappop(scoville)
            heapq.heappush(scoville,minimum+(minimum2*2))
            answer+=1
        else:
            break
            
    if (len(scoville)<2)&(scoville[0]<K):
        answer=-1
            
    return answer