def get_loop_list(n):
    ans_list = []
    num = n
    ans_list.append(int(str(num)[-1]))
    # print(int(str(num)[-1]))
    while True:
        num = num * n
        if int(str(num)[-1]) in ans_list: break
        ans_list.append(int(str(num)[-1]))
        # print(ans_list)
    # print(ans_list)
    # ans_list = list(ans_list)
    return ans_list

def main():
    a, b, c = map(int, input().split())
    a_list = get_loop_list(a)
    # print(a_list)
    spliter = len(a_list)
    # print(spliter)
    index = pow(b,c,spliter)
    # print(index)
    print(a_list[index-1])
    
if __name__=="__main__":
    main()
        