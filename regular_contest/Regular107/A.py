from decimal import *
def sumNum(n):
    return int(Decimal("0.5")*Decimal(n)*(Decimal("1")+Decimal(n)))

def main():
    deviser = 998244353
    a, b, c = input().split()
    print(int((sumNum(a)*sumNum(b)*sumNum(c))%deviser))

if __name__ == "__main__":
    main()
