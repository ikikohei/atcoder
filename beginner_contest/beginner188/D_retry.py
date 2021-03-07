def main():
    n,prime_c = map(int,input().split())
    cost_dict = {}
    for i in range(n):
        a,b,c = map(int,input().split())
        if cost_dict.get(a) is None:
            cost_dict.update({a: c})
        else:
            cost_dict[a] += c
        if cost_dict.get(b+1) is None:
            cost_dict.update({b+1:-c})
        else:
            cost_dict[b+1] -= c
    cost_list = sorted(cost_dict.items(), key=lambda x:x[0])
    # print(cost_list)
    all_cost = 0
    daily_cost = cost_list[0][1]
    for i in range(1,len(cost_list)):
        # print(i)
        tmp_cost = min(prime_c,daily_cost)
        # print(tmp_cost)
        all_cost += tmp_cost*(cost_list[i][0] - cost_list[i-1][0])
        daily_cost += cost_list[i][1]
    print(all_cost)

if __name__ == "__main__":
    main()