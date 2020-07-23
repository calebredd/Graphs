"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
#self.vertices = {
    # '0': {'1', '3'},
    # '1': {'0'},
    # '2': set(),
    # '3': {'0'}
# }
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
            # Adding 0 to the dictionary without any neighbors

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
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
# make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)

        # make a set to track visited nodes
        visited = set()

        # while queue still has things in it
        while q.size() > 0:
        ## dq from front of the line, this is our current node
            current_node = q.dequeue()
        ## check if we've visited, if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()

        # as long as our stack isn't empty
        while s.size() > 0:
        ## pop off the top, this is our current node
            current_node = s.pop()

        ## check if we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
        ### print it (in this case)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### and add them to our stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            ### get its neighbors
            neighbors = self.get_neighbors(starting_vertex)
            ### iterate over neighbors
            for neighbor in neighbors:
            #### and add them to our stack
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)

        # make a set to track visited nodes
        visited = []
        path = [starting_vertex]

        # while queue still has things in it
        previous_node = None
        current_node = None
        while destination_vertex != current_node:
            previous_node = current_node
            current_node = q.dequeue()
        ## dq from front of the line, this is our current node
        ## check if we've visited, if not:
            if current_node not in visited:
        ### mark it as visited
                visited.append(current_node)
                # print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors,
                if destination_vertex in neighbors:
                    if previous_node not in path:
                        path.append(previous_node)
                    if current_node not in path:
                        path.append(current_node)
                    if destination_vertex not in path:
                        path.append(destination_vertex)
                    current_node = destination_vertex
                else:
                    for neighbor in neighbors:
                        if destination_vertex in self.get_neighbors(neighbor):
                            if previous_node not in path:
                                path.append(previous_node)
                            if current_node not in path:
                                path.append(current_node)
                            if neighbor not in path:
                                path.append(neighbor)
                            if destination_vertex not in path:
                                path.append(destination_vertex)
                            current_node = destination_vertex
        #### add to queue
                        else:
                            q.enqueue(neighbor)
        return path 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = []

        # as long as our stack isn't empty
        while s.size() > 0 and destination_vertex not in visited:
        ## pop off the top, this is our current node
            current_node = s.pop()

        ## check if we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.append(current_node)
        ### print it (in this case)
                # print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### and add them to our stack
                    s.push(neighbor)
        # print(visited)
        return visited 
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def recursionFx(self, previous_node=None, current_node=starting_vertex, destination_vertex=destination_vertex, visited=[], path=[starting_vertex]):
    # as long as our stack isn't empty
            if destination_vertex not in visited:
            ## check if we have visited this before, and if not:
                if current_node not in visited:
            ### mark it as visited
                    visited.append(current_node)
            ### get its neighbors
                    neighbors = self.get_neighbors(current_node)
            ### iterate over neighbors
                    if destination_vertex in neighbors:
                        if previous_node not in path:
                            path.append(previous_node)
                        if current_node not in path:
                            path.append(current_node)
                        if destination_vertex not in path:
                            path.append(destination_vertex)
                        current_node = destination_vertex
                    else:
                        for neighbor in neighbors:
                            if destination_vertex in self.get_neighbors(neighbor):
                                if previous_node not in path:
                                    path.append(previous_node)
                                if current_node not in path:
                                    path.append(current_node)
                                if neighbor not in path:
                                    path.append(neighbor)
                                if destination_vertex not in path:
                                    path.append(destination_vertex)
                                current_node = destination_vertex
            ### and add them to our stack
                            recursionFx(self, current_node, neighbor, destination_vertex, visited)
            return path
        
        return recursionFx(self)

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
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
