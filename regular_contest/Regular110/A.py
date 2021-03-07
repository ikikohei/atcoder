def checkSosu(num):
    for n in range(2,num):
        if num % n == 0: return False
    return True

def main():
    N = int(input())
    ans = 1
    for i in range(1, N+1):
        if checkSosu(i):
            # print(i)
            ans = ans * i
            # print(ans)
    print((ans*2*4*3*3*5) + 1)

if __name__=='__main__':
    main()