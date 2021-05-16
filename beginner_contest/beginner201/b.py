def main():
    n = int(input())
    top = 0
    second = 0
    mountains = {}
    for _ in range(n):
        s, t = map(str, input().split())
        t = int(t)
        mountains[t] = s
        if t > top:
            second = top
            top = t
            continue
        if t > second:
            second = t
    print(mountains[second])
            
if __name__=="__main__":
    main()
