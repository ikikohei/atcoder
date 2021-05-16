def calc_b(d, h, di, hi):
    if d - di == 0:
        return 0
    a = (h-hi) / (d - di)
    return h - a * d

def main():
    n, d, h = map(int, input().split())
    b = 0
    for _ in range(n):
        di, hi = map(int, input().split())
        tmp_b = calc_b(d, h, di, hi)
        b = max(tmp_b, b)
    return print(b)

if __name__=="__main__":
    main()

