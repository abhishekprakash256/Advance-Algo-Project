"""
The file for the question 1 
"""

def input_parser(file):
	"""
	the file to parse the input from the text file 

	"""
	#open the file and read input
	lines = []
	with open(file) as f:
		lines = f.readlines()
	#the number of the edges
	counter = 0
	graph_lst = []
	
	for line in lines:
		if counter == 0:
			num_edges = line
		else:
			edge_lst = []
			strings_lst = []
			strings_lst = (line.replace("\n", "").split(" "))

			for x in strings_lst:
				x = float(x)
				edge_lst.append(x)

			graph_lst.append(edge_lst)

		counter +=1

	return graph_lst



def sorting_fun(graph_lst):
	"""
	the function is used to sort the edges in weight format 
	"""
	sorted_graph_lst = (sorted(graph_lst, key = lambda x: x[2]))    

	sorted_graph_lst.reverse()

	#print(sorted_graph_lst)
	
	return sorted_graph_lst


def make_set(sorted_lst):
	"""
	the function is used to check the set and put the max weight edges in set if not adjacent

	"""
	#sets of the vertex and weights

	vertex_1 = []
	vertex_2 = []
	weights = []

	count = 0 

	for i,j,k in sorted_lst:
		if count == 0 :
			vertex_1.append(i)
			vertex_2.append(j)
			weights.append(k)
		elif i not in vertex_1 and i not in vertex_2 and j not in vertex_2 and j not in vertex_1:
			vertex_1.append(i)
			vertex_2.append(j)
			weights.append(k)
		else:
			continue

		count+=1

	return vertex_1, vertex_2, weights


if __name__ == '__main__':
	graph_lst = input_parser('input_7.txt')
	sorted_lst = sorting_fun(graph_lst)
	sets = make_set(sorted_lst)

	#parsing the output 
	print("vertex_1")
	for i in sets[0]:
		print(i)
	print("vertex_2")
	for j in sets[1]:
		print(j)

	print("weights")
	for k in sets[2]:
		print(k)