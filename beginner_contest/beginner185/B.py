def main():
    N, M, T = map(int, input().split())
    vat = N
    Alist = []
    Blist = []
    Bbefore = 0
    for m in range(M):
        A, B = map(int,input().split())
        Alist.append(A)
        Blist.append(B)
    for i in range(M):
        vat -= Alist[i] - Bbefore
        if vat <= 0 : return print("No")
        vat += Blist[i] - Alist[i]
        if vat > N : vat = N
        # print(vat)
        Bbefore = Blist[i]
    vat -= T - Bbefore
    if vat <= 0 : return print("No")
    print("Yes")
            
if __name__=='__main__':
    main()