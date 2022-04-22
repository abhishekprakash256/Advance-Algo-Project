import  math
import sys

inf = 10086

if __name__ == "__main__":
    f = open("weighted_graph.txt", "r")
    graph_content = f.read()
    f.close()
    graph_content = graph_content.strip()
    graph_split = graph_content.split("\n")
    vertices_no = int(graph_split[0])
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
        #print(graph_edges[0])
        #print(type(graph_edges[0]))
        #print(graph_edges[1])
        #print(type(graph_edges[1]))
        if(int(graph_edges[0]) in range(0,vertices_no) and int(graph_edges[1]) in range(0,vertices_no)):
            mgraph[int(graph_edges[0])][int(graph_edges[1])] = float(graph_edges[2])
            mgraph[int(graph_edges[1])][int(graph_edges[0])] = float(graph_edges[2])
        else:
            print("enter the valid edges or vertices no")
            sys.exit("enter the valid edges or vertices_no")
    file2 = open("required_vertices.txt", "r")
    reqd_vert_read = file2.read()
    file2.close()
    reqd_vertices_content = reqd_vert_read.strip().split("\n")
    reqd_vertices = reqd_vertices_content[0].split(" ")
    reqd_vertices_dict={}
    reqd_vertices_list = []
    for i in range(0,len(reqd_vertices)):
        if int(reqd_vertices[i]) not in range(0,vertices_no):
            print("enter the valid required vertices")
            sys.exit("enter the valid required vertices")
        else:
            if (len(reqd_vertices) < 2):
                print("Atleast two required vertex should be present")
                sys.exit("Atleast two required vertex should be present")
            else:
                reqd_vertices_dict[reqd_vertices[i]] = False
    #print(reqd_vertices_dict)
    print("our graph " +str(mgraph))
    selected_vertices = []
    selected_edges={}
    count = 0;
    min_value = inf
    edge_value = min_value
    edge = ""
    for i in range(0,len(reqd_vertices)):
        for j in range(i+1,len(reqd_vertices)):
            if(min_value>mgraph[int(reqd_vertices[i])][int(reqd_vertices[j])]):
                min_value = mgraph[int(reqd_vertices[i])][int(reqd_vertices[j])]
                edge = reqd_vertices[i] +" " + reqd_vertices[j]
    initial_vertices = edge.split()
    selected_edges[edge] = min_value
    no_of_edges = 1
    reqd_vertices_dict[initial_vertices[0]] = True
    reqd_vertices_dict[initial_vertices[1]] = True
    #print(selected_vertices)
    #print(selected_edges)
    #print(reqd_vertices_dict)
    #print("edge "+edge+" edge weight "+str(min_value))
    while(no_of_edges<len(reqd_vertices)-1):
        min_value = inf
        vertex2 = 0
        edge = ""
        for i in range(0, len(reqd_vertices)):
             if(reqd_vertices_dict[reqd_vertices[i]]):
                for j in range(0,len(reqd_vertices)):
                    if(not reqd_vertices_dict[reqd_vertices[j]]):
                            if(min_value>mgraph[int(reqd_vertices[i])][int(reqd_vertices[j])]):
                                min_value = mgraph[int(reqd_vertices[i])][int(reqd_vertices[j])]
                                edge = reqd_vertices[i] +" " + reqd_vertices[j]
                                vertex2 = reqd_vertices[j]
        reqd_vertices_dict[vertex2] = True
        no_of_edges = no_of_edges + 1
        selected_edges[edge] = min_value
    print("metric steiner tree instance " +str(selected_edges))