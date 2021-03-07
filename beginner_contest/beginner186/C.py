def main():
    n = int(input())
    ten_slicer = [1,10,10**2,10**3,10**4]
    eight_slicer = [1,8,8**2,8**3,8**4,8**5]
    # slicer = [10, 10**2,10**3,10**4,8,8**2,8**3,8**4,8**5]
    ans = 0
    count = 1
    for i in range(1,n+1):
        for t in ten_slicer:
            if (i//t)%10 == 7:
                count = 0
                break
        for e in eight_slicer:
            if (i//e)%8 == 7:
                count = 0
                break
        ans += count
        count = 1
    print(ans)
        
if __name__ == "__main__":
    main()