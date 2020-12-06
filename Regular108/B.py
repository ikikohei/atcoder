def judge(num,s,ans):
    if num < len(s) and s[num] == "f":
        # print("f: {}".format(num))
        num += 1
        num,ans = judge(num, s, ans)
        if num < len(s) and s[num] == "o":
            # print("o: {}".format(num))
            num += 1
            num,ans = judge(num,s,ans)
            if num < len(s) and s[num] == "x":
                # print("x: {}".format(num))
                num = num + 1 
                ans = ans - 3
    return num, ans
       
def main():
    N = int(input())
    ans = N
    s = input()
    num = 0
    while num < N:
        num,ans = judge(num,s,ans)
        # print(ans)
        print(num)
        if num < N and s[num] != "f":
            num += 1
    print(ans)

if __name__=='__main__':
    main()
                

            