<h1>Jumping Numbers</h1>

<p>Given a positive number X. Find all Jumping Numbers smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.</p>

<h2>Input:</h2>
<p>The first line of the input contains T denoting the number of testcases. Each testcase contain a positive number X.</p>

<h2>Output:</h2>
<p>Output all the jumping numbers less than X in sorted order. Jump to example for better understanding.</p>

<h2>Constraints:</h2>
<p>1 <= T <= 100<br>
1 <= N <= 109</p>

<h2>Example:</h2>
<p>Input:<br>
2<br>
10<br>
50<br>
Output:<br>
0 1 2 3 4 5 6 7 8 9 10<br>
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45</p>

<h2>Explanation:</h2>
<p>Testcase 2: Here, the most significant digits of each jumping number is following increasing order, i.e., jumping numbers starting from 0, followed by 1, then 2 and so on, themselves being in increasing order 2, 21, 23.</p>

<small><a href="https://practice.geeksforgeeks.org/problems/jumping-numbers/0">Source</a></small>