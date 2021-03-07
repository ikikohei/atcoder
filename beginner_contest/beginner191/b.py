def main():
    n, x = map(int,input().split())
    a_list = list(map(int,input().split())) 
    ans_list = []
    for i in range(n):
        if a_list[i] != x:
            ans_list.append(a_list[i])
    return print(*ans_list)

if __name__ == "__main__":
    main()