def devisor_count(n):
    i = 1
    count = 0
    while i*i <= n:
        if n % i == 0:
            count += 1
            if n != i * i:
                count += 1
        i += 1
    return count
# 愚直に計算したがダメ
def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        # print("i : {}  devisorcount: {}".format(i,devisor_count(i)))
        ans += devisor_count(i) * i
    print(ans)

if __name__ == "__main__":
    main()
