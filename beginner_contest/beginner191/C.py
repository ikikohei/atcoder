def check_white(mapping,hi,wi):
    white = 0
    if hi != 0:
        if mapping[hi-1][wi] == ".": white += 1
    if wi != 0:
        if mapping[hi][wi-1] == ".": white += 1
    if mapping[hi+1][wi]==".": white += 1
    if mapping[hi][wi+1]==".": white += 1
    if white == 2:
        if mapping[hi-1][wi] == mapping[hi+1][wi]: return 0
    if white == 2: return 1
    if white == 3 and mapping[hi][wi] == "#": return 2
    if white == 1 and mapping[hi][wi] == ".": return 2
    if white == 4 and mapping[hi][wi] == "#": return 4
    return 0

def main():
    h, w = map(int,input().split())
    mapping = []
    for i in range(h):
        mapping.append(list(input()))
    ans = 0
    for hi in range(h):
        for wi in range(w):
            if hi==0 or wi==0 or hi==h-1 or wi==w-1: continue
            ans += check_white(mapping,hi,wi)
    print(ans)

if __name__ == "__main__":
    main()