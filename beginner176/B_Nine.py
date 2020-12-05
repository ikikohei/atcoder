def Nine(N):
    sumN = 0
    for n in N:
        sumN += int(n)
    if sumN % 9 ==0: return "Yes"
    else: return "No"


def main():
    N = input()
    print(Nine(N))

if __name__=='__main__':
    main()