def main():
    s = input()
    char_map = {}
    before_char = None
    ans = 0
    for num in range(len(s)):
        if s[-1-num] in char_map:
            char_map[s[-1-num]] += 1
        else:
            char_map[s[-1-num]] = 1
        if before_char == s[-1-num]:
            ans += num + 1 - char_map[s[-1-num]]
            char_map = {}
            char_map[s[-1-num]] = num + 1
        before_char = s[-1-num]
    print(ans)

if __name__=='__main__':
    main()

        
    