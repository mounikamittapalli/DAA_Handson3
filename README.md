# DAA_Handson3

This is DAA Hands-On 3<br/>
Name:Mounika Mittapalli<br/>
Studentid :1002279512<br/>

1.The outer loop runs n times<br/>
for each outer loop iteration, the inner loop runs n times<br/>
Thus, the total number of iterations of the inner loop is n^2<br/>
T(n)=n^2 times<br/>
Total operations: i=1∑n j=1∑n 1


2.please check [function.py](https://github.com/mounikamittapalli/DAA_Handson3/blob/268969d220afdcb5fd249724d8bc4be00dfb515c/function.py)<br/>
[output](https://github.com/mounikamittapalli/DAA_Handson3/blob/379f43506b3740e1057704a24f3ac982f44e8bb5/function.png)

3.**big-o (upper bound)**: The function is upper bounded by 𝑂(𝑛^2)<br/>
  *Tabspace* *Tabspace**Tabspace*o(n^2) meaning that the algorithm will never take more than quadratic time.<br/>
**big-omega (lower bound)**:since the runtime will always be proportional to n^2 or greater (even in the best case)<br/>
 *Tabspace* *Tabspace* *Tabspace*so time complexity is ω(𝑛^2)<br/>
**big-theta (tight bound):** big-theta represents the exact asymptotic behavior.since the polynomial fitting shows that the time complexity is dominated by n^2 <br/>
*Tabspace* *Tabspace* *Tabspace*so time complexity is  θ(𝑛^2)

4.please check [function2.py](https://github.com/mounikamittapalli/DAA_Handson3/blob/d3315b527561668967cd14df97da69be364bd446/function2.py)
<br/>
*Tabspace*[output](https://github.com/mounikamittapalli/DAA_Handson3/blob/379f43506b3740e1057704a24f3ac982f44e8bb5/function2.png)

4.please check [function3](https://github.com/mounikamittapalli/DAA_Handson3/blob/268969d220afdcb5fd249724d8bc4be00dfb515c/function3.py)<br/>
*Tabspace*[output](https://github.com/mounikamittapalli/DAA_Handson3/blob/379f43506b3740e1057704a24f3ac982f44e8bb5/function3.png)

5.Since the number of operations remains n^2, the addition of y = i + j<br/>
it will not affect the overall time complexity or the measured runtime in terms of big-O.<br/>
The runtime may increase slightly because there is an additional operation inside the inner loop,<br/>
but it will still follow the same quadratic growth pattern.<br/>
So,it will slightly increase the runtime, but it won't change the big-O complexity.

6.please check code of [merge_sort](https://github.com/mounikamittapalli/DAA_Handson3/blob/268969d220afdcb5fd249724d8bc4be00dfb515c/merge_sort.py)


