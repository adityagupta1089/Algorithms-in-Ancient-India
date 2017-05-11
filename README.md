# Algorithms in Ancient India
## 1. Ghanapatha for a given input string.
To memorize slokas in ancient time people performed various recitation styles for complete and perfect memorizations, one of which is Ghanapatha. In essence it is just a permutation with repetition of words in different orders.
### How to run?
`python3 ghanapatha.py`

### Explanation

- In this problem we will first store the words of the string in an array.
- We can then see than ghanapatha is the sequence `1221123321123` repeated each time with `+1` to each term, i.e. `1221...` $\to$ `2332...`.
- So we loop through this sequence and print the corresponding word each time by an offset of `-1,0,1,2,...` (`-1` for 0-based indexing) to the numbers in the sequence until the maximum index is contained in the string.
- This means that $3+\text{offset}<\text{length}(\text {string})$

### Sample Input
```
dhiyah. yah. na pracodayāt
```

### Sample Output
```
Ghanapatha for given text is:

dhiyah. yah. yah. dhiyah. dhiyah. yah. na na yah. dhiyah. dhiyah. yah. na ;
yah. na na yah. yah. na pracodayāt pracodayāt na yah. yah. na pracodayāt ;
```

## 2. Sequences of binary number using Pingala's Algorithm
An algorithm by pingala to write binary numbers with given number of digits.

### How to run?
`python3 pingala_binary_sequence.py`

### Explanation

- This problem is based on recursive algorithm where the function returns a list `[0, 1]` if $n=1$.
- Otherwise it first recurses to get list for $n=n-1$ and then for every binary string in that list, it first appends `0` to it and then finally `1` to all of them. 
- Finally it returns the constructed binary sequence (In $L\to R$ manner).

### Sample Input
```
5
```

### Sample Output
```
Binary sequence of n bits written in L-R manner is
00000
10000
01000
11000
00100
10100
01100
11100
00010
10010
01010
11010
00110
10110
01110
11110
00001
10001
01001
11001
00101
10101
01101
11101
00011
10011
01011
11011
00111
10111
01111
11111
```

## 3. Power of 2 using Pingala's Algorithm
The famous `O(log n)` power of 2 algorithm.
### How to run?
`python3 pingala_2_pow_n.py`

### Explanation

- In this problem if $n=0$ we return `1`, else we recurse in the following manner:
	- If $2\mid n$, we return `pow(n/2)*pow(n/2)` else
	- If $2\not\mid n$, we return `pow(n-1)*2`

### Sample Input
```
123
```

### Sample Output
```
2^n using pingala's algorithm is: 10633823966279326983230456482242756608
```
## 4. Solving a linear diophantine equation by Kuttaka method
An algorithm to solve the linear diophantine equation `ax+c=by`.

### How to run?
`python kuttaka.py`

### Explanation

$$ax + c = by$$

- We first check if `gcd(a, b)` divides `c`.If gcd is `>1` Then we divide by common gcd. We make `A, B, C` as positive values of `a, b, c`
- We then create a list for quotients na dmake dividend and divisor as `A` and `B`.
- We find remainders until we get 1 and make valli.
- Finally we multiply the penultimate term with the factor above and add the next term. We expunge the last term and repeat this process till we have only 2 values in the column.
- Then we deal with special cases `a < 0`, `b < 0` and `c < 0`.
- Then we subtract `a` and `c` times the minimum dividend when dividing `y` and `x` respectively.



### Sample Run
```
ax + c = by
Enter a: 60
Enter c: 3
Enter b: 13
60 * 11 + 3 = 663 = 663 = 13 * 51
Solution is (11, 51)
```

## 5. Solving a quadratic diophantine equation by Chakravala method
Solves the quadratic Pell-like equation `Pq^2+s=r^2` through Chakravala method.
### How to run?
`python chakravala.py`

### Explanation
$$Pq^2+s=r^2$$

- We first nearest square to `P`, i.e. $\left(\text{round}(\sqrt P)\right)^2$, `r` as $P\cdot1^2+s=r^2\implies r=\sqrt{s+P}$ and $q=1$.
- Then while we get $s=\pm1,\pm2\pm4$, we solve $qx+r=sy$ (ignoring sign) using previously made kuttaka. Let us get $(x,y)$ as the solution.
- Then we will have $(x+ks,y+kq)$ as another solution, so we need to minimize $|P-X^2|=|P-(x+ks)^2|$ which is  concave, so minima will be near root, i.e. $\frac{\sqrt{P}-x}s$, so we check both integers near to this value and find required $(X, Y) = (x+ks,y+kq)$.
- Then we take $s=-\frac{X^2-P}s$ (neglecting sign) and $q=Y, r=\sqrt{Pq^2+s}$.
- Then we do bhavana, where we use the two rules:
	- Solution of $Pq^2+c=r^2$ is $(\alpha, \beta)$ then solution of $Pq^2+c/k^2=r^2$ is $(\alpha/k,\beta/k)$.
	- Solution of $Pq^2+k=r^2$ is $(\alpha, \beta)$ then solutions of $Pq^2+k^2=r^2$ is $(2\alpha\beta, P\alpha^2+\beta^2)$, or if we have another solution $(\alpha_1,\beta_1)$ then $(\alpha\beta_1+\alpha_1\beta,P\alpha\alpha_1+\beta\beta_1)$ 
	- We do the following transformations: `-1 -> 1`, `4 -> 1`, `-4 -> -1 -> 1`, `2 -> 4 -> 1`, `-2 -> 4 -> 1`.

### Sample Run
```
Pq^2 + s = r^2
Enter P: 61
Enter s: 1
61 * 226153980 ^ 2 + 1 = 3119882982860264401 = 3119882982860264401 = 1766319049 ^ 2
Solution is (226153980, 1766319049)
```