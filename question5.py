"""
The file to implememt the question 5 the TSP algorithm
"""

#imports 
import os
import itertools

#import src.utils as utils
#from src.graph import Graph

#define the class 
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, nx_graph=None, multi_graph=False, di_graph=False):
        if nx_graph:
            self.g = nx_graph
        elif multi_graph:
            self.g = nx.MultiGraph()
        elif di_graph:
            self.g = nx.DiGraph()
        else:
            self.g = nx.Graph()

    def add_node_list(self, node_list):
        self.g.add_weighted_edges_from(node_list)

    def node_count(self):
        return self.g.number_of_nodes()

    def edge_count(self):
        return self.g.number_of_edges()

    def get_edges(self):
        return self.g.edges

    def get_edge_weight(self, node1, node2):
        return self.g.get_edge_data(node1, node2)["weight"]

    def get_nodes(self):
        return self.g.nodes

    def get_degree(self):
        return self.g.degree

    def add_edge(self, node1, node2, weight=None):
        if weight:
            self.g.add_edge(node1, node2, weight=weight)
        else:
            self.g.add_edge(node1, node2)

    def has_edge(self, node1, node2):
        return self.g.has_edge(node1, node2)

    def remove_node(self, node):
        return self.g.remove_node(node)

    def get_graph(self):
        return self.g

    def plot_graph(self, output_path):
        pos = nx.spring_layout(self.g)
        nx.draw(self.g, pos, with_labels=True)
        # labels
        if isinstance(self.g, nx.MultiGraph):
            labels = {}
        else:
            labels = {e: str(self.get_edge_weight(e[0], e[1])) for e in self.g.edges}
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=labels, font_size=5)

        if isinstance(self.g, nx.DiGraph):
            nx.draw_networkx_edges(self.g, pos, edgelist=self.g.edges, arrows=True)
        plt.savefig(output_path)
        plt.close()

    def get_euler_tour(self, source_node):
        return nx.algorithms.eulerian_circuit(self.g, source=source_node)



def create_graph_from_txt_file(txt_file: str):
    #file reading line to line 
    nodes = []
    with open(txt_file) as file:
        line = file.readline()
        counter = 0
        while line:
            if counter ==0 and type(line) == str: 
                num_nodes = line  
                counter +=1
            else:
                n_info = line.replace("\n", "").split(" ")
                nodes.append((n_info[0], n_info[1], n_info[2]))

            line = file.readline()

    if len(nodes) > 0:
        g = Graph()
        g.add_node_list(nodes)
        return g

    raise Exception("Wrong input file provided")


def get_mst(graph: Graph):
    # Kruskal's algorithm
    edges = graph.get_edges()
    weighted_edges = {}
    for (u, v) in edges:
        weighted_edges[(u, v)] = float(graph.get_edge_weight(u, v))

    # sort edges by weight, by value
    weighted_edges = sorted(weighted_edges.items(), key=lambda x: x[1])

    mst_graph = Graph()
    nodes = []
    for itm in weighted_edges:
        u, v = itm[0]
        mst_graph.add_edge(u, v, graph.get_edge_weight(u, v))
        try:
             nx.algorithms.find_cycle(mst_graph.get_graph())
             mst_graph.get_graph().remove_edge(u, v)
        except nx.NetworkXNoCycle:
            nodes.append(u)
            nodes.append(v)

    return mst_graph


def get_degrees(graph: Graph):
    degrees = {}

    for d in graph.get_degree():
        degrees[d[0]] = d[1]

    return degrees


def get_nodes_odd_degrees(degrees: dict):
    odd_degrees = {}

    for k in degrees.keys():
        if (degrees[k]%2) !=0:
            odd_degrees[k] = degrees[k]

    return odd_degrees


def print_edges_with_weight(graph: Graph):
    if isinstance(graph.get_graph(), nx.MultiGraph):
        for e in graph.get_edges():
            print(f"Edge : ({e[0]},{e[1]})")
    else:
        for e in graph.get_edges():
            print(f"Edge : ({e[0]},{e[1]}) = {graph.get_edge_weight(e[0], e[1])}")


def convert_edges_tuples_to_dict(nodes, edges_tuples):
    edges = {}

    # add all nodes as keys
    for n in nodes:
        edges[n] = []

    for e in edges_tuples:
        edges[e[0]].append((e[1]))
        edges[e[1]].append((e[0]))

    return edges


