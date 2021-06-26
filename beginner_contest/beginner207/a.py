def main():
    a, b, c = map(int, input().split())
    return print(max(a+b, b+c, c+a))

if __name__=="__main__":
    main()