'''Problem Statement

Mohit has three types of sweets. Type A is not tasty but has an antidote, B is tasty and also has an antidote and type C is tasty and poisonous.

    Eating poisonous sweet results in a stomach-ache
    Eating another poisonous sweet, while already having a stomach-ache, results to death
    Eating a sweet with antidote can cure the stomachache

Mohit wants to live and eat the maximum number of tasty sweets.

Find the maximum number of tasty sweets that he can have.

Constraints

    0≤A,B,C≤109
    A,B and C are integers.

Input Format

A B C
Output Format

Print the maximum number of tasty sweets Mohit can have.


Sample Testcase #0
Testcase Input

3 1 4

Testcase Output

5

Explanation

Mohit can eat all tasty sweets, in the following order:

    A tasty sweet containing poison
    An untasty sweet containing antidotes
    A tasty sweet containing poison
    A tasty sweet containing antidotes
    A tasty sweet containing poison
    An untasty sweet containing antidotes
    A tasty sweet containing poison
'''

S = list(map(int, input().rstrip().split()))
U = S[0]
T = S[1]
P = S[2]
var_count = 0
for i in range (0, (U+T+P)):
    if P > (U+T+1):
        var_count += ((2*T)+U+1)
        break
    else:
        var_count += (T+P)
        break
print(var_count)
