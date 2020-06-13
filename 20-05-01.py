'''Problem Statement

Himanshu is a nerd due to his love for Mathematics. He always creates trouble for others with his senseless questions. This time he has asked his two friends, Vaibhav and Nikunj, to calculate p mod m where numbers p and m are in base-b and they have to report the result in base-b only. But they are busy preparing more problems for you. So they need you to help them answer Himanshu’s easy math problem.
Input Format

The first line consists of a single integer T (1<=T<=1000) - the number of testcase.
The next T lines describe the test cases. Each test case is given as three space-separated integers b, p, m.


2 <= b <= 10 - b is in base-10.
1 <= numberOfDigits(p) <= 105 - each digit of p is in between 0 and b-1 (both inclusive).
1 <= numberOfDigits(m) <= 9 - each digit of m is in between 0 and b-1 (both inclusive) and m is not equal to 0.
∑Ti=1 numberOfDigits(p) <= 2.106
Output Format

In each of the T lines, output the answer to the corresponding test case in base-b.


Sample Testcase #0
Testcase Input

2
2 1100 101
3 1201 22

Testcase Output

10
20

Explanation

1100 in base-2 is equivalent to 12 in base-10 and 101 in base-2 is equivalent to 5 in base-10 so 12 mod 5
= 2 which is equivalent to 10 in base-2.
Sample Testcase #1
Testcase Input

2
7 102345 1256
4 102312 112

Testcase Output

636
102

Explanation

1201 in base-3 is equivalent to 46 in base-10 and 22 in base-3 is equivalent to 8 in base-10 so 46 mod 8
= 6 which is equivalent to 20 in base-3.'''





# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input(''))
list_in = list()
for i in range(0,n):
    S = input('').split( )
    list_in.append(S)

for x in list_in:
    b = int(x[0])
    p = x[1]
    m = x[2]
    if b >= 2 and b<=(10-b) and len(p)>=1 and len(p)<=100000 and len(m)>=1 and len(m)<=9:
        def val(c):
            if c >= '0' and c <= '9':
                return ord(c) - ord('0')
            else:
                return ord(c) - ord('A') + 10
        def toDeci(str,base):
            llen = len(str)
            power = 1
            num = 0
    
            for i in range(llen - 1, -1, -1):
                if val(str[i]) >= base:
                    print('Invalid Number')
                    return -1
                num += val(str[i]) * power
                power = power * base
            return num
        
        re1 = int(toDeci(p, b))
        re2 = int(toDeci(m, b))
        res10 = (re1%re2)

        def reVal(num):
            if (num >= 0 and num <= 9):
                return chr(num + ord('0'))
            else:
                return chr(num - 10 + ord('A'))

        def strev(str):
            len = len(str)
            for i in range(int(len / 2)):
                temp = str[i]
                str[i] = str[len - i - 1]
                str[len - i - 1] = temp
    
        def fromDeci(res, base, inputNum):
    
            index = 0; # Initialize index of result r
            while (inputNum > 0):
                res+= reVal(inputNum % base)
                inputNum = int(inputNum / base)
            res = res[::-1]
            return res
        res = ""
        print(fromDeci(res, b, res10))
    else:
        print('-1')
        

