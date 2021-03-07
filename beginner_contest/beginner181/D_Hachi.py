def judgeHachi(N):
    # hachies = [(i+1)*8 for in range(999//8)]
    count = 0
    Nlist = list(N)
    for i in range(100//8,999//8):
        hachi = str((i+1)*8)
        for num in hachi:
            if num in Nlist:
                Nlist.remove(num)
                count += 1
            if count==3: return True
        Nlist = list(N)
        count = 0
    return False

def switchNum(num):
    numlist = list(num)
    return int(numlist[1])*10 + int(numlist[0])

def main():
    N = input()
    judge = False
    if len(N) == 1 and N == "8":
        judge = True
    if len(N) == 2:
        if int(N)%8==0 or switchNum(N)%8==0:
            judge = True
    if len(N) > 2:
        judge = judgeHachi(N)
    print("Yes") if judge else print("No")

if __name__ == '__main__':
    main()
