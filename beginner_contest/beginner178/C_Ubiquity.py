def Ubiquity(N):
    const = 10**9 + 7
    allEvents = 10**N
    return (allEvents - 2*9**N + 8**N) % const

def main():
    N = int(input())
    print(Ubiquity(N))

if __name__=='__main__':
    main()