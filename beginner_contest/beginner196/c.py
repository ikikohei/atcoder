def main():
    n = int(input())
    index = 0
    ans = 0
    while True:
        if index == len(str(n)):
            keta = index
            break
        if index % 2 == 0:
            ans += 9 * 10 ** (index / 2 - 1)
        index += 1
    if keta % 2 == 1:
        return print(int(ans))
    num = int(10 ** (keta/2 - 1))
    while True:
        if int(str(num) + str(num)) <= n:
            ans += 1
            num += 1
        else:
            break
    print(int(ans))

if __name__=='__main__':
    main()
        


        

