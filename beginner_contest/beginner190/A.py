def main():
    n, s, d = map(int,input().split())
    magic_l = []
    for i in range(n):
        magic_l.append(list(map(int,input().split())))
    for magic in magic_l:
        if magic[0] < s and magic[1] > d:
            return print("Yes")
    print("No")

if __name__ == "__main__":
    main()