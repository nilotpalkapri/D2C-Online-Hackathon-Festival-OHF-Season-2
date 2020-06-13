'''Problem Statement

Ram, Vijay and Tej love chocolates. They have X, Y and Z chocolates, respectively. Now, they will exchange those chocolates by repeating the action below:

Each person simultaneously divides his chocolates in half and gives one half to each of the other two persons.

This action will be repeated until there is a person with odd number of chocolates in hand.

How many times will they repeat this action? Note that the answer may not be finite.

CONSTRAINTS:

1<=X,Y,Z<=10^9
Input Format

Input is given from Standard Input in the following format:

X Y Z
Output Format

Print the number of times the action will be performed by the three people, if this number is finite. If it is infinite, print -1 instead.


Sample Testcase #0
Testcase Input

4 12 20

Testcase Output

3

Explanation

Initially, Ram, Vijay and Tej have 4,12 and 20 chocolates. Then,

-After the first action, they have 16, 12 and 8.

--After the second action, they have 10, 12 and 14.

---After the third action, they have 13, 12 and 11.

Now, Ram and Tej have odd number of chocolates, and therefore the answer is 3.
Sample Testcase #1
Testcase Input

14 14 14

Testcase Output

-1

Explanation

There is no possibility for this to exchange and get odd number of chocolates '''
'''#from importlib2 import abc
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function'''
S=raw_input()
S=(S.split( ))
#S = S[0]
#print(S)
#S = list(map(int, input().rstrip().split()))
count = 0
for i in range(0, 999999):
    new_list = S
    x = int(new_list[0])
    y = int(new_list[1])
    z = int(new_list[2])
    new_list[0] = str((y/2) + (z/2))
    new_list[1] = str((x/2) + (z/2))
    new_list[2] = str((x/2) + (y/2))
    if x%2 !=0 or y%2 != 0 or z%2 != 0:
        print(count)
        count += 1
        break
    else:
        count += 1
        continue
else:
    print(-1)
