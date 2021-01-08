def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s = input()
        if s[0] == "!":
            s = s.replace("!","")
            s += "!"
        s_list.append(s)
    s_list = list(set(s_list))
    s_list.sort()
    # print(s_list)
    for i in range(len(s_list)-1):
        if s_list[i] + "!" == s_list[i+1]:
            return print(s_list[i])
    print("satisfiable")

if __name__ == "__main__":
    main()