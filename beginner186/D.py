# 全部やったらもちろん時間がたりません
def main():
    n = int(input())
    numlist = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += abs(numlist[i]-numlist[j])
    print(ans)

if __name__ == "__main__":
    main()
            

