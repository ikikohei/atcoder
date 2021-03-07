def main():
    n = int(input())
    num = 0
    i = 1
    n = n*2
    while i*i <= n:
        if n % i == 0:
            if i % 2 != (n/i)%2:
                num += 2
        i += 1
    return print(num)

if __name__ == "__main__":
    main()