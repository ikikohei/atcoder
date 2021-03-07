def main():
    k = int(input())
    ans = 0
    for i in range(k):
        for j in range(k//(i+1)):
            ans += (k // (i+1)) // (j+1)
    print(ans)


if __name__=="__main__":
    main()