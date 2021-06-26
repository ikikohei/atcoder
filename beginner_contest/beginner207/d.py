from decimal import Decimal
import math

def check(s, t):
    s_sort = sorted(s)
    t_sort = sorted(t)
    diff = [-s_sort[0][0]+t_sort[0][0], -s_sort[0][1]+t_sort[0][1]]
    for i in range(len(s_sort)):
        if s_sort[i][0] + diff[0] != t_sort[i][0] or s_sort[i][1] + diff[1] != t_sort[i][1]:
            return False
    return True
        

def rotate(p,a,b):
    p_pi = Decimal(str(p)) / Decimal("360") * Decimal("2") * Decimal(str(math.pi))
    return a*Decimal(str(math.cos(p_pi))) - b*Decimal(str(math.sin(p_pi))), a*Decimal(str(math.sin(p_pi))) + b*Decimal(str(math.cos(p_pi)))

def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        a, b = map(str, input().split())
        s.append([Decimal(a),Decimal(b)])
    for _ in range(n):
        c,d = map(str, input().split())
        t.append([Decimal(c),Decimal(d)])
    for i in range(1,360):
        rotate_s = []
        for p in s:
            x, y = rotate(i,p[0],p[1])
            rotate_s.append([x,y])
        if i == 270:
            print(rotate_s)
        if check(rotate_s, t):
            return print("Yes")
    return print("No")

if __name__=="__main__":
    main()
