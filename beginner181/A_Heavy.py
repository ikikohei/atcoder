# 問題文
# 高橋くんは今、白い服を着ています。

# 高橋くんは、白い服を着た次の日には黒い服を、黒い服を着た次の日には白い服を着ます。

# N日後には何色の服を着るでしょうか？

# 入力
# 入力は以下の形式で標準入力から与えられる。

# N

# 出力
# N日後に白い服を着るなら White を、黒い服を着るなら Black を出力せよ。

def judgeClothesColor(N):
        return "White" if N%2==0 else "Black"

def main():
        N = int(input())
        print(judgeClothesColor(N))

if __name__ == '__main__':
    main()