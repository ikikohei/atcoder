# this method is disable because of memori over
def main():
    n,prime_c = map(int,input().split())
    max_days = 10**9+1
    cost_list = [0]*(max_days)
    for i in range(n):
        a,b,c = map(int,input().split())
        cost_list[a-1] += c
        cost_list[b] -= c
    minimum_cost = 0
    daily_cost = 0
    for i in range(max_days-1):
        daily_cost += cost_list[i]
        minimum_cost += min(daily_cost,prime_c)
    print(minimum_cost)

if __name__ == "__main__":
    main()