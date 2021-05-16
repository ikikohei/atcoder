def main():
    s = input()
    import itertools
    num = 0
    static = []
    not_include = []
    undifined = []
    for c in s:
        if c == "o":
            static.append(num) 
        elif c == "x":
            not_include.append(num)
        else:
            undifined.append(num)
        num += 1
    if len(static) > 4:
        return print(0)
    if len(static) == 0 and len(undifined) == 0:
        return print(0)
    if len(static) == 4:
        return print(24)
    import copy
    additional = copy.copy(static)
    additional.extend(undifined)
    ans = 0
    from collections import defaultdict
    import math
    for ad in itertools.combinations_with_replacement(additional, 4 - len(static)):
        tmp_count = 24
        tmp = copy.copy(static)
        tmp.extend(ad)
        tmp_dict = defaultdict(int)
        for t in tmp:
            tmp_dict[t] += 1
        for n in tmp_dict.values():
            tmp_count = tmp_count // (math.factorial(n))
        # print(tmp_count)
        ans += tmp_count
    print(ans)

if __name__=="__main__":
    main()

        
        


        