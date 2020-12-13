def main():
    S = input()
    count = 0
    ans = 0
    for s in S:
        if s == "R":
            count += 1
            ans = max(ans,count)
        else:
            count = 0
    print(ans)


if __name__=='__main__':
    main()