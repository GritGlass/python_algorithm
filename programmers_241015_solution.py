def solution(id_list, report, k):

    id_cnt=[0]*len(id_list)
    report=list(set(report))
    for rep in report:
        a,b=rep.split(' ')
        id_loc=id_list.index(b)
        id_cnt[id_loc]+=1

    id_index=[]
    for i,cnt in enumerate(id_cnt):
        if cnt>=k:
            id_index.append(id_list[i])

    stop_cnt=[0]*len(id_list)
    for c in id_index:
        for rep in report:
            a,b=rep.split(' ')
            if c==b:
                id_loc=id_list.index(a)
                stop_cnt[id_loc]+=1


    return stop_cnt