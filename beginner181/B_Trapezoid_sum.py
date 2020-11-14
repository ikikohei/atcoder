# 時間超過のためNG。改善策を考える必要あり
# for 文内に for 文いるから、 O(n^2) になってる。。。
def TrapezoidSum(A,B):
    return sum([k for k in range(A, B+1)])

if __name__ == '__main__':
    N = int(input())
    ans_sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        ans_sum += TrapezoidSum(A,B)
    print(ans_sum)