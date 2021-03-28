def main():
    import itertools
    INF = 10 ** 19
    n = int(input())
    a_list = list(map(int, input().split()))
    if n == 1:
        return (print(a_list[0]))
    num_list = [i+1 for i in range(n-1)]
    ans = INF
    for i in range(n-1):
        for combi in itertools.combinations(num_list,i+1):
            # print(combi)
            xor_ans = 0
            before = 0
            for com in combi:
                or_ans = 0
                for j in range(before, com):
                    or_ans = or_ans | a_list[j]
                xor_ans = xor_ans ^ or_ans
                before = com
            or_ans = 0
            for j in range(before, n):
                or_ans = or_ans | a_list[j]
            xor_ans = xor_ans ^ or_ans
            ans = min(ans, xor_ans)
    print(ans)

if __name__=="__main__":
    main()
        

        
            
                
                
    