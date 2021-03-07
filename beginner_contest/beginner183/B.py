def Billiards(Sx,Sy,Gx,Gy):
    a = (-Gy - Sy)/(Gx-Sx)
    b = Sy - a*Sx
    return - b / a


def main():
    Sx,Sy,Gx,Gy = map(int,input().split())
    print(Billiards(Sx,Sy,Gx,Gy))

if __name__=='__main__':
    main()