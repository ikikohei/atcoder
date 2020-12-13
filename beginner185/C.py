def main():
    import math
    L = int(input())
    print(math.factorial(L-1)//math.factorial(11)//math.factorial(L-12))

if __name__=='__main__':
    main()
