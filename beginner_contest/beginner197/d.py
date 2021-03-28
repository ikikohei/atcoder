import math
def roll(x, y, sheta):
    sheta = sheta / 360 * 2 * math.pi
    return (x * math.cos(sheta) - y * math.sin(sheta), y*math.cos(sheta) + x*math.sin(sheta))

def leng(x0, y0, xi, yi):
    return math.sqrt((xi-x0)**2 + (yi-y0)**2)

def main():
    from decimal import Decimal
    n = int(input())
    x_zero, y_zero = map(int, input().split())
    x_n_half, y_n_half = map(int, input().split())
    taikaku = leng(x_zero, y_zero, x_n_half, y_n_half)    
    kaku = 180 * (n-2) / n
    hen = taikaku * math.cos(kaku / 360 * math.pi)
    if x_n_half - x_zero != 0:
        katamuki = (y_n_half - y_zero)/(x_n_half - x_zero)
        if x_n_half > x_zero:
            operator = 1
        else:
            operator = -1
        roll_base_x = operator*math.sqrt(hen**2 / (katamuki**2 + 1))
        roll_base = (roll_base_x, katamuki * roll_base_x)
    else:
        if y_n_half < y_zero:
            roll_base = (0, -hen)
        else:
            roll_base = (0, hen)
    roll_after = roll(roll_base[0], roll_base[1], -kaku/2)
    ans = [roll_after[0]+x_zero, roll_after[1] + y_zero]
    print(" ".join([str(n) for n in ans]))

if __name__=="__main__":
    main()
