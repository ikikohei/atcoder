def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_max = 0
    pre_max = 0
    for i in range(n):
        a_max = max(a[i],a_max)
        print(max(pre_max,a_max*b[i]))
        pre_max = max(pre_max,a_max*b[i]) 

if __name__ == "__main__":
    main()

