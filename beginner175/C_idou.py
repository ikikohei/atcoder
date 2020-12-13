def main():
    X, K, D = map(int,input().split())
    base_num = abs(X)//D
    if K <= base_num:
        return print(abs(X) - D * K)
    if base_num % 2 == K % 2:
        return print(abs(X) - base_num * D)
    else:
        return print(abs(abs(X) - (base_num+1)*D))

if __name__=='__main__':
    main()


    
