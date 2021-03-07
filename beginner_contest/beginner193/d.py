def main():
    k = int(input())
    s = input()
    t = input()
    tramp = {}
    takahashi = {}
    aoki = {}
    for i in range(1,10):
        tramp[i] = 0
        takahashi[i] = 0
        aoki[i] = 0
    for str_num in s:
        if str_num == "#": continue
        takahashi[int(str_num)] += 1
        tramp[int(str_num)] += 1
    for str_num in t:
        if str_num == "#": continue
        aoki[int(str_num)] += 1
        tramp[int(str_num)] += 1
    takahashi_point = 0
    aoki_point = 0
    for i in range(1,10):
        takahashi_point += i * 10 ** takahashi[i]
        aoki_point += i * 10 ** aoki[i]
    takahashi_count = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(1,10):
        for j in range(1,10):
            tmp1 = takahashi_point + i * (10**(takahashi[i]+1) - 10**takahashi[i])
            tmp2 = aoki_point + j * (10**(aoki[j]+1) - 10**aoki[j])
            if tmp1 > tmp2:
                if i == j:
                    takahashi_count += (k - takahashi[i] - aoki[j]) * (k - takahashi[i] - aoki[j] - 1) 
                else:
                    if (k - takahashi[i] - aoki[i]) > 0 and (k - takahashi[j] - aoki[j]) > 0:
                        takahashi_count += (k-takahashi[i]-aoki[i]) * (k-takahashi[j]-aoki[j])
    print(takahashi_count/(9*k-8)/(9*k-9))

if __name__=='__main__':
    main()
            
