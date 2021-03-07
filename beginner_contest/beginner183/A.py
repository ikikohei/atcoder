def ReLU(x):
    return x if x >= 0 else 0

def main():
    x = int(input())
    print(ReLU(x))

if __name__=='__main__':
    main()