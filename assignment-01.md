

# CMPS 2200 Assignment 1

**Name:** Zev Gaslin


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes becuase 2^n+1/2^n = 2^1  which is constant time, so 2^n+1 is the same time as 2^n
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No becuase the ratio of 2^2^n / 2^n is not in constant time. 2^(2^n) = 2^2n 2^(2n)/2^n = 2^n, which is still in 2^n time, so 2^2^n is not in O(2^n) time
    
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No becuase n^1.01 is a polynomial and log^2(n) is a logarithmic function
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, becuase n^1.01 is a polynomial so it will alwasy eventually be larger than any constant * the logarithmic function, so it will always be in the omega of log^2(n)
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  

10^(log^n)^3  = 10^[log(n)*log(n)*log(n)] = 3(10^log(n)) = 3(n) = 3n

10^sqrt(n) = 10^n^1/2 = 10^0.5^n 
10^0.5n grows faster than 3n becuase one has c^n while the other has c*n so they are not the same big O
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
sqrt(n) is in omega (logn^3) if for any constant c, n^0.5 is greater than log(n)^3
Any positicve polynomial will always be greater than any log function at large values of n, so n^0.5 will be greater than log(n)^3 for any c, therefor n^0.5 is in omega (log(n)^3), so yes



2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  this function is a recursive function summing up the fibbonachi sequence up until the number x. The function first checks if the input is 1 or less, and if so it returns 1. If the input is greater than 1 the function creates two new variables ra and rb and calls the foo function on both of them, inputing the number 1 less than and 2 less than x into foo of ra and rb. This  then calls the foo function on those numebrs recusivly until the input is 1, getting the values of the 2 numbers before x in the fibbinachi sequence for ra and rb. The function then returns ra + rb, adding the two numebrs before x in the fibinachi sequence which is how you get the value of the xth number in the sequence 
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

the work is W(n) because the function has to go over all n numbers in the list once, for a total of n times 

Span is S(n) because the function does each call one after the other, so there is only one path which makes the longest path = to the work



  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   
  

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  

For the sequential algothirm the work and span is the same as in 3b. 

the work of the sequential algorithm is W(n) because the function has to go over all n numbers in the list once, for a total of n times 

The span is S(n) because the function does each call one after the other, so there is only one path which makes the longest path = to the work

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

Work = 2W(n/2) +W(1) becuase it has a recursive step which splits the list into 2 lists both is size n/2 and then a step that combines the two lists which takes O(1) time

Span: First the function splits the list into n lists of size one. This span is log(n) to get down to lists of size 1. Next the funciton adds the lists back together in reverse order of how it split them up. the span of that is also log(n). So the ttola span is 2*log(n), or S(2log(n))

