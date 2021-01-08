# set の in 演算子を使ってみるパターン
def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    s_set = set(s_list)
    for s in s_set:
        if "!" + s in s_set: return print(s)
    print("satisfiable")

if __name__ == "__main__":
    main()