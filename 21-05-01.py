'''Problem Statement

The doctor has n vaccines. The vaccine has destroy power Pi. He needs to destroy a corona virus, the strength of which is d. When a vaccine with power Pi strikes the virus, the strength of the virus is decreased by Pi (if d<pi, then d becomes 0) and the attack power of the vaccine becomes floor(Pi/2).

Doctor has k trials, and he has to destroy the virus within those k trials.

If it is not possible, print -1.

If possible, print the least number of hits required.

Constraints:

 1 <= n <= 105

 1 <= d <= 1017

 1 <= k <= 105

 0 <= Pi <= 1014
Input Format

First line contains 3 integers, n, d, k;

Second line contains n space separated positive integers, denoting the powers of the n vaccines
Output Format

Print the number of attacks required(less than or equal to k).

 Or -1 if it is not possible to destroy the virus within k trials.


Sample Testcase #0
Testcase Input

3 30 4
10 5 11

Testcase Output

4

Explanation

Initially set of vaccine is: (10, 11, 5)

1 possible way of choosing the vaccine is:

1st, choose the 1st vaccine. Now d becomes 20 and set of vaccines is (5, 11, 5).

2nd, choose the 3rd vaccine Now d becomes 15 and set of vaccines  is (5, 11, 2).

3rd, choose the 1st vaccine. Now d becomes 10 and set of vaccines is (2, 11, 2).

4th, choose the 2nd vaccine Now d becomes 0(since d<11) and set of vaccines  is (2, 5, 2).

So the door can be destroyed in 4 trials.
Sample Testcase #1
Testcase Input

5 40 7
5 12 34 56 68

Testcase Output

1

Explanation

Initially set of vaccine is: (5,12,34,56,68)

1 possible way of choosing the vaccine is:

1st, choose the 4th vaccine. Now d becomes 0 and set of vaccines is (5,12,34,16,68 ).

So the door can be destroyed in 1 trial'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
S1 = list(map(int, input().rstrip().split()))
S2 = list(map(int, input().rstrip().split()))
n = S1[0]
d = S1[1]
k = S1[2]
count = 0
for i in range(0, k):
    max_S2 = max(S2)
    if max_S2 >= d:
        count += 1
        print(count)
        break
    else:
        d -= max_S2
        index = S2.index(max_S2)
        S2[index] = max_S2//2
        count += 1
else:
    print('-1')
