Problem 4:

author: Sangeetha Rallabandi, Godasree Mamilla

The code for 2 - approximation for metric Travelling Salesman Problem is written in python.
we have also attached sample input file "weighted_graph.txt" to execute our project.

Steps to execute our project:
1) Unzip the project file and copy TravellingSalesmanProblem folder to your linprog server.
2) Navigate to TravellingSalesmanProblem folder by using terminal of your linprog server.
3) Now specify your inputs in "weighted_graph.txt" file. The line 1 of "weighted_graph.txt" contains number of vertices/nodes and following lines contains edges in u, v, w order where u, v are vertices or nodes of edge and w is the weight of that edge where range of w is [0,1] and when we are specifying edges our nodes(u,v) should be in the range of [0,(no of vertices -1)] and these u, v, w should be separated by single space in our input file (i.e,) for example when number of vertices are 4 our u, v should be either 0, 1, 2 or 3. In the input file atleast 2 vertices needs to be given.
4) We have assumed that our input is connected and complete graph.
5) Next execute our program using "python3 travellingsalesmanproblem.py" command. The output of the program is travelling salesman tour and it's cost is displayed in the terminal.

Important Note:
1) Make sure that there should be no white/blank spaces before or after in any lines.
Or else it will throw a "ValueError" error.
2) If valid number of edges or vertices are not entered then it will display "enter the valid edges or vertices no" error message and exits the program.