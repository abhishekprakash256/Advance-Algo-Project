Problem 5:

author: Godasree Mamilla, Akshat Sharma

The code for 3/2 - approximation for metric Travelling Salesman Problem is written in python.
we have also attached a sample input file "weighted_graph.txt" to execute our project.

Steps to execute our project:
1) Unzip the project file and copy the Christofides folder to your Linprog server.
2) Navigate to the Christofides folder by using the terminal of your Linprog server.
3) Now specify your inputs in the "weighted_graph.txt" file. Line 1 of "weighted_graph.txt" contains the number of vertices/nodes and the following lines contain edges in u, v, w order where u, v are vertices or nodes of edge and w is the weight of that edge where the range of w is [0,1] and when we are specifying edges our nodes(u,v) should be in the range of [0,(no of vertices -1)] and these u, v, w should be separated by single space in our input file (i.e,) for example when the number of vertices is 4 our u, v should be either 0, 1, 2 or 3.
4) We have assumed that our input is a connected and complete graph.
5) Next execute our program using the "python3 christofidesTSP.py" command. The output of the program is Christofides traveling salesman tour and its cost is displayed in the terminal.

Important Note:
1) Make sure that there should be no white/blank spaces before or after in any lines.
Or else it will throw a "ValueError" error.
2) If a valid number of edges or vertices are not entered then it will display an "enter the valid edges or vertices no" error message and exits the program.
