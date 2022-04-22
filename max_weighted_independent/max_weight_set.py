"""
The file for the question 1 
"""

from collections import defaultdict

#class to append in the graph 
class Graph:

	def __init__(self,vertices):
		self.V= int(vertices) #No. of vertices
		self.graph = defaultdict(list) 



	def addEdge(self,u,v):
		self.graph[u].append(v)


	def find_parent(self, parent,i):
		if parent[int(i)] == -1:
			return i
		if parent[int(i)]!= -1:
			return self.find_parent(parent,parent[int(i)])


	def union(self,parent,x,y):
		parent[int(x)] = int(y)




	def isCyclic(self):
		

		parent = [-1]*(self.V)


		for i in self.graph:
			for j in self.graph[int(i)]:
				x = self.find_parent(parent, i)
				y = self.find_parent(parent, j)
				if x == y:
					return True
				self.union(parent,x,y)



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
			global num_edges 
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
	
	return sorted_graph_lst


def findUnique(arr):
	unique = []
	for i in arr:

		if int(i[0]) not in unique:
			unique.append(int(i[0]))
		if int(i[1]) not in unique:
			unique.append(int(i[1]))
	return unique

if __name__ == '__main__':
	graph_lst = input_parser('weighted_graph.txt')
	
	new_sort = sorting_fun(graph_lst)



	length_of_sort = len(new_sort)
	unique = []

	answer = [[new_sort[0][0],new_sort[0][1],new_sort[0][2]]]
	for i in new_sort[1:]:	
		unique = findUnique(answer+[[i[0],i[1],i[2]]])
		mapping = {}
		for c in range(len(unique)):
			mapping[unique[c]]=c
		
		g = Graph(len(unique))	
		for j in answer:
			g.addEdge(mapping[j[0]],mapping[j[1]])
			
		g.addEdge(mapping[i[0]],mapping[i[1]])

		if not g.isCyclic(): 
			answer.append([i[0],i[1],i[2]])
	

	print(answer,"\n")