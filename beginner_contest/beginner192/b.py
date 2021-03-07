def main():
    s = input()
    char_num = 1
    for char in s:
        if char_num % 2 == 0 and char.islower(): return print("No")
        elif char_num % 2 == 1 and char.isupper(): return print("No")
        char_num += 1
    return print("Yes")

if __name__=="__main__":
    main()
