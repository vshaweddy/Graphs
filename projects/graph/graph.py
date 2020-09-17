"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception("It's not a vertice.")

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue 
        queue = Queue()
        queue.enqueue(starting_vertex)
        # create an empty set for the visited verticies
        visited = set()

        # while the queue is not empty
        while queue.size() > 0:
            curr = queue.dequeue()

            # check if the current has been visited or not
            if curr in visited:
                return

            # print the current vertex
            print(curr)

            # add the current vertex to the visited set
            visited.add(curr)

            # change the current vertex to the current vertex's neighbor
            neighbors = self.get_neighbors(curr)

            # add all the neighbors to the queue
            for neighbor in neighbors:
                queue.enqueue(neighbor)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        stack = Stack()
        stack.push(starting_vertex)
        # create an empty set for the visited verticies
        visited = set()

        # while the queue is not empty
        while stack.size() > 0:
            curr = stack.pop()

            # check if the current has been visited or not
            if curr in visited:
                return

            # print the current vertex
            print(curr)

            # add the current vertex to the visited set
            visited.add(curr)

            # change the current vertex to the current vertex's neighbor
            neighbors = self.get_neighbors(curr)

            # add all the neighbors to the queue
            for neighbor in neighbors:
                stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create an empty set for the visited verticies
        visited = set()

        def helper(vertex):
            # check if the vertex is visited to break the recursion 
            if vertex in visited:
                return

            print(vertex)
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)

            for neighbor in neighbors:
                helper(neighbor)  

        helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue of paths
        queue = Queue()

        # add the starting to the queue but store it in a list
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            # get the first path in queue
            path = queue.dequeue()

            # get the last vertice to check if it's the destination
            node = path[-1]

            if node == destination_vertex:
                return path

            # enumerate all neighbors, constuct a new path and push it to queue
            for neighbor in self.vertices.get(node, set()):
                # create a new path from the previous path
                new_path = list(path)

                # add the new node to the new path
                new_path.append(neighbor)

                # add the new path to the que
                queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
