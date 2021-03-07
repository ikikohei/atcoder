def main():
    n = int(input())
    n = 2**n
    tournament_list = list(map(int,input().split()))
    left_tree = tournament_list[0:n//2]
    right_tree = tournament_list[n//2:n]
    # print(left_tree)
    # print(right_tree)
    left_winner = max(left_tree)
    right_winner = max(right_tree)
    print(tournament_list.index(min(left_winner,right_winner))+1)
    
if __name__ == "__main__":
    main()