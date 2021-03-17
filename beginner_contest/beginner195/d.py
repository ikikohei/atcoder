def main():
    n, m, q = map(int,input().split())
    baggage = []
    for _ in range(n):
        w, v = map(int, input().split())
        baggage.append([w,v])
    size_list = list(map(int, input().split()))
    size_dict = {}
    for index,size in enumerate(size_list):
        size_dict[index] = size
    size_dict_sorted = sorted(size_dict.items(), key=lambda x:x[1])
    query_list = []
    for _ in range(q):
        q1, q2 = map(int, input().split())
        query_list.append([q1-1,q2-1])
    remove_set = set()
    # print(size_dict_sorted)
    # print(query_list)
    over_num = 53
    for qi in range(q):
        value = 0
        remove_set.clear()
        # print(size_dict_sorted)
        for size_taple in size_dict_sorted:
            tmp_value = 0
            tmp_index = over_num
            # print(size_taple)
            if query_list[qi][0] <= size_taple[0] <= query_list[qi][1]:
                continue
            for ni in range(n):
                if ni in remove_set:
                    continue
                if size_taple[1] >= baggage[ni][0] and baggage[ni][1] >= tmp_value:
                    tmp_value = baggage[ni][1]
                    tmp_index = ni
            value += tmp_value
            # print(remove_set)
            remove_set.add(tmp_index)
        print(value)
            
if __name__=='__main__':
    main()


