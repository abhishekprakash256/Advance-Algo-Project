Problem: 3
Authors: Dhruv Kale and Godasree Mamilla
The code for 2 approximation for metric Steiner tree is written in python. And along with the code, we have attached sample weighted_graph.txt and required_vertices.txt
Below we have shown how to run the code and the input/output formats to run the code successfully.

Steps to run the code:
1. Extract the folder in your home directory.
2. Open the terminal inside the folder.
3. To run this code, you need python or python3 in your system.
4. To run the code, type the "python3 metricsteinertree.py weighted_graph.txt" command.

The input format for weighted_graph.txt:
1. line #1 no of vertex/nodes
2. following lines contain edges in u,v,wt order.

((## No.1 important thing!!! While inserting the number of vertex/nodes on line #1, the code counts from 0. So, if there are 10 vertices/nodes (1 to 10), you have to write 11 on line #1, as you can see from the sample weighted_graph.txt attached. And if there are 10 vertices/nodes (0 to 9), you have to write 10 on line #1.
Or else it will throw a "enter the valid edges or vertices no" error.

## No.2 important thing!!! There should be no white/blank spaces before or after in any lines.
Or else it will throw a "ValueError" error.))

The input format for vertices_graph.txt:
1. line #1 contains vertices that need to be checked.

((## Important thing!!! There should be no white/blank spaces before or after on the line.
Or else it will throw a "ValueError" error.))

Output format:
The output will show us the edges and their weights.
example: (metric steiner tree instace {'u v' : w, 'u v' : w})
