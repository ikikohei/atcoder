def main():
    x = input()
    ans_list = []
    for c in x:
        if c == ".":
            break
        ans_list.append(c)
    print(''.join(ans_list))

if __name__=='__main__':
    main()