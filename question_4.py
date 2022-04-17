"""
The question 4
input - is a txt file that has numnber of the node and the node0 , node1, weight
output - 0-1-1-2

"""

#reading the file input and storing in the list foramt and number of the edges 
lines = []
with open('weighted_graph.txt') as f:
    lines = f.readlines()
    #store the number of the vertices
    #num_nodes = lines[0]
    #print(num_nodes)


#loop over the variables to store the values 

counter = 0
for i in lines:
	#store the number of node value
	if counter == 0:
		counter +=1
		num_node = lines[0]
	else:
		print(i.rstrip())