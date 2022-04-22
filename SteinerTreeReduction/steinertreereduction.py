import  math
inf = 10086
"""
author : Godasree Mamilla(gm20dv)
"""
def startwith(start, mgraph):
    shortest_distance = []
    previous_node = []
    unvisited_nodes = []
    visited_nodes = []

    for i in range(0,len(mgraph)):
        shortest_distance.insert(i, math.inf)
        unvisited_nodes.insert(i, i)
        previous_node.insert(i,-1)
    shortest_distance[start] = 0.0
    visited_nodes.append(start)
    unvisited_nodes.remove(start)
    current_node = start
    while unvisited_nodes:
        count = 0
        for node in unvisited_nodes:
            if(mgraph[current_node][node] is not inf):
                if(shortest_distance[current_node]+mgraph[current_node][node] < shortest_distance[node]):
                    #print("mgraph dist"+str(mgraph[current_node][node]))
                    #print("short dis"+str(shortest_distance[current_node]))
                    #print(str(current_node)+"
                    # "+str(node))
                    shortest_distance[node] = round(mgraph[current_node][node]+shortest_distance[current_node],5)
                    #print(type(shortest_distance[node]))
                    #print(shortest_distance[node])
                    previous_node[node] = current_node
            else:
                count =count+1
        #if(count == len(unvisited_nodes)):
            #break
        min_value = float(shortest_distance[unvisited_nodes[0]])
        for node in unvisited_nodes:
            if(min_value >shortest_distance[node]):
                min_value = shortest_distance[node]
        min_index = []
        for node in unvisited_nodes:
            if(min_value == shortest_distance[node]):
                min_index.append(node)
        if(len(min_index)>2):
                prevnode_current = False
                for j in min_index:
                    if(previous_node[j] == current_node):
                        prevnode_current = True
                        min_node = j
                        break
                if prevnode_current:
                    current_node = min_node
                else:
                    current_node = min_index[0]
        else:
            current_node = min_index[0]
        visited_nodes.append(current_node)
        unvisited_nodes.remove(current_node)
    #print(shortest_distance)
    #print(previous_node)
    return shortest_distance


if __name__ == "__main__":
    f = open("weighted_graph.txt", "r")
    graph_content = f.read()
    graph_content = graph_content.strip()
    f.close()
    graph_split = graph_content.split("\n")
    vertices_no = int(graph_split[0].strip())
    mgraph = []
    for i in range(vertices_no):
        col = []
        for j in range(vertices_no):
            col.append(inf)
        mgraph.append(col)
    #print(mgraph)
    for i in range(vertices_no):
        mgraph[i][i] = 0
    file1 = open("metricsteinertree.txt", "w")
    file1.write("=============Metric steiner tree instance================\n")
    for i in range(1, len(graph_split)):
        graph_split[i] = graph_split[i].strip()
        graph_edges = graph_split[i].split(" ")
        # print(graph_edges)
        mgraph[int(graph_edges[0])][int(graph_edges[1])] = float(graph_edges[2])
        mgraph[int(graph_edges[1])][int(graph_edges[0])] = float(graph_edges[2])
    #print(mgraph)
    flag = 0
    for src in range(0,len(mgraph)):
        #file1.write("===========================================================\n")
        dis = startwith(src, mgraph)
        #print(dis)
        for i in range(src,len(dis)):
            if(i is not src):
                #print(dis[i]);
                if(dis[i] is not math.inf):
                    file1.write(str(src)+" "+str(i)+" "+str(dis[i])+"\n")
                else:
                    flag = 1
        if(flag):
            file1.close()
            file1 = open("metricsteinertree.txt", "w")
            print("Cannot create metric steiner tree instance because input is disconnected graph\n")
            file1.write("Cannot create metric steiner tree instance because input is disconnected graph\n")
            break

    if(not flag):
        file2 = open("required_vertices.txt", "r")
        content = file2.read()
        file1.write("Required vertices\n")
        file1.write(content+"\n")
        file2.close()

    file1.close()
    print("\nSee the output in metricsteinertree.txt file")
