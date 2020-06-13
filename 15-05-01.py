'''Problem Statement
In the near future, lockdown opens and the crowd emerges in the market. Saurabh goes to the market to meet his friend after a long time but is unable to find him. Saurabh called his friend to ask where is he.
His friend said, "Everyone in the crowd is wearing a T-Shirt with a number on it and every T-Shirt repeats K times except the one I am wearing (Because I am unique)."


Saurabh's friend gives him an array A, consisting of N integers, where Ai represents the T-Shirt number of ith person in the crowd 1 ≤ i ≤ N. Saurabh needs to find x, the T-shirt number of his friend, which is unique and every other T-shirt number is repeated.

Now, to reach his friend, Saurabh needs to calculate his friend's location so that he could directly teleport to his friend avoiding contact with any other person. His friend also gave him an integer R and the location is defined as x^(2RCR), where NCr =N!/(R!(N −R)!)

Saurabh needs to print calculate the location finally. Since the location can be very big, print the location(answer) modulo 109 + 7. [%(109 + 7)].

Note: Output for 0^0 is 1

Constraints

1 ≤ T ≤ 1,000
3 ≤ N ≤ 1,00,000
1 ≤ Ai ≤ 109
2 ≤ K ≤ N − 1
0 ≤ R ≤ 109

Input Format
The first line contains T, the number of test cases.
The first line of every test case contains N, K and R.
The second line of every test case contains N integers denoting Ai.

 

Output Format
For every test case, print location ^109 + 7 in new line.



Sample Testcase #0
Testcase Input
2
6 5 4
11 11 11 14 11 11
5 2 10
8 8 6 6 7
Testcase Output
947961792
527936690
Explanation
In first test case, N = 6 , K = 5 and R = 4. We can see that 11 is repeated 4 times but 14 occurs
once, so x=14. Now, 2∗4C4= 70. So, the location is (1470 )%(109 + 7) = 947961792.

In the second test case, N = 5 , K = 2 and R = 10. We can see that 8 and 6 are repeated 2 times
but 7 occurs once, so x=7. Now, 2∗10C10 = 184756. So, the location is (7184756)%(109 + 7) = 527936690
 '''
from math import *
T = int(input(''))
for r in range(0, T):
    var_str = input('')
    array_in = input('')
    var_list = var_str.split()
    N = int(var_list[0])
    K = int(var_list[1])
    R = int(var_list[2])
    array_list = array_in.split(' ')
    if T>=1 and T<=1000 and N>=3 and N<=100000 and K>=2 and K<=(N-1) and R>=0 and R<=1000000000:
        for j in array_list:
            if int(j)>=1 and int(j)<=1000000000:
                var_count = array_in.count(j)
                if var_count == 1:
                    x = int(j)
                    break
                else:
                    x = 0
                    continue
            else:
                x = 0

        # The Value Of nCr 
        def nCr(n, r): 
            return (fact(n) / (fact(r) * fact(n - r)))%1000000007 

        # Returns factorial of n 
        def fact(n):  
            if n == 0: # The termination condition
                return 1 # The base case
            else:
                res = n * factorial(n-1) # The recursive call
                return res

        # Driver code 
        n = 2*R
        r = R
        nCr = int(nCr(n, r))
        if x == 0 and nCr == 0:
            res = 1
        else:
            res = (x**nCr)%(10**9+7)
        print(res)
