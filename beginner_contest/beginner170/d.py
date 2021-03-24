def main():
    # from collections import defaultdict
    n = int(input())
    a_list = list(map(int, input().split()))
    # a_dict = defaultdict(int)
    a_dict = {}
    for a in a_list:
        if a not in a_dict:
            a_dict[a] = 1
        else:a_dict[a] += 1
    ans = n
    for a in a_list:
        index = 1
        while index * index <= a:
            if a == 1:
                if a_dict[1] > 1:
                    ans -= 1
                break
            elif index == 1:
                if index in a_dict or a_dict[a//index] > 1:
                    ans -=1
                    break
            elif a % index == 0:
                if index in a_dict or a//index in a_dict:
                    ans -= 1
                    break
            index += 1
    print(ans)

if __name__=="__main__":
    main()
    
        