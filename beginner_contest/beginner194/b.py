def main():
    INFTY = 10**5 + 1
    n = int(input())
    time_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        time_list.append([a,b])
    min_time = INFTY
    time = INFTY
    for i in range(n):
        for j in range(n):
            if i == j:
                time = time_list[i][0] + time_list[j][1]
            else:
                time = max(time_list[i][0], time_list[j][1])
            min_time = min(min_time, time)
    print(min_time)

if __name__=='__main__':
    main()



