def main():
    import itertools
    cookies = list(map(int,input().split()))
    for i in range(1,3):
        for com in itertools.combinations(cookies,i):
            if sum(com) == sum(cookies) / 2:
                return print("Yes")
    return print("No")

if __name__ == "__main__":
    main()

