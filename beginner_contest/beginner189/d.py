def main():
    n = int(input())
    ao_l = []
    for _ in range(n):
        ao_l.append(input())
    t_num = 1
    f_num = 1
    loop = 0
    for ao in ao_l:
        if ao == "AND":
            f_num = 2**(loop+2) - t_num
        else:
            t_num = 2**(loop+2) - f_num
        loop += 1
    return print(t_num)
        
if __name__ == "__main__":
    main()