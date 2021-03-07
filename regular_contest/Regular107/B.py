def main():
    n, k = map(int,input().split())
    num_list = [0]*(2*n-1)
    for i in range(n):
        num_list[i]=i+1
        num_list[-(i+1)]=i+1
    # print(num_list)
    loop_num = 2*n-abs(k)-1
    ans = 0
    for j in range(loop_num):
        ans += num_list[j] * num_list[j+abs(k)]
    return print(ans)
        
if __name__ == "__main__":
    main()