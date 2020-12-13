def main():
    n, m = map(int,input().split())
    if m == 0: return print(1)
    blue_list = list(map(int,input().split()))
    blue_list.sort()
    print(blue_list)
    white_size_list = []
    if blue_list[0]-1 != 0:
        white_size_list.append(blue_list[0]-1)
    for bi in range(1,m):
        if blue_list[bi]-blue_list[bi-1]-1 != 0:
            white_size_list.append(blue_list[bi]-blue_list[bi-1]-1)
    if n-blue_list[-1] != 0:
        white_size_list.append(n-blue_list[-1])
    if len(white_size_list) > 0:
        stamp = min(white_size_list)
    stamp_count = 0
    for white in white_size_list:
        stamp_count += white // stamp
        if white % stamp != 0:
            stamp_count += 1
    print(stamp_count)
    
if __name__=='__main__':
    main()

    

    