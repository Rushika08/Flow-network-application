# Flow network application example: committee assignment problem

The input to the committee assignment problem consists of the following data: \
	A set of people P={p_1,p_2,...,p_m}. \
	A set of committees C={c_1,c_2,...,c_n}. \ 
	Each person p_i has a set of committees W_i they are willing to be on. \
	Each person p_i has a maximum number of committees m_i they are willing to be in total. \ 
	Each committee c_i has a required number of people z_i.

The problem is to come up with an assignment of people to committees that satisfies all the constraints, for example, each committee has exactly z_i different people assigned to it, and each person p_i is assigned only to committees they are willing to be on, and to no more than m_i committees in total, or report that this is not possible.


## Solution via flow network:

The solution is to turn the problem into an appropriate flow network; finding a max flow will then correspond to solving the problem. In particular, we build a flow network G=(V,E)  as follows: \
	V=P∪C∪{s,t}. There is one vertex for each person, one for each committee, and two extra vertices to serve as the source and sink. \
	Connect the source s to each p_i with a directed edge of capacity m_i. \
	Connect each c_i to the sink t with a directed edge of capacity z_i. \
	Make a directed edge (p_i,c_j) with capacity 1 for each c_j ∈ W_i; that is, connect each person to those committees they are willing to be on. \

To solve the committee assignment problem, we can now find a max flow on G (using the Ford-Fulkerson algorithm). If the max flow has value z_1 + z_2 + ... + z_n (that is, if it completely saturates all the incoming edges to the sink), then a valid committee assignment exists, and we can read it off by assigning person p_i to committee c_j if and only if the edge (p_i,c_j) has a flow of 1. Otherwise, no valid committee assignment exists.


## About the Inputs and Outputs:

The first line provides the number of people, and the second line provides the number of committees. The third line takes the names of the individuals, and the next line defines the names of the committees. Then the program should read the maximum number of committees for each person and the name of the committee they are willing to join. Finally, the maximum number of people allowed for each committee is indicated. All these data should be inserted through the std:in.
The example given below has 4 people and 3 committees. These people were named from P1-P4 and the committees were named from C1-C3. Then the maximum number of committees for the 4 people and the relevant committees are denoted. The last part will define the maximum number of people for the 3 committees (C1,C2 and C3).

4 \
3 \
P1 P2 P3 P4 \
C1 C2 C3 \
2 C1 C2 \
2 C2 C3 \
2 C1 C3 \
3 C1 C2 C3 \
2 \
3 \
1


The program should print its output as given below.

Person: Committee \
P1 : C1 C2 \
P2 : C2 C3 \
P3 : C1 \
P4 : C2

Committee: Person \
C1 : P1 P3 \
C2 : P1 P2 P4 \
C3 : P2


If the graph doesn't produce a correct output, write "Not Possible" to the std:out.
