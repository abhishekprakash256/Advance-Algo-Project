"""
The file to insert the graph in edge list format and print it
"""

#the graph in the edge list format 

test_graph = [[0,1,5],[0,2,7],[0,3,3],[1,4,2],[1,5,10],[2,6,1],[3,7,11],[4,5,9],[5,7,4],[6,7,6]]

def test_algo(graph_lst):
	"""
	The algorithm will do something
	"""

	#do operation to the graph and store it in the edge list format 
	# and print it out 
	for i,j,k in graph_lst:
		print(i,j,k)

	#return graph_lst



print(test_algo(test_graph))