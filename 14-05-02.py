'''Problem Statement
There is a lowercase English letter string S of length 2N. These 2N characters in S can be colored red or green in 2(2^N) ways. Find the number of ways which satisfies the following condition:

The string obtained by reading the characters painted red from left to right is equal to the string obtained by reading the characters painted blue from right to left.
Constraints:

1≤N≤18
The length of S is 2N.
S consists of lowercase English letters.
Input Format
N
S
Output Format
Print the number of ways to paint the string that satisfy the condition.



Sample Testcase #0
Testcase Input
4
cabaacba
Testcase Output
4
Explanation
There are four ways to paint the string, as follows:

cabaacba (2,3,4,6 in green)
cabaacba (2,3,5,6 in green)
cabaacba (1,5,7,8 in green)
cabaacba (1,4,7,8 in green)'''
