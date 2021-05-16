def main():
    a = list(map(int,input().split()))
    import itertools
    for tmp in itertools.permutations(a, 3):
        if tmp[2] - tmp[1] == tmp[1] - tmp[0]:
            return print("Yes")
    print("No")

if __name__=="__main__":
    main()