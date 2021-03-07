def main():
    import math
    n = int(input())
    a , b = 1, 1
    maxa = int(18 / math.log10(3)) + 1
    maxb = int(18 / math.log10(5)) + 1
    for ai in range(maxa):
        for bi in range(maxb):
            if 3**(ai+a)+5**(bi+b)==n:
                return print("{} {}".format(ai+a,bi+b))
    return print(-1)

if __name__ == "__main__":
    main()