def main():
    n = int(input())
    if n <= 999:
        return print(0)
    ans = 0
    index = 1
    num = 999
    nine = '9'
    while True:
        num = int(nine*3*index)
        if n <= num:
            return print(ans)
        ans += n - num
        index += 1
        print(num)

if __name__=='__main__':
    main()