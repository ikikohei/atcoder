def calculateMahattanDist(positions):
    manhattanDist = 0
    for ps in positions:
        manhattanDist += abs(ps)
    return manhattanDist

def calculateEuclidDist(positions):
    import math
    euclidDist = 0
    for ps in positions:
        euclidDist += ps*ps    
    euclidDist = math.sqrt(euclidDist) 
    return euclidDist

def calculateChebyshev(positions):
    chebyshevDist = 0
    for ps in positions:
        if abs(ps) > chebyshevDist:
            chebyshevDist = abs(ps)
    return chebyshevDist

def main():
    N = int(input())
    positions = []
    positions = list(map(int, input().split()))
    print(calculateMahattanDist(positions))
    print(calculateEuclidDist(positions))
    print(calculateChebyshev(positions))

if __name__ == '__main__':
    main()
    

    
