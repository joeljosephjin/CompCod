# Problem: find if there is a cycle in an undirected graph
# Solution: do DFS and see if it meets a visited node (other than its immediate parent)

def f(A,B):
    """
    A: no. of nodes
    B: list of pairs of nodes which are connected
    """
    adj={}
    # create the adjacency matrix
    for a,b in B:
        # adj = {1:[2,3], 2:[1,3], 3:[1,2]}
        if a in adj: adj[a].append(b)
        else: adj[a]=[b]
        if b in adj: adj[b].append(a)
        else: adj[b]=[a]

    # indicating a visitedness for each node
    vis = [0]*A

    # is the node with a certain parent cyclic or not
    # parent helps us exclude it from a "visited" guy
    def isCyclic(n, parent):
        # mark the node as visited
        vis[n-1]=True
        # for each adjacent node
        for i in adj[n]:
            # if it is not visited, i am interested
            if vis[i-1]==0:
                # recursively check if the child node is cyclic
                if isCyclic(i,n):
                    return True
            # base case
            # if it is visited, then it could be the parent node too, if its not, then it means it is cyclic
            elif i!=parent:
                return True
        # if 
        return False


    # double check each node
    for i in range(1,A+1):
        # if it is already visited, we don't go to that node
        if vis[i-1]==0:
            # if the node is isolated, just let it be
            if i in adj:
                # checks if that node is cyclic
                if isCyclic(i,-1):
                    return 1

    return 0       




# A=5
# B=[[1, 2],
#     [1, 3],
#     [2, 3],
#     [1, 4],
#     [4, 5]
#     ]

A = 3
B = [[1, 2],
    [1, 3]
    ]


# A = 88
# B = [[6, 45],
#   [29, 81],
#   [7, 8],
#   [67, 76],
#   [40, 76],
#   [7, 73],
#   [9, 20],
#   [56, 63],
#   [52, 57],
#   [22, 31],
#   [26, 76],
#   [14, 58],
#   [31, 69],
#   [30, 31],
#   [56, 85],
#   [22, 57],
#   [12, 42],
#   [19, 78],
#   [12, 85],
#   [72, 85],
#   [3, 41],
#   [32, 87],
#   [31, 48],
#   [17, 81],
#   [2, 63],
#   [25, 78],
#   [49, 51],
#   [30, 61],
#   [7, 54],
#   [79, 80],
#   [23, 37],
#   [25, 32],
#   [54, 63],
#   [7, 28],
#   [41, 58],
#   [45, 52],
#   [77, 78],
#   [26, 53],
#   [54, 83],
#   [26, 75],
#   [61, 72],
#   [57, 82],
#   [9, 36],
#   [30, 73],
#   [12, 17],
#   [24, 55],
#   [47, 68],
#   [12, 64],
#   [35, 77],
#   [33, 86],
#   [2, 50],
#   [17, 41],
#   [27, 70],
#   [7, 43],
#   [62, 73],
#   [3, 60],
#   [49, 58],
#   [32, 52],
#   [26, 73],
#   [13, 78],
#   [8, 68],
#   [17, 68],
#   [34, 51],
#   [48, 51],
#   [8, 11],
#   [31, 78],
#   [22, 53],
#   [2, 64],
#   [71, 80],
#   [11, 81],
#   [86, 88],
#   [9, 67],
#   [6, 18],
#   [40, 53],
#   [52, 77],
#   [21, 52],
#   [47, 71],
#   [48, 50],
#   [16, 76],
#   [16, 86],
#   [3, 71],
#   [10, 59],
#   [33, 73],
#   [52, 68],
#   [24, 66],
#   [32, 72],
#   [3, 4],
#   [34, 35],
#   [57, 76],
#   [25, 33],
#   [20, 59],
#   [29, 44],
#   [50, 56],
#   [41, 82],
#   [25, 85],
#   [17, 35],
#   [34, 52],
#   [62, 68],
#   [5, 26],
#   [13, 39],
#   [25, 56],
#   [5, 12],
#   [85, 87],
#   [20, 86],
#   [63, 80],
#   [6, 53],
#   [28, 78],
#   [47, 65],
#   [28, 64],
#   [7, 51],
#   [41, 59]
# ]


print(f(A,B))