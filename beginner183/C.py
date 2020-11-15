import itertools
itertools.permutations

def travel(N,times):
    routes = list(itertools.permutations(range(2,N+1)))
    # print(routes)
    alltime = 0
    alltimes = []
    for route in routes:
        alltime += times[0][route[0]-1]
        for i in range(len(route)):
            if i == len(route)-1:
                alltime += times[route[i]-1][0]
            else:
                alltime += times[route[i]-1][route[i+1]-1]
        # print(alltime)
        alltimes.append(alltime)    
        alltime = 0
    # print(alltimes)
    return alltimes

def main():
    N, K = map(int, input().split())
    times = []
    count = 0
    for i in range(N):
        l = list(map(int,input().split()))
        times.append(l)
    # print(times)
    alltimes = travel(N,times)    
    for at in alltimes:
        if at == K:
            count += 1
    print(count)

    
    


if __name__=='__main__':
    main()