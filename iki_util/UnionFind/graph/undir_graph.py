#頂点iと頂点jを編で接続
def connect(graph, i, j):
    graph[i][j] = 1
    graph[j][i] = 1

#display the information of graph
def pretty_print(graph,n):
    print("   ", end = "")
    for i in range(0, n):
        print(i, " ", end = "")
    print("")
    for i in range(0, n):
        print(i, " ", end = "")
        for j in range(0, n):
            print(graph[i][j], " ", end = "")
        print("")

if __name__ == "__main__":
    # number fo vertexes
    N = 5

    # generate and initialize graph
    graph = [[0 for i in range(0, N)] for j in range(0, N)]

    # set the edge (sample)
    connect(graph,0,1)
    connect(graph, 0, 4)
    connect(graph, 1, 2)
    connect(graph, 1, 3)
    connect(graph, 1, 4)
    connect(graph, 2, 3)
    connect(graph, 3, 4)

    #display the graph
    pretty_print(graph, N)
