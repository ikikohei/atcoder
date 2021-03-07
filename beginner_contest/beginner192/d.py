def convert_num(i, num):
    ans = 0
    index = 0
    for n in reversed(str(num)):
        ans += int(n) * i**index
        index += 1
    return ans

def main():
    x = input()
    m = input()
    x_set_list = list(set(list(x)))
    max_num = 0
    for i in x_set_list:
        max_num = max(max_num, int(i))
    index = max_num + 1
    xlen = len(x)
    x = int(x)
    ans = 0
    l  = len(m)
    print(l)
    print(xlen)
    if l - xlen > 1:
        ans = 10 ** (l-xlen) - index
        index = 10 ** (l-xlen)
        print(index)
    print(convert_num(index, x))
    while True:
        print(index)
        if convert_num(index, x) <= int(m):
            ans += 1
            index += 1
        else: break
    print(ans)
    
if __name__=='__main__':
    main()