def create_subgraph(graph: Graph, nodes_to_include):
    subgraph = nx.Graph(graph.get_graph().subgraph(nodes_to_include))
    return Graph(subgraph)


def create_minimum_weight_perfect_matching(graph: Graph):
    # create new graph with negative weight
    new_graph = Graph()
    for e in graph.get_edges():
        new_graph.add_edge(e[0], e[1], -float((graph.get_edge_weight(e[0], e[1]))))

    set_matching = nx.max_weight_matching(new_graph.get_graph(), maxcardinality=True)

    matching_graph = Graph()
    for m in set_matching:
        matching_graph.add_edge(m[0], m[1], graph.get_edge_weight(m[0], m[1]))

    return matching_graph


def union_graphs(graph1: Graph, graph2: Graph):

    multi_graph = Graph(multi_graph=True)
    for e in graph1.get_edges():
        multi_graph.add_edge(e[0], e[1])

    for e in graph2.get_edges():
        multi_graph.add_edge(e[0], e[1])

    return multi_graph


def get_total_cost(graph, path):
    weight = 0
    for i in range(1, len(path)):
        weight += float(graph.get_edge_weight(path[i-1], path[i]))
    return weight


if __name__ == '__main__':

    #file reading 
    txt_file = r"input_7.txt"
    debug_folder = r"output/1/"
    source_node = "0"
    debug = False



    # create graph from input txt file
    initial_g = create_graph_from_txt_file(txt_file)
    if debug:
        print("Initial Graph:")
        print_edges_with_weight(initial_g)
        initial_g.plot_graph(os.path.join(debug_folder, "graph.png"))


    # create a MST
    mst_graph = get_mst(initial_g)
    if debug:
        print("\nMST:")
        print_edges_with_weight(mst_graph)
        mst_graph.plot_graph(os.path.join(debug_folder, "mst.png"))

    mst_degrees = get_degrees(mst_graph)
    if debug:
        print(f"\nMST degree : {mst_degrees}")

    odd_degrees = get_nodes_odd_degrees(mst_degrees)
    if debug:
        print(f"\nMST odd degree : {odd_degrees}")

    subgraph = create_subgraph(initial_g, odd_degrees)
    if debug:
        print("\nSubgraph:")
        print_edges_with_weight(subgraph)
        subgraph.plot_graph(os.path.join(debug_folder, "subgraph.png"))

    minimum_perfect_match = create_minimum_weight_perfect_matching(subgraph)
    if debug:
        print("\nMinimum weight perfect match:")
        print_edges_with_weight(minimum_perfect_match)
        minimum_perfect_match.plot_graph(os.path.join(debug_folder, "minimum_perfect_match.png"))

    union_graph = union_graphs(mst_graph, minimum_perfect_match)
    if debug:
        print("\nUnion graph details:")
        print_edges_with_weight(union_graph)
        union_graph.plot_graph(os.path.join(debug_folder, "union_graph.png"))

    euler_tour_itr = union_graph.get_euler_tour(source_node)
    euler_tour = []
    for e in euler_tour_itr:
        euler_tour.append(e)

    if debug:
        print(f"\n Euler tour: {euler_tour}")

        #initializzation of the object 
        euler_g = Graph()
        for e in euler_tour:
            euler_g.add_edge(e[0], e[1], initial_g.get_edge_weight(e[0], e[1]))
        euler_g.plot_graph(os.path.join(debug_folder, "euler_tour.png"))

    euler_tour = list(itertools.chain.from_iterable(list(euler_tour)))
    euler_tour = list(dict.fromkeys(euler_tour).keys())
    euler_tour.append(source_node)

    print(f"\nPath: {euler_tour}")
    if debug:
        final_path = Graph(di_graph=True)
        for i in range(len(euler_tour)-1):
            final_path.add_edge(euler_tour[i],
                                euler_tour[i+1],
                                initial_g.get_edge_weight(euler_tour[i], euler_tour[i+1]))
        final_path.plot_graph(os.path.join(debug_folder, "output.png"))

    total_weight = get_total_cost(initial_g, euler_tour)
    
    print(f"Total traveling cost : {total_weight}")