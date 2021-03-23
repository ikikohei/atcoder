def fucntion(x, a_list, t_list, index):
    if t_list[index] == 1:
        x = x + a_list[index]
    if t_list[index] == 2:
        x = max(x, a_list[index])
    if t_list[index] == 3:
        x = min(x, a_list[index])
    if index == len(a_list) - 1:
        print(x)
        return x
    fucntion(x, a_list, t_list, index+1)


def main():
    n = int(input())
    a_list = []
    t_list = []
    for _ in range(n):
        a, t = map(int, input().split())
        a_list.append(a)
        t_list.append(t)
    q = int(input())
    x_list = list(map(int, input().split()))
    for i in range(q):
        fucntion(x_list[i], a_list, t_list, 0)

if __name__=='__main__':
    main()