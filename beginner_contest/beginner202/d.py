from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def identify_b(a, b, k):
    r = 0
    n = b-1
    count = 0
    pre_count = 0
    while True:
        count += cmb(n, r)
        if k <= count:
            k -= pre_count
            b -= 1
            return a - r, r, b, k
        if r == a:
            return 0
        n += 1
        r += 1
        pre_count = count


def main():
    a, b, k = map(int, input().split())
    num = a+b
    tmp = 0
    b_posi_list = []
    for _ in range(b):
        b_posi, a, b, k = identify_b(a, b, k)
        b_posi_list.append(tmp + b_posi)
        tmp += b_posi + 1
    ans = []
    for i in range(num):
        if i in b_posi_list:
            ans.append("b")
        else:
            ans.append("a")
    return print("".join(ans))

if __name__=="__main__":
    main()




