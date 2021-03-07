def hands(a,b,x,y):
    if a == b: return x
    if a < b:
        if y < 2*x: return (b-a)*y+x
        else: return (b-a)*2*x + x
    else:
        if y < 2*x: return (a-b-1)*y + x
        else: return (a-b)*2*x - x

def main():
    a, b, x, y = map(int,input().split())
    print(hands(a,b,x,y))

if __name__=='__main__':
    main()