'''Problem Statement
Adarsh, a baker, can make N kinds of cakes using only a certain powder. These cakes are called Cake1, Cake2, ...,CakeN. In order to make one Cake i (1≤i≤N), he needs to consume m[i] grams of powder. He cannot make a non-integer number of cakes, such as 0.5 cakes.

The recipes of these cakes are developed by repeated modifications from the recipe of Cake1. Specifically, the recipe of Cake i (2≤i≤N) is a direct modification of the recipe of Cake p[i] such that (1≤p[i]<i).

 

Now, he has X grams of powder. He decides to make as many cakes as possible for a party tonight. However, since the tastes of the guests differ, he will follow the below condition:

-->Let c[i] be the number of Cake i (1≤i≤N) that he makes. For each integer i such that 2≤i≤N,  c[p[i]]≤c[i]≤c[p[i]]+D must hold. Here, D is a predetermined value.

Now your task is to find how many cakes can be made here? He does not necessarily need to consume all the powder.

CONSTRAINTS:

1) 2≤N≤50

2) 1≤X≤10^9

3) 0≤D≤10^9

4) 1≤m[i]≤10^9  (1≤i≤N)

5) 1≤p[i]<i (2≤i≤N)

All values in input are integers

Input Format
Input is given from Standard Input in the following format:

N X D

m1

m2 p2

.

.

mN pN

Output Format
Print the maximum number of cakes that can be made under the condition.



Sample Testcase #0
Testcase Input
3 100 1
15
10 1
20 1
Testcase Output
7
Explanation
He has 100 grams of powder, can make three kinds of cakes, and the conditions that must hold are c1≤c2≤c1+1 and c1≤c3≤c1+1. It is optimal to make two Cake 1, three Cake 2 and two Cake 3.

Sample Testcase #1
Testcase Input
3 100 10
15
10 1
20 1
Testcase Output
10
Explanation
The amount of powder and the recipes of the cakes are not changed from Sample Input 1, but the last conditions are relaxed. In this case, it is optimal to make just ten cakes 2. As seen here, he does not necessarily need to make all kinds of cakes.'''
S1=raw_input()
S1=(S1.split( ))
N = int(S1[0])
X = int(S1[1])
D = int(S1[2])

res_list = list()
for i in range(0,N):
    S2=raw_input()
    S2=(S2.split( ))
    print(res_list)
    res_list.append(S2[0])

for i in 
K = int(X/Z)
print(K)
