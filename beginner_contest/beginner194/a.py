def main():
    a, b = map(int, input().split())
    if a+b >= 15 and b >= 8:
        return print(1)
    if a+b >= 10 and b >= 3:
        return print(2)
    if a+b >= 3:
        return print(3)
    print(4)

if __name__=='__main__':
    main()