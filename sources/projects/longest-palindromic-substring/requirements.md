This problem can be solved using 3 methods.

### Method 1 (Brute Force)

The simple approach is to check each substring whether the substring is a palindrome or not. We can run three loops, the outer two loops pick all substrings one by one by fixing the corner characters, the inner loop checks whether the picked substring is palindrome or not.

- Time complexity: O(n<sup>3</sup>)
- Auxiliary complexity: O(1)

### Method 2 (Dynamic Programming)

The time complexity can be reduced by storing results of subproblems. We maintain a boolean table[n][n] that is filled in bottom up manner. The value of table[i][j] is true, if the substring is palindrome, otherwise false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true. Otherwise, the value of table[i][j] is made false.

- Time complexity: O(n<sup>2</sup>)
- Auxiliary Space: O(n<sup>2</sup>)

### Method 3

The time complexity of the Dynamic Programming based solution is O(n<sup>2</sup>) and it requires O(n<sup>2</sup>) extra space. We can find the longest palindrome substring in O(n<sup>2</sup>) time with O(1) extra space. The idea is to generate all even length and odd length palindromes and keep track of the longest palindrome seen so far.

#### Step to generate odd length palindrome:

Fix a center and expand in both directions for longer palindromes.

#### Step to generate even length palindrome

Fix two center (low and high) and expand in both directions for longer palindromes.

- Time complexity: O(n<sup>2</sup>) where n is the length of input string.
- Auxiliary Space: O(1)
