def main():
    n = int(input())
    alp_num = 26
    alp_list = [chr(ord('a') + i) for i in range(26)]
    s = 0
    for num in range(1, 12):
        s += alp_num ** num
        if n <= s:
            order = num
            break
    ans_list = []
    order_num = n - alp_num**(order-1)
    print(order_num)
    # if order != 1: order_num -= 1
    for i in range(order-1):
        if order_num != 0: order_num -= 1
        ans_list.append(alp_list[order_num % alp_num])
        order_num = order_num // alp_num
    print(order_num)
    ans_list.append(alp_list[order_num])
    ans_list = reversed(ans_list)
    print(''.join(ans_list))

if __name__=='__main__':
    main()
