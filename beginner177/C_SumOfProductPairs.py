def sumOfProductPairs(N,productlist):
    modNum = 10**9 + 7 
    ans = 0
    sumofproductlist = sum(productlist)
    # print(sumofproductlist)
    for i in range(N-1):
        sumofproductlist -= productlist[i]
        ans += productlist[i] * sumofproductlist
        ans = ans%modNum 
    return ans

def main():
    N = int(input())
    productlist = list(map(int,input().split()))
    print(sumOfProductPairs(N,productlist))

if __name__=='__main__':
    main()
        