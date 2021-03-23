def main():
    n = int(input())
    c_matrix = []
    for _ in range(n):
        c_list = list(map(int, input().split()))
        c_matrix.append(c_list)
    for i in range(n-1):
        for j in range(n):
            tmp_diff = c_matrix[j][i+1] - c_matrix[j][i]
            if j == 0:
                diff = tmp_diff
                continue
            if tmp_diff != diff:
                return print("No")
    mini = 10**19
    for i in range(n):
        s = sum(c_matrix[i])
        if s < mini:
            mini = s
            mini_index = i
    a = []
    for j in range(n):
        a.append(c_matrix[j][0] - c_matrix[mini_index][0])
    print("Yes")
    print(" ".join(map(str,a)))
    print(" ".join(map(str,c_matrix[mini_index])))

if __name__=="__main__":
    main()
            
        