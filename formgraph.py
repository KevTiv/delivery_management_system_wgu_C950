# Name : Kevin Tivert
# Student ID: 001372496

# minimum distance value not yet included in shortest path tree
# O(n)
# Function used to compare the distance between the different 
# location present in the location list.
def minimum_distance(v, distance, visited):

    # Initilaize minimum distance for next node
    min_dist = float('inf')

    
    for v in range(v):
        if distance[v] < min_dist and visited[v] == False:
            min_dist = distance[v]
            min_index = v

    return min_index

# Class use to create graph
# This hraph will be used for the calculation of the truck's route.

# O([V+E]log V)
class FormGraph:

    # Constructor
    # O(1)
    # This function will create an empty graph object that will be 
    # used to determine the future truck route.
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # Add edges
    # O(1)
    #This function given location parameters will add a new 
    # edge to the graph. The graph format is a 2D matrix.
    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    # Remove edges
    # O(1)
    # This function given location parameters will set the given matrix 
    # points to -1 if the locations were used but not do anything 
    # if the matrix points were not used.
    def remove_edge(self, v1, v2):
        if self.graph[v1][v2] == 0:
            return
        self.graph[v1][v2] = -1
        self.graph[v2][v1] = -1

    # Get Distance
    # O(1)
    # This function will return a given matrix stored value. The values stored 
    # in the matrix is the distance between two location points in the graph. 
    def get_distance(self, v1, v2):
        return self.graph[v1][v2]

    # This function uses the greedy algorithm “Dijkstra’s algorithm” to compute 
    # the shortest path the trucks will use to deliver packages. This function 
    # iteratively makes a call for the function “minimum_distance ()” to find the 
    # shortest distances to the next location not yet visited and from this 
    # repetitive process create a ordered list of the new found shortest routes.
    # O([V+E]log V)
    def shortest_path(self, src):
        found_dist = [float('inf')] * self.V

        found_dist[src] = 0
        visited = [False] * self.V

        for count in range(self.V):

            # Find minimum distance from the set of vertices not yet processed.
            # u = src in first iteration
            u = minimum_distance(self.V, found_dist, visited)

            # Minimum distance vertex is set in shortest path tree
            visited[u] = True

            # Update distance to shortest
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and found_dist[v] > found_dist[u] + self.graph[u][v]:
                    found_dist[v] = round(found_dist[u] + self.graph[u][v], 1)

        return found_dist

    # Path is a complete graph, therefore we can run an optimization algorithm
    # through every slot (nodes) to find shortest path at every slot.
    # This function is use to make sure that the Dijkstra’s algorithm in 
    # “shortest_path ()” found the actual shortest path the first time this a 
    # redundant step to ensure the accuracy of the shortest path.
    # O([V+E]log V)
    def optimize_distance(self):
        optimal_distance = []
        for i in range(0, len(self.graph)):
            dist = self.shortest_path(i)
            optimal_distance.append(dist)
        return optimal_distance