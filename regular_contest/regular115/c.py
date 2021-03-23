def main():
    n = int(input())
    ans_list = [0 for i in range(n)]
    ans_list[0] = 1
    for i in range(1, n):
        ans = 0
        index = 1
        n = i + 1
        while index*index <= n:
            if n % index == 0:
                ans = max(ans, ans_list[index - 1])
                if index != n//index:
                    ans = max(ans, ans_list[n//index - 1])
            index += 1
        ans_list[i] = ans + 1
    print(" ".join(map(str,ans_list)))

if __name__=="__main__":
    main()

