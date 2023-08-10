from _LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        
        # Defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        # creating a new Linked List for each vertex/index of the list
        self.array = [LinkedList() for _ in range(vertices)]
    
    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            # As we are implementing a directed graph, (1,0) != (0,1)
            self.array[source].insert_at_head(destination)
            
            # Uncomment the below line if you want to create a undirected graph
            # self.array[destination].insert_at_head(source)
            
        # If we were to implement an undirected graph where (1,0) == (0,1)
        # we would create an edge from destination to source as well
        # self.array[destination].insert_at_head(source)
        
    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print()
        
        for i in range(self.vertices):
            print("|", i, "| => ", end="")
            temp = self.array[i].get_head()
            
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            
            print("None")

if __name__ == "__main__":
    graph = Graph(4)
    
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    
    graph.print_graph()
    print(graph.array[1].get_head().data)