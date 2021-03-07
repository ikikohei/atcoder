def main():
    n = int(input())
    alp_num = 26
    alp_list = [chr(ord('a') + i) for i in range(26)]
    sums = 0
    for num in range(1, 12):
        sums += alp_num ** num 
        if n <= sums:
            first_num = num
            break
    ans_list = []
    if first_num == 1:
        num = n
    else:
        num = n - alp_num**(first_num-1)
    # print(num)
    for i in reversed(range(first_num-1)):
        # print(i)
        if num %  (alp_num**(i+1)) == 0:
            ans_list.append(alp_list[num // alp_num**(i+1) -1])
        else:
            ans_list.append(alp_list[num // alp_num**(i+1)])
        num = num % (alp_num**(i+1))
    ans_list.append(alp_list[num-1])
    print("".join(ans_list))

if __name__=='__main__':
    main()
