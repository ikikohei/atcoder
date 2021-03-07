def makePluralForm(st):
    if st[-1] == "s":
        print(st + "es")
    else:
        print(st+"s")

def main():
    st = input()
    makePluralForm(st)

if __name__=='__main__':
    main()