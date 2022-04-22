"""
authors: Godasree Mamilla, Akshat Sharma
"""

import  math
import sys
inf = 10086

path=""

def dfs(visited_nodes, graph, node,path):

    if node not in visited_nodes:
        file1 = open("output.txt","a")
        file1.write(str(node)+" ")
        file1.close()
        print(str(node), end=" --> ")
        visited_nodes.append(node)
        stack.append(node)
        for neighbour in graph[node]:
            dfs(visited_nodes, graph,neighbour, path)


if __name__ == "__main__":
    f = open("weighted_graph.txt", "r")
    graph_content = f.read()
    f.close()
    graph_content = graph_content.strip()
    graph_split = graph_content.split("\n")
    vertices_no = int(graph_split[0].strip())
    mgraph = []
    for i in range(vertices_no):
        col = []
        for j in range(vertices_no):
            col.append(inf)
        mgraph.append(col)
    for i in range(vertices_no):
        mgraph[i][i] = 0
    for i in range(1, len(graph_split)):
        graph_edges = graph_split[i].strip().split(" ")
        if (int(graph_edges[0]) in range(0, vertices_no) and int(graph_edges[1]) in range(0, vertices_no)):
            mgraph[int(graph_edges[0])][int(graph_edges[1])] = float(graph_edges[2])
            mgraph[int(graph_edges[1])][int(graph_edges[0])] = float(graph_edges[2])
        else:
            print("enter the valid edges or vertices no")
            sys.exit("enter the valid edges or vertices_no")
    print("our graph "+ str(mgraph))
    selected_vertices = []
    selected_edges={}
    count = 0;
    for i in range(0,vertices_no):
        selected_vertices.append(False)
        #selected_vertices[i] = False
    min_value = inf
    edge_value = min_value
    edge = ""
    for i in range(0,vertices_no):
        for j in range(i+1,vertices_no):
            if(min_value>mgraph[i][j]):
                min_value = mgraph[i][j]
                edge = str(i) +" " + str(j)
    initial_vertices = edge.split()
    selected_edges[edge] = min_value
    no_of_edges = 1
    selected_vertices[int(initial_vertices[0])] = True
    selected_vertices[int(initial_vertices[1])] = True
    while(no_of_edges<vertices_no-1):
        min_value = inf
        vertex2 = 0
        edge = ""
        for i in range(0,vertices_no):
            if(selected_vertices[i]):
                for j in range(0,vertices_no):
                    if(not selected_vertices[j]):
                          if(min_value>mgraph[i][j]):
                              min_value = mgraph[i][j]
                              edge = str(i) + " " + str(j)
                              vertex2 = j
        selected_vertices[vertex2] = True
        no_of_edges = no_of_edges + 1
        selected_edges[edge] = min_value
    print("our MST "+ str(selected_edges))
    adj_list = {}
    for i in range(0,vertices_no):
        adj_list[i] = []
    for key in selected_edges:
        keysplit = key.split(" ")
        adj_list[int(keysplit[0])].append(int(keysplit[1]))
        adj_list[int(keysplit[1])].append(int(keysplit[0]))
    print("our adjacency list "+str(adj_list))
    odd_vertices = []
    for key in adj_list:
        if(int(len(adj_list[key]))%2!=0):
            odd_vertices.append(key)

    print(odd_vertices)
    #print(odd_vertices[0])
    perfect_match = {}
    while(odd_vertices):
        min_val = inf
        x = len(odd_vertices) + 1
        y = len(odd_vertices) + 1
        for i in range(0,len(odd_vertices)):
            for j in range(i+1,len(odd_vertices)):
                if(mgraph[int(odd_vertices[i])][int(odd_vertices[j])]<min_val):
                    min_val = mgraph[int(odd_vertices[i])][int(odd_vertices[j])]
                    x = int(odd_vertices[i])
                    y = int(odd_vertices[j])
        str1 = str(x)+" "+str(y)
        perfect_match[str1]=mgraph[x][y]
        #print(str1)
        odd_vertices.remove(x)
        odd_vertices.remove(y)
        #print(odd_vertices)
    print("perfect matching " + str(perfect_match))

    for key in perfect_match:
        keysplit = key.split(" ")
        if(int(keysplit[1]) not in adj_list[int(keysplit[0])]):
            adj_list[int(keysplit[0])].append(int(keysplit[1]))
            adj_list[int(keysplit[1])].append(int(keysplit[0]))

    #print(adj_list)

    print(adj_list)
    visited_nodes = []
    stack=[]
    print("our tour ", end =" ")
    file1 = open("output.txt", "w")
    file1.close()
    dfs(visited_nodes, adj_list, 0, path)
    print("0")
    file1 = open("output.txt", "a")
    file1.write(str(0))
    file1.close()
    f = open("output.txt", "r")
    tour = f.read()
    f.close()
    tour_list = tour.strip().split(" ")
    cost = 0
    #print(tour_list)
    for i in range(0,len(tour_list)-1):
        #print(cost)
        cost = cost + mgraph[int(tour_list[i])][int(tour_list[i+1])]
    print("cost of the tour is "+ str(cost))






