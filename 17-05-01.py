'''Problem Statement

The Administration of NIT Manipur has planned a trip for the students to visit the historic Kangla Fort. The students are very excited about the trip and formed groups of friends among them to enjoy during their journey to the Kangla Fort.

There are a total of N groups formed and the ith group consists of Si students ( 1<= Si <=4 ). The Administration has booked taxis for the students for going from NIT Manipur to Kangla Fort. Each taxi can accommodate a maximum of 4 students.

Now, to save some money, the Administration wants to know the minimum number of taxis required for all the students if all members of a group should ride together in the same taxi (but one taxi can take more than one group ).

Can you help the Administration?
Input Format

The first line contains N (Total number of groups of students).

The second line contains a sequence of N integers S1 , S2 , … SN where Si represents the number of students in the ith group.

Constraints: 

1<=N<=105

1<=Si <=4
Output Format

Print a single integer – the minimum number of Taxis required for all the students.


Sample Testcase #0
Testcase Input

5
1 2 4 3 3

Testcase Output

4

Explanation

A possible combinations is [4],[3,1],[3],[2], total 4 taxis.'''

N = input('')
S = list(map(int, input().rstrip().split()))
S.sort(reverse=True)
var_count = 0
for i in S:
    if i == 4:
        var_count += 1
    elif i == 3 and S.count(1) >= 1:
        S[S.index(1)] = 0
        var_count += 1
    elif i == 3 and S.count(1) == 0:
        var_count += 1
    elif i == 2 and S.count(2) >= 2:
        S[S.index(2)] = 0
        S[S.index(2)] = 0
        var_count += 1
    elif i == 2 and S.count(1) >= 2:
        S[S.index(2)] = 0
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        var_count += 1
    elif i == 2 and S.count(1) == 1:
        S[S.index(2)] = 0
        S[S.index(1)] = 0
        var_count += 1
    elif i == 2 and S.count(1) == 0:
        S[S.index(2)] = 0
        var_count += 1
    elif i == 1 and S.count(i) >= 4:
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        var_count += 1
    elif i == 1 and S.count(i) == 3:
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        var_count += 1
    elif i == 1 and S.count(i) == 2:
        S[S.index(1)] = 0
        S[S.index(1)] = 0
        var_count += 1
    elif i == 1 and S.count(i) == 1:
        S[S.index(1)] = 0
        var_count += 1
print(var_count)
