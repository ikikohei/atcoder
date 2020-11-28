def subString(S,T):
    count = 0
    maxcount = 0
    for i in range(len(S)):
        for j in range(len(T)):
            if i+len(T) > len(S): break
            if S[i+j] == T[j]:
                count += 1
                maxcount = max(count,maxcount)
        count=0
    return len(T) - maxcount

def main():
    S = input()
    T = input()
    print(subString(S,T))

if __name__=='__main__':
    main()