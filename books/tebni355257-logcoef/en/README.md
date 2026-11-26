# What survives at a prime column?

Column 3 begins $14,29,50$. Each leaves remainder $2$ on division by $3$, yet not all are even. Column 4 begins $90,206,406$; now division by $4$ always leaves remainder $2$. Why does moving down a column preserve one remainder but sometimes change whether the number is divisible by another divisor?

## Build the table by multiplying

Write two lists of numbers as coefficients of $1,x,x^2,\ldots$. When you multiply, a pair contributes to $x^k$ only if its two powers add to $k$. We write $[x^k]$ to pick out that coefficient. This is a **formal power series**: to find any one coefficient you need only finitely many terms, and you never have to assign a value to $x$.

Let $B_n(t)=[x^t]\,(1-x)^{-n}$. For $n\ge1$ this counts the ways to put $t$ identical objects in $n$ labelled boxes: $\binom{n+t-1}{t}$. For $n=0$ it is $1$ at $t=0$ and $0$ otherwise. In particular $B_n(0)=1$ and $B_n(1)=n$. The other list comes from $L(x)=\log((1-x)/(1-2x))$: the coefficient at $x^j$ is $(2^j-1)/j$ for $j\ge1$, and the constant coefficient is zero. With row and column numbered from zero, the entry $A(n,k)=k![x^k]\,(1-x)^{-n}L(x)$ is therefore

$$A(n,k)=\sum_{j=1}^k\frac{k!}{j}(2^j-1)B_n(k-j).$$

Every denominator $j$ is one of the factors of $k!$, so all entries are integers; column zero is the empty sum. At $k=3$ the three contributions are $3n(n+1)$, $9n$ and $14$. This one sum explains both the remainders and the polynomial pattern.

## Change the divisor, change the survivor

Working modulo $k$ means keeping only remainders on division by $k$. Cancelling a factor $j<k$ from $k!$ leaves the factor $k$ in place. All but the last term disappear, leaving $(k-1)!(2^k-1)$, which has no $n$ in it. For prime $p$, Wilson's theorem gives $(p-1)!\equiv-1$, and Fermat's little theorem gives $2^p\equiv2$, so the remainder is $-1$ in modular notation, or $p-1$ in ordinary remainder notation. For composite $k$, its factors usually fit inside $(k-1)!$: use two distinct factors if possible, or use $a$ and $2a$ for a square $k=a^2$ with $a\ge3$. Column $4$ is the exception and always leaves $2$; $1$ divides every entry in its column and is not prime. The divisibility test does not include column zero.

Now divide by $p-1$. For $p=2$ the divisor is $1$. For odd primes, the terms with $j<p-1$ still have a factor $p-1$, and so does the final term. Only the next-to-last term can obstruct division, because it contains $B_n(1)=n$. At $p=3$ it gives $n$ modulo $2$; at $p=5$ it gives $2n$ modulo $4$. For $p\ge7$, the composite $p-1$ already divides $(p-2)!$, so odd rows also work. Whenever the quotient $q$ is an integer, $(p-1)q\equiv-1\pmod p$ forces $q\equiv1\pmod p$. For instance $A(1,3)=29$ is not divisible by $2$, but $A(1,7)=218868$ is divisible by $6$, and its quotient $36478$ leaves remainder $1$ modulo $7$.

The short film tracks the surviving term as the divisor changes.

::: {.film src="001-prime-columns"}
:::

## Why a column is a polynomial

The product formula $B_n(t)=n(n+1)\cdots(n+t-1)/t!$ makes each fixed column $k\ge1$ a polynomial $P_k$ in the row number. The $j=1$ term alone has the highest degree, $k-1$, and its leading coefficient is $k$. After the factorial scaling the coefficients are nonnegative integers. In column 3 we get $3n^2+12n+14$. Its first three points determine it: the difference of two polynomials of degree at most two cannot have three distinct roots unless it is zero. That is why [A355259](https://oeis.org/A355259) can recover column $k+1$ from the first $k+1$ entries. The proof supplies the degree bound before doing any interpolation.

## Scope and sources

The same setup gives recurrences, a fixed-row growth rate, and an extension replacing $2$ by any integer. The growth estimate does not let the row index grow with the column, and the paper does not cover every combinatorial interpretation, integral or nonterminating special-function formula of the linked sequences. [Statements and proofs](results.md) gives the exact scope and distinguishes the arithmetic already expressed in Lean from the written arguments.

This reading accompanies Haobo Ma and Wenlin Zhang's paper, version 2, [DOI 10.5281/zenodo.24406609](https://doi.org/10.5281/zenodo.24406609), CC BY 4.0. The questions are from Peter Luschny and Mélika Tebni's [OEIS A355257](https://oeis.org/A355257), revision 37; the column-polynomial and even-row quotient conjectures are attributed to Tebni. The all-row prime residue is not new: Benyattou and Mihoubi's [Lah-polynomial congruence](https://doi.org/10.2989/16073606.2017.1391349) (published online 2017, Proposition 8) gives row zero, and a row difference propagates it. [Fried's proof](https://oeis.org/A355372/a355372_1.pdf) (2025, Theorem 1) directly treats row $n=3$ and can likewise be propagated. This reading follows the paper's alternative argument from the recorded coefficient sum and its sharp quotient criterion.
