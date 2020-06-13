'''Problem Statement

Lily is a nurse in a nearby hospital. She has been given a duty to arrange the COVID-19 kits with required masks in a specific order. The masks available to her are of various sizes. The task is to create a perfect kit.

Consider an array of n distinct integers, arr=a[a[0],a[1],….,a[n-1]] . Lily can swap any two elements of the array any number of times. An array is perfect if the sum of |arr[i]-arr[i-1]|  among  0<i<n  is minimal.

Given the array arr, determine and return the minimum number of swaps that should be performed in order to make the array perfect.

For example, arr= [7,15,12,3]. One minimal array is [3,7,12,15]. To get there, Lily performed the following swaps:

Swap           Result

-                 [7, 15, 12, 3]

3 7           [3, 15, 12, 7]

7 15             [3, 7, 12, 15]

It took 2 swaps to make the array perfect. This is minimal among the choice of perfect arrays possible.

Function Description

Complete the code in the editor below. It should return an integer that represents the minimum number of swaps required.
Input Format

The first line contains a single integer,n , the number of elements in arr . The second line contains n space-separated integers arr[i].

Constraints

    1 <= n <= 10^5
    1 <= arr[i] <= 2*10^9

Output Format

Return the minimum number of swaps needed to make the array beautiful.


Sample Testcase #0
Testcase Input

4
2 5 3 1

Testcase Output

2

Explanation

Let's define array B = [1,2,3,5] to be the perfect reordering of arr. The sum of the absolute values of differences between its adjacent elements is minimal among all permutations and only two swaps (1 with 2 and then 2 with 5) were performed.
Sample Testcase #1
Testcase Input

5
3 4 2 5 1

Testcase Output

2

Explanation

Let's define array B = [5,4,3,2,1] to be the perfect reordering of arr. The sum of the absolute values of differences between its adjacent elements is minimal among all permutations and only two swaps (3 with 5 and then 2 with 3) were performed.'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
S = list(map(int, input().rstrip().split()))
A = list()
for i in range(0, (n+1)):
    A.append(S[n-i])
print(A)
def minSwaps(arr): 
    n = len(arr)  
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1]) 
    vis = {k:False for k in range(n)} 
    ans = 0
    for i in range(n):    
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]:  
            vis[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 
print(minSwaps(S))
