def main():
    x, y = map(int, input().split())
    if x == y:
        return print(x)
    for i in range(3):
        if i != x and i != y:
            return print(i)

if __name__=="__main__":
    main()    