## Project Description 

The project is about the implementation of different algorithms that are NP hard problems in computer science.

### Dependences

-  Python 3

### Running the program 

- In the same directory as the file run the following commands 

```bash
python3 file_name.py 
```

## Authors 

### -  Abhishek Prakash (ap20fe)

### - Godasree Mamilla (gm20dv)

### - Dhruv Kale (dkk20t)

### - Sangeetha Rallabandi (sr21bp)

### - Akshat Sharma (as20kx)



### First Algorithm 

### Description of Algo

- The algo is implementation of the greedy approach to find the max weighted independent set in a graphic matroid. The algo works by sorting the edges by greedy approach and then check for the looping edges and then store it and give the max sets of the edges.

### Running the File

### Steps 

- First unzip the zip file 

```bash
cd max_weighted_independent
python3 max_weight_set.py 
```

### Changing the input file 

```python
if __name__ == '__main__':
	graph_lst = input_parser('weighted_graph.txt')  
"""
change the file name in the line 110 to the input file that is 
to pares as in the abobe example shown
graph_lst = input_parser('weighted_graph.txt')  (file is weighted_graph.txt)
graph_lst = input_parser('input.txt')  (file is input.txt)
"""
```

### Output 

```python
[[1.0, 2.0, 1.0], [2.0, 3.0, 1.0], [0.0, 3.0, 0.5]]
"""
in the nested list the first index gives the vertex 1 as 1.0. 2.0, 0.0
in the nested list the second index gives the vertex 2 as 2.0. 3.0, 3.0
in the nested list the third index gives the weights as 1.0. 1.0, 0.5
"""
```

### References 

```
https://www.geeksforgeeks.org/union-find/
```



### Second Algorithm

- The code for approximation preserving reduction from general steiner tree to metric steiner tree is written in python. we have also attached sample input files "weighted_graph.txt"  and "required_vertices.txt" to execute our project.

### Steps for execution 

-  Navigate to SteinerTreeReduction folder by using terminal of your linprog server.

- Now specify your inputs in "weighted_graph.txt" file and "required_vertices.txt" file. The line 1 of "weighted_graph.txt" contains number of vertices/nodes and following lines contains edges in u, v, w order where u, v are vertices or nodes of edge and w is the weight of that edge where range of w is [0,1] and when we are specifying edges our nodes(u,v) should be in the range of [0,(no of vertices -1)] and these u, v, w should be separated by single space in our input file (i.e,) for example when number of vertices are 4 our u, v should be either 0, 1, 2 or 3.

- Then specify your required vertices in "required_vertices.txt" input file in one line and each vertex should be separated by single space where vertices start from 0. Here we are assuming that you will give valid vertices (i.e,) for example if number of vertices are 4 then we specify 0 1 2 3 or 0 1 3 etc as our required vertices.

-  Our input can be connected graph or disconnected graph.

- Next execute our program using "python3 steinertreereduction.py" command. The output of the program will be displayed in "metricsteinertree.txt" file which is present in the same path as that of our python file.

- If the input is disconnected graph then output in "metricsteinertree.txt" contains "Cannot create metric steiner tree instance because input is disconnected graph" message otherwise if the input is connected graph then "metricsteinertree.txt" file contains the instance of metric steiner tree in it.

  Important Note:
  1) Make sure that there should be no white/blank spaces before or after in any lines.
  Or else it will throw a "ValueError" error.
  2) We are assuming more than 5 digits will not be specified after decimal point.


### Third Algorithm

- The code for 2 approximation for metric Steiner tree is written in python. And along with the code, we have attached sample weighted_graph.txt and required_vertices.txt
  Below we have shown how to run the code and the input/output formats to run the code successfully.

Steps to run the code:
1. Extract the folder in your home directory.
2. Open the terminal inside the folder.
3. To run this code, you need python or python3 in your system.
4. To run the code, type the "python3 metricsteinertree.py weighted_graph.txt" command.

The input format for weighted_graph.txt:
1. line #1 no of vertex/nodes
2. following lines contain edges in u,v,wt order.

- No.1 important thing!!! While inserting the number of vertex/nodes on line #1, the code counts from 0. So, if there are 10 vertices/nodes (1 to 10), you have to write 11 on line #1, as you can see from the sample weighted_graph.txt attached. And if there are 10 vertices/nodes (0 to 9), you have to write 10 on line 
  Or else it will throw a "enter the valid edges or vertices no" error.

- No.2 important thing!!! There should be no white/blank spaces before or after in any lines.

- Or else it will throw a "ValueError" error.))

- The input format for vertices_graph.txt:

1. line #1 contains vertices that need to be checked.

- ((## Important thing!!! There should be no white/blank spaces before or after on the line.
  Or else it will throw a "ValueError" error.))

- Output format:
  The output will show us the edges and their weights.
  example: (metric steiner tree instace {'u v' : w, 'u v' : w})

### Fourth Algorithm

The code for 2 - approximation for metric Travelling Salesman Problem is written in python.
we have also attached sample input file "weighted_graph.txt" to execute our project.

Steps to execute our project:

- Navigate to travellingsallesman folder by using terminal of your linprog server.
- Now specify your inputs in "weighted_graph.txt" file. The line 1 of "weighted_graph.txt" contains number of vertices/nodes and following lines contains edges in u, v, w order where u, v are vertices or nodes of edge and w is the weight of that edge where range of w is [0,1] and when we are specifying edges our nodes(u,v) should be in the range of [0,(no of vertices -1)] and these u, v, w should be separated by single space in our input file (i.e,) for example when number of vertices are 4 our u, v should be either 0, 1, 2 or 3. In the input file atleast 2 vertices needs to be given.
- We have assumed that our input is connected and complete graph.
- Next execute our program using "python3 travellingsalesmanproblem.py" command. The output of the program is travelling salesman tour and it's cost is displayed in the terminal.

Important Note:

- Make sure that there should be no white/blank spaces before or after in any lines.
  Or else it will throw a "ValueError" error.
- If valid number of edges or vertices are not entered then it will display "enter the valid edges or vertices no" error message and exits the program.

 ### Fifth Algorithm

- The code for 3/2 - approximation for metric Travelling Salesman Problem is written in python.
  we have also attached a sample input file "weighted_graph.txt" to execute our project.

Steps to execute our project:

-  Navigate to the Christofides folder by using the terminal of your Linprog server.
- Now specify your inputs in the "weighted_graph.txt" file. Line 1 of "weighted_graph.txt" contains the number of vertices/nodes and the following lines contain edges in u, v, w order where u, v are vertices or nodes of edge and w is the weight of that edge where the range of w is [0,1] and when we are specifying edges our nodes(u,v) should be in the range of [0,(no of vertices -1)] and these u, v, w should be separated by single space in our input file (i.e,) for example when the number of vertices is 4 our u, v should be either 0, 1, 2 or 3.
-  We have assumed that our input is a connected and complete graph.
-  Next execute our program using the "python3 christofidesTSP.py" command. The output of the program is Christofides traveling salesman tour and its cost is displayed in the terminal.

Important Note:

-  Make sure that there should be no white/blank spaces before or after in any lines.
  Or else it will throw a "ValueError" error.
- If a valid number of edges or vertices are not entered then it will display an "enter the valid edges or vertices no" error message and exits the program.

### 



