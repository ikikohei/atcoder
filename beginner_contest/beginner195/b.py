def main():
    a, b, w = map(int,input().split())
    if a == b:
        if (w*1000)%a != 0:
            return print("UNSATISFIABLE")
        return print(str((w*1000)/a)+" "+str((w*1000)/a))
    from decimal import Decimal
    a_split = w * 1000 // a
    amari = (w * 1000) % a
    if (b-a)*a_split < amari:
        return print("UNSATISFIABLE")
    b_split = (w*1000) // b +1
    if (w*100)%b == 0:
        b_split=(w*1000)//b
    print(str(b_split) + " " + str(a_split))

if __name__=='__main__':
    main()
        