def main():
    n = int(input())
    pos_list = []
    for i in range(n):
        pos_list.append(list(map(int,input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (pos_list[i][1]-pos_list[j][1])/(pos_list[i][0]-pos_list[j][0]) <= 1:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
            