def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    money = 1000
    stocks = 0
    for i in range(n-1):
        if a_list[i+1] < a_list[i] and stocks > 0:
            money += stocks * a_list[i]
            stocks = 0
        if a_list[i+1] > a_list[i]:
            stocks += money // a_list[i]
            money -= a_list[i] * (money // a_list[i])
    money += stocks * a_list[n-1]
    print(money)

if __name__=="__main__":
    main()
