'''Problem Statement
There are N blocks (1 to N) arrange from left to right in a row. Each block i has a weight Ai. Rahul has to perform the following operation on these blocks N times.

Choose a block that is not removed and remove it. The cost of this is the sum of the weights of the blocks that are connected to the block being removed including its own weight. Here, two blocks x and y ( x≤y ) are connected when, for all z ( x≤z≤y), Block z is still not removed.
There are N! possible orders in which Rahul removes the blocks. For all of those N! orders, find the total cost of the N operations and calculate the sum of those N! total costs. As the answer can be extremely large, compute the sum modulo 109+7.

Constraints:

1≤N≤105
1≤Ai≤109
All values in input are integers.
Input Format
N
A1 A2 ...... AN
Output Format
For all of the N! orders, find the total cost of the N operations, and print the sum of those N! total costs, modulo 109+7.



Sample Testcase #0
Testcase Input
2
1 2
Testcase Output
9
Explanation
First, we will consider the order "Block 1 -> Block 2". In the first operation, the cost of the operation is 1+2=3, as Block 1 and 2 are connected. In the second operation, the cost of the operation is 2, as only Block 2 remains. Thus, the total cost of the two operations for this order is 3+2=5.

Then, we will consider the order "Block 2 -> Block 1". In the first operation, the cost of the operation is 1+2=3, as Block 1 and 2 are connected. In the second operation, the cost of the operation is 1, as only Block 1 remains. Thus, the total cost of the two operations for this order is 3+1=4.

Therefore, the answer is 5+4=9.'''



from itertools import permutations
n = int(input(''))
block_weight = input('')
str_of_block = ''

def making_string():
    global str_of_block
    bw_list = block_weight.split(' ')
    for i in bw_list:
        str_of_block += i #creating a string with blocks
    
def do_operation():
    global str_of_block
    weight_loss = 0
    per_res = permutations(str_of_block)
    per_res_list = list(per_res)
    for i in per_res_list:
        k = list(i)
        def loop_new():
            nonlocal weight_loss
            nonlocal k
            for j in k:
                if len(k) == 1:
                    weight_loss = (weight_loss + int(k[0]))
                    break
                else:
                    weight_loss = (weight_loss + int(k[0]) + int(k[1]))
                    del k[0]
                    loop_new()
        loop_new()        
    print(weight_loss%1000000007)

making_string()
do_operation()
