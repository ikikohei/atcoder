def mygcd(*numbers):
    from functools import reduce
    import math
    return reduce(math.gcd, numbers)

def main():
    n = int(input())
    num_list = list(map(int,input().split()))
    print(mygcd(*num_list))

if __name__ == "__main__":
    main()