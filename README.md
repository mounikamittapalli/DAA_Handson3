# DAA_Handson3
function x = f(n)
   x = 1;
   for i = 1:n
        for j = 1:n
             x = x + 1;
1.find the runtime of the algorithm mathematically (i should see summations).

the outer loop runs n times
for each outer loop iteration, the inner loop runs n times.
thus, the total number of iterations of the inner loop is n^2
t(n)=n^2 times
total operations: i=1∑n j=1∑n 1


2.please check code of function.py (/users/mounika/pycharmprojects/daa_handson3/function.py)

3.big-o (upper bound): the function is upper bounded by 𝑂(𝑛^2)
o(n^2) meaning that the algorithm will never take more than quadratic time.
big-omega (lower bound):since the runtime will always be proportional to n^2 or greater (even in the best case), we have:
ω(𝑛^2)
big-theta (tight bound): big-theta represents the exact asymptotic behavior. since the polynomial fitting shows that the time complexity is dominated by
 we can say:θ(𝑛^2)

4.please check code of function2.py (/users/mounika/pycharmprojects/daa_handson3/function2.py)

5.please check code of function3.py (/users/mounika/pycharmprojects/daa_handson3/function3.py)

6.please check code of merge_sort.py (/users/mounika/pycharmprojects/daa_handson3/merge_sort.py)


