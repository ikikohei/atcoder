def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    inner_product = 0
    for i in range(n):
        inner_product += a[i]*b[i]
    if inner_product == 0:
        return print("Yes")
    return print("No")

if __name__ == "__main__":
    main()

