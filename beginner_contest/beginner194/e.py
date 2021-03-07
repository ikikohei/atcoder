def mex(tmpset):
    loop = 1
    while True:
        if loop not in tmpset:
            return loop
        loop += 1

def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    mex_list = []
    for i in range(n-m+1):
        tmp_list = a_list[i:i+m]
        tmp_set = set(tmp_list)
        mex_list.append(mex(tmp_set))
    print(min(mex_list))

if __name__=='__main__':
    main()


