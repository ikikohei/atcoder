def main():
    s = input()
    ans = []
    for c in reversed(s):
        if c == "6":
            c = "9"
        elif c == "9":
            c = "6"
        ans.append(c)
    print("".join(ans))

if __name__=="__main__":
    main()