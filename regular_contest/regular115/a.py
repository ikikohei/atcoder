def main():
    n, m = map(int, input().split())
    ans_list = []
    for _ in range(n):
        answer = input()
        ans_list.append(answer)
    ans_dict = {}
    even = 0
    odd = 0
    for i in range(n):
        num = 0
        for ans in ans_list[i]:
            if ans == "1":
                num += 1
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    print(even * odd)

if __name__=="__main__":
    main()


