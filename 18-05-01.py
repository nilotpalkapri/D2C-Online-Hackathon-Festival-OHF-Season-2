'''Problem Statement

There are N stones arranged in a row. The i-th stone from the left is painted in the color Ci.

Mohit will perform the following operation zero or more times:

    Choose two stones painted in the same color. Repaint all the stones between them, with the color of the chosen stones.

Find the number of possible final sequences of colors of the stones, modulo 109+7.

 
Constraints

    1≤N≤2×105
    1≤Ci≤2×105(1≤i≤N)
    All values in input are integers.

Input Format

N
C1
::
CN

Output Format

Print the number of possible final sequences of colors of the stones, modulo 109+7


Sample Testcase #0
Testcase Input

5
1
2
1
2
2

Testcase Output

3

Explanation

We can make three sequences of colors of stones, as follows:

    (1,2,1,2,2), by doing nothing.
    (1,1,1,2,2), by choosing the first and third stones to perform the operation.
    (1,2,2,2,2), by choosing the second and fourth stones to perform the operation.
'''

N = int(input(''))
str_in = ''
for i in range(0,N):
    str_in += input('')
str_unique = ''
for x in str_in:
    if x not in str_unique:
        str_unique += x

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

from functools import partial
dups_in_source = partial(list_duplicates_of, str_in)

position_list = list()
for c in str_unique:
    position_list.append(dups_in_source(c))
#print('position_list= ', position_list)

res = 0
res_list = list()
for j in position_list:
    count = 0
    if len(j) > 1:
        var = (1+count)
        for p in j:
            temp_str = ''
            #print(j[count], j[var])
            for k in range(j[count], j[var]):
                temp_str += str_in[k]
                var += 1
                if str_in[k] == j[count]:
                    continue
                else:
                    res += 1
                    break
            if var == len(j):
                break
            res_list.append(str_in[0:j[count]]+temp_str+str_in[j[var]:])
        count += 1

final = 0
final_list = list()
for i in res_list:
    if i not in final_list:
        final_list.append(i)
        final += 1

print(final+1)
