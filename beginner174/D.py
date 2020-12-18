def main():
    n = int(input())
    whiteCount = 0
    ans = 0
    rocks = input() 
    for rock in rocks:
        if rock == "W": whiteCount += 1
    for ri in reversed(range(n-whiteCount,n)):
        if rocks[ri]=="R": ans += 1
    print(ans)

if __name__ == "__main__":
    main()