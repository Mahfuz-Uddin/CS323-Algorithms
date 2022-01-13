# Analysis of Algorithms - CSCI 323
# Assignment 2
# Mahfuz Uddin




import sys
import timeit
from prettytable import PrettyTable

global ComparisonCount
ComparisonCount = 0


def read_file_to_matrix(file_name):
    f = open(file_name + '.txt', 'r')
    each_line = f.readlines()

    num_of_vertice = len(each_line)
    rows, cols = (num_of_vertice, num_of_vertice)
    matrix = [[float('inf') for i in range(cols)] for j in range(rows)]

    for i in range(len(each_line)):
        from_ = int(each_line[i][0])
        toAndCost = each_line[i][3:]
        n = toAndCost.split(',')
        for k in n:
            to, cost = k.split()
            to = int(to)
            cost = int(cost)
            matrix[from_][to] = cost
    return matrix


for i in read_file_to_matrix('input'):
    print(i)


#### KRUSAL ####
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


# Does union of i and j. It returns
# false if i and j are already in same
# set.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b


# Finds MST using Kruskal's algorithm
def kruskalMST(cost, V, INF):
    global ComparisonCount
    print('\nKruskal MST\n')
    mincost = 0  # Cost of min MST
    table = PrettyTable(['Progress'])
    vertex = []
    MST = []
    for e in range(V):
        MST.append(float('inf'))
    print(MST)
    addedEdge = []
    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i

    # Include minimum weight edges one by one
    edge_count = 0
    tempArr= []
    ComparisonCount += 1
    while edge_count < V - 1:
        ComparisonCount += 1
        min = INF
        a = -1
        b = -1
        print(tempArr)

        for i in range(V):
            for j in range(V):
                ComparisonCount += 2
                if find(i) != find(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        tempArr.append(a)
        print('Newly added', a)
        union(a, b)

        print('Edge {} to {} with cost:{}'.format(a, b , min))
        edge_count += 1
        mincost += min

    print("The Minimum Cost of the MST is {}\n".format(mincost))


### END OF KRUSAL ###

### PRISM ###
class GraphPrism:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        totalweight = 0
        print('\nPrism MST\n')
        print("Edge \tWeight")
        for i in range(1, self.V):
            print('Edge {} to {} with cost:{}'.format(parent[i], i, self.graph[i][parent[i]]))
            totalweight += self.graph[i][parent[i]]
        print('The total weight of the MST is', totalweight)

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
        global ComparisonCount
        # Initialize min value
        min = float('inf')

        for v in range(self.V):
            ComparisonCount += 2
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [float('inf')] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                global ComparisonCount
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                ComparisonCount += 3
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    print('Vertex', v, '\tMST', key, '\t\t a Newly added Edge:', key[v])
                    for k in key:
                        # print (k)
                        parent[v] = u

        self.printMST(parent)


### END OF PRISM ###

timedata_for_prism = []
comparisons_for_prism = []
timedata_for_kruskal = []
comparisons_for_kruskal = []


def timer_for_prism(theFunction, timedata_for_x, comparisons_for_x):
    global ComparisonCount
    ComparisonCount = 0
    for test in range(2):
        t = timeit.timeit(lambda: theFunction(), number=1)
        timedata_for_x.append(t)
        comparisons_for_x.append(ComparisonCount)
        ComparisonCount = 0


def timer_for_kruskal(theFunction, timedata_for_x, comparisons_for_x, cost, V, INF):
    global ComparisonCount
    ComparisonCount = 0
    for test in range(2):
        t = timeit.timeit(lambda: theFunction(cost, V, INF), number=1)
        timedata_for_x.append(t)
        comparisons_for_x.append(ComparisonCount)
        ComparisonCount = 0


table = PrettyTable(['Time_For_Prism_MST', 'Comparisons_For_Prism_MST', 'Time_For_Kruskal_MST',
                     'Comparisons_For_Kruskal_MST'])
# for prism
g = GraphPrism(10)
g.graph = read_file_to_matrix('input')
timer_for_prism(g.primMST, timedata_for_prism, comparisons_for_prism)

print('\n\n')
# for Kruskal
V = 10
parent = [i for i in range(V)]
INF = float('inf')
cost = read_file_to_matrix('input')

timer_for_kruskal(kruskalMST, timedata_for_kruskal, comparisons_for_kruskal, cost, V, INF)

for x in range(2):
    table.add_row(
        [timedata_for_prism[x], comparisons_for_prism[x], timedata_for_kruskal[x], comparisons_for_kruskal[x]])
print("This data is for 5 trails of Prism and Krusal MST")
print(table)
