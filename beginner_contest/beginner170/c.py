def main():
    x, n = map(int, input().split())
    if n == 0: return print(x)
    p_list = list(map(int, input().split()))
    p_set = set(p_list)
    diff = 0
    while True:
        x_pls, x_min = x + diff, x-diff
        if x_min not in p_set:
            return print(x_min)
        if x_pls not in p_set:
            return print(x_pls)
        diff += 1
    
if __name__=="__main__":
    main()