Problem 2:

author: Godasree Mamilla

The code for approximation preserving reduction from general steiner tree to metric steiner tree is written in python.
we have also attached sample input files "weighted_graph.txt" 
and "required_vertices.txt" to execute our project.

Steps to execute our project:
1) Unzip the project file and copy SteinerTreeReduction folder to your linprog server.
2) Navigate to SteinerTreeReduction folder by using terminal of your linprog server.
3) Now specify your inputs in "weighted_graph.txt" file and "required_vertices.txt" file. The line 1 of "weighted_graph.txt" contains number of vertices/nodes and following lines contains edges in u, v, w order where u, v are vertices or nodes of edge and w is the weight of that edge where range of w is [0,1] and when we are specifying edges our nodes(u,v) should be in the range of [0,(no of vertices -1)] and these u, v, w should be separated by single space in our input file (i.e,) for example when number of vertices are 4 our u, v should be either 0, 1, 2 or 3.
4) Then specify your required vertices in "required_vertices.txt" input file in one line and each vertex should be separated by single space where vertices start from 0. Here we are assuming that you will give valid vertices (i.e,) for example if number of vertices are 4 then we specify 0 1 2 3 or 0 1 3 etc as our required vertices.
5) our input can be connected graph or disconnected graph.
6) Next execute our program using "python3 steinertreereduction.py" command. The output of the program will be displayed in "metricsteinertree.txt" file which is present in the same path as that of our python file.
7) If the input is disconnected graph then output in "metricsteinertree.txt" contains "Cannot create metric steiner tree instance because input is disconnected graph" message otherwise if the input is connected graph then "metricsteinertree.txt" file contains the instance of metric steiner tree in it.

Important Note:
1) Make sure that there should be no white/blank spaces before or after in any lines.
Or else it will throw a "ValueError" error.
2) We are assuming more than 5 digits will not be specified after decimal point.



