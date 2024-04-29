import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Graph:
    def __init__(self):
        """
        Initialize an empty graph with an adjacency list, which is a dictionary.
        """
        self.adj_list = {}

    def add_undirected_edge(self, node1, node2):
        """
        Add an undirected edge between node1 and node2.

        :param node1: First node in the pair to connect.
        :param node2: Second node in the pair to connect.
        """
        # If the nodes are not in the adjacency list, initialize them with an empty list
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        if node2 not in self.adj_list:
            self.adj_list[node2] = []

        # Add the node2 as a neighbor of node1 and vice versa since the graph is undirected
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def print_adj_list(self):
        """
        Print the adjacency list of each node in the graph.
        """
        for node, edges in self.adj_list.items():
            print(f"{node}: {edges}")

    def draw_graph(self):
        """
        Visualize the graph using networkx and matplotlib.
        """
        g = nx.Graph(self.adj_list)

        # Draw the graph
        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10)

        plt.show()

    def bfs_traversal(self, start_node):
        """
        Perform BFS traversal starting from the start_node.

        :param start_node: The starting node for BFS traversal.
        :return: A list of nodes in the order they were visited.
        """
        visited = []
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                visited.append(current_node)
                adjacent_nodes = self.adj_list.get(current_node, [])  # get or default

                # Add adjacent, unvisited nodes to the queue
                for next_node in adjacent_nodes:
                    if next_node not in visited:
                        queue.append(next_node)

        return visited

    def bfs_visualization(self, start_node):
        """
        Visualize the BFS traversal process, highlighting visited nodes.

        :param start_node: The starting node for BFS traversal.
        """
        visited = set()
        queue = deque([start_node])
        g = nx.Graph(self.adj_list)  # initialize network graph with our own

        pos = nx.spring_layout(g)  # positions for all nodes

        # Function to draw the graph
        def draw_graph(highlight_nodes):
            plt.clf()  # clear the plot to redraw
            nx.draw(g, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10)
            nx.draw_networkx_nodes(g, pos, nodelist=highlight_nodes, node_color='red')
            plt.pause(1)  # pause to show the updated graph

        draw_graph([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                draw_graph(list(visited))  # update drawing with the current visited node
                queue.extend([node for node in self.adj_list[current_node] if node not in visited])

        plt.show()  # display


graph = Graph()

# Add edges as the floor plan
graph.add_undirected_edge(1, 2)
graph.add_undirected_edge(2, 3)
graph.add_undirected_edge(3, 8)
graph.add_undirected_edge(8, 9)
graph.add_undirected_edge(9, 10)
graph.add_undirected_edge(10, 5)
graph.add_undirected_edge(5, 4)
graph.add_undirected_edge(1, 6)
graph.add_undirected_edge(6, 11)
graph.add_undirected_edge(11, 12)
graph.add_undirected_edge(12, 17)
graph.add_undirected_edge(17, 22)
graph.add_undirected_edge(17, 16)
graph.add_undirected_edge(16, 21)
graph.add_undirected_edge(12, 7)
graph.add_undirected_edge(7, 8)
graph.add_undirected_edge(8, 13)
graph.add_undirected_edge(13, 18)
graph.add_undirected_edge(18, 23)
graph.add_undirected_edge(23, 24)
graph.add_undirected_edge(24, 25)
graph.add_undirected_edge(10, 15)
graph.add_undirected_edge(15, 20)
graph.add_undirected_edge(20, 19)
graph.add_undirected_edge(19, 14)


# graph.print_adj_list()
graph.draw_graph()

# Perform BFS and print all completed paths
traversal_result = graph.bfs_traversal(1)
print("BFS Traversal from chamber 1:", traversal_result)

graph.bfs_visualization(1)
