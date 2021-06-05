def main():
    from collections import defaultdict
    n, k = map(int, input().split())
    df = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        df[a] += b
    df_sorted = sorted(df.items(), key=lambda x:x[0])
    okane = k
    # print("df_sorted {} ".format(df_sorted))
    for d in df_sorted:
        if okane < d[0]:
            break
        okane += d[1]
    return print(okane)

if __name__=="__main__":
    main()
    

    
        