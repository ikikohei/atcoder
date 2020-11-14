def TrapezoidSum(A,B):
        if (B-A+1)%2 == 0: return (A+B)*(B-A+1)/2
        else: return (A+B)*(B-A)/2+(A+B)/2

if __name__ == '__main__':
    N = int(input())
    ans_sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        ans_sum += TrapezoidSum(A,B)
    print(int(ans_sum))