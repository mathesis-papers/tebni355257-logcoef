# Statements and proofs

Write $F_n(x)=(1-x)^{-n}L(x)$ with $A,B_n,L$ as in the previous chapter. The rising product $z^{\overline t}=\prod_{i=0}^{t-1}(z+i)$ is $1$ when $t=0$.

::: {.remark #sharp-arithmetic title="Theorem 1: Divisibility and prime quotients" mathesis="collected:tebni355257-logcoef:2:s1"}
For all $n,k\ge0$, $A(n,k)$ is integral. For every prime $p$, $A(n,p)\equiv-1\pmod p$. For $k\ge1$ with $k\ne4$, $k\mid A(n,k)$ if and only if $k$ is not prime; $A(n,4)\equiv2\pmod4$. The quotient $A(n,p)/(p-1)$ is integral in every row for $p=2$ and primes $p\ge7$; at $p=3,5$ it is integral exactly when $n$ is even. Every integral quotient is $1$ modulo $p$.
:::

::: {.proof #pf-sharp-arithmetic}
Original Sections 2–3. The coefficient sum gives integrality and reduces modulo $k$ to $(k-1)!(2^k-1)$. Wilson and Fermat give the prime case. The factorial lemma below handles composites; $1$ is immediate, and the last term at $k=4$ is $90$. Modulo $p-1$ only the next-to-last term can survive, giving $p(p-2)!(2^{p-1}-1)n$. The divisor is $1$ at $p=2$; for $p\ge7$ the factorial lemma applies. At $3$ and $5$ the residues are $n$ modulo $2$ and $2n$ modulo $4$, respectively. Multiply an integral quotient back by $p-1\equiv-1\pmod p$ to read off its residue $1$.
:::

Public frozen Lean theorems cover the integer witness, prime residue, divisibility away from $k=4$, and the even-row quotient. That last declaration does not cover odd rows: the odd-row failures at $3,5$, successes at $p\ge7$, and the residue at column $4$ are not statements of those public theorems.

::: {.remark #composite-factorial title="Lemma 2: A composite and the preceding factorial" mathesis="collected:tebni355257-logcoef:2:s2"}
If $m>1$ is composite and $m\ne4$, then $m\mid(m-1)!$. Write $m=ab$ with $2\le a\le b<m$. If $a<b$, both factors occur in the factorial. If $a=b$, then $a\ge3$, and the distinct factors $a,2a$ occur and multiply to $2m$. The same lemma is already proved as an internal helper in the frozen implementation, not exposed as a public result.
:::

::: {.corollary #column-interpolation title="Corollary 3: Recovering the whole column" mathesis="collected:tebni355257-logcoef:2:s3" status="written-proof" proof="pf-column-interpolation" doi="10.5281/zenodo.24406609" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/586"}
For every $k\ge0$, the polynomial of degree at most $k$ interpolating $(n,A(n,k+1))$ for $0\le n\le k$ is $P_{k+1}$, so it gives the column at every $n\ge0$. For $d\ge1$, the explicit polynomial is
$$P_d(z)=\sum_{j=1}^d\binom dj(j-1)!(2^j-1)z^{\overline{d-j}}.$$
:::

::: {.proof #pf-column-interpolation}
Original Section 4. Substitute $B_n(t)=n^{\overline t}/t!$ into the coefficient sum to obtain $A(n,d)=P_d(n)$. Only $j=1$ reaches degree $d-1$, with leading coefficient $d$. Set $d=k+1$. Two polynomials of degree at most $k$ that agree at $k+1$ distinct points have zero difference. This is the interpolation used in A355259.
:::

::: {.remark #six-rows title="Corollary 4: Six named rows" mathesis="collected:tebni355257-logcoef:2:s4"}
Rows $0,1,2,3,4,5$ are A029767, A103213, A355171, A355372, A355407 and A355414 respectively, by their generating functions $F_n$. They inherit the prime residue and divisibility criterion; every prime quotient is integral in rows $0,2,4$, and precisely $3,5$ fail in rows $1,3,5$. For $k\ge1$, row zero is $(k-1)!(2^k-1)$ because only $j=k$ contributes. The labels identify the source sequences rather than create new proof obligations.
:::

::: {.corollary #column-identities title="Corollary 5: An alternate sum and a column difference" mathesis="collected:tebni355257-logcoef:2:s5" status="written-proof" proof="pf-column-identities" doi="10.5281/zenodo.24406609" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/587"}
For $n\ge0,k\ge1$, $A(n,k)=k!\sum_{j=1}^k\binom{n+k-1}{k-j}/j$. Set $P_0=0$. For $k\ge1$, $P_k(z+1)-P_k(z)=kP_{k-1}(z+1)$, and
$$\sum_{k\ge0}P_{k+1}(z)\frac{x^k}{k!}=\frac{zL(x)+(1-2x)^{-1}}{(1-x)^{z+1}}.$$
:::

::: {.proof #pf-column-identities}
Original Section 4. Expand $L$ as $\sum_{j\ge1}x^j/[j(1-x)^j]$ and take coefficients for the alternate sum. The identities $F_{z+1}-F_z=xF_{z+1}$ and $L'=1/[(1-x)(1-2x)]$ give the difference and exponential generating function by coefficient comparison and differentiation. First use nonnegative integer $z$, then extend because every coefficient is polynomial in $z$.
:::

::: {.corollary #row-recurrences title="Corollary 6: Fixed-row recurrences" mathesis="collected:tebni355257-logcoef:2:s6" status="written-proof" proof="pf-row-recurrences" doi="10.5281/zenodo.24406609" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/588"}
Fix $n\ge0$ and let $a_k=A(n,k)$. Then $a_0=0,a_1=1$ and for $k\ge2$,
$$a_k=(3(k-1)+n)a_{k-1}-2(k-1)(k-2+n)a_{k-2}+n^{\overline{k-1}}.$$
For $r\ge0$,
$$\begin{aligned}a_{r+3}={}&(4r+2n+7)a_{r+2}\\&-[5r^2+(6n+12)r+n^2+8n+7]a_{r+1}\\&+2(r+1)(r+n+1)(r+n)a_r.\end{aligned}$$
:::

::: {.proof #pf-row-recurrences}
Original Section 5. In the differential identity $(1-x)(1-2x)F_n'-n(1-2x)F_n=(1-x)^{-n}$, take the $x^{k-1}$ coefficient and multiply by $(k-1)!$ for the first recurrence. Apply $(1-x)d/dx-n$ first to kill the right side and take the coefficient of $x^{r+1}/(r+1)!$ for the second. Rows $0,1,3,5$ specialize to the recurrences credited to Mathar, Israel, Tebni and Mathar, respectively.
:::

::: {.corollary #row-growth title="Corollary 7: Fixed-row growth" mathesis="collected:tebni355257-logcoef:2:s7" status="written-proof" proof="pf-row-growth" doi="10.5281/zenodo.24406609" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/589"}
For every fixed $n\ge0$, $A(n,k)\sim2^{k+n}(k-1)!$ as $k\to\infty$: the ratio tends to $1$. The cases $n=1,2$ match the OEIS formulas of Alcover and Kotesovec, respectively.
:::

::: {.proof #pf-row-growth}
Original Section 5. Row zero follows from its closed form. For $n\ge1$, divide the coefficient sum by $2^k(k-1)!$ and put $r=k-j$. The summand is $\frac{k}{k-r}(2^{-r}-2^{-k})B_n(r)$. For $r\le k/2$, it is bounded by the summable sequence $2^{1-r}B_n(r)$ and tends termwise to $2^{-r}B_n(r)$. The other half is bounded in total by a constant times $k^n\sum_{r>k/2}2^{-r}$, which tends to zero. Thus the limit is $(1-1/2)^{-n}=2^n$.
:::

::: {.corollary #signed-parameters title="Corollary 8: Integer parameters" mathesis="collected:tebni355257-logcoef:2:s8" status="written-proof" proof="pf-signed-parameters" doi="10.5281/zenodo.24406609" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/590"}
For $b,n\in\mathbb Z$ and $k\ge0$, $C_b(n,k)=k![x^k]\,(1-x)^{-n}\log((1-x)/(1-bx))$ is integral. For $k\ge1$, $C_b(n,k)\equiv(k-1)!(b^k-1)\pmod k$; for prime $p$, $C_b(n,p)\equiv1-b\pmod p$. Every composite $k\ne4$ divides its entry; a prime $p$ divides its entry exactly when $p\mid b-1$; $4$ divides its entry exactly when $b$ is odd. The prime quotient $C_b(n,p)/(p-1)$ is integral if $p=2$, $p\ge7$ or $b$ is odd; when $b$ is even and $p=3,5$ it is integral exactly when $n$ is even. Every integral quotient is $b-1$ modulo $p$.
:::

::: {.proof #pf-signed-parameters}
Original Section 5. For $n<0$, $B_n(r)=(-1)^r\binom{-n}{r}$ is still integral, and $B_n(1)=n$. Replace $2^j-1$ by $b^j-1$ in the coefficient sum. The last term modulo $k$, Wilson and Fermat give divisibility, with $6(b^4-1)$ at column $4$. The next-to-last term modulo $p-1$ gives $(b^2-1)n$ at $3$ and $2(b^4-1)n$ at $5$; $2$ is automatic and $p\ge7$ uses the factorial lemma. Multiply back by $p-1$ to obtain the residue of any integral quotient.
:::

::: {.corollary #negative-row title="Corollary 9: Two formulas for row minus one" mathesis="collected:tebni355257-logcoef:2:s9" status="written-proof" proof="pf-negative-row" doi="10.5281/zenodo.24406609" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/591"}
A355258 is $C_2(-1,k)$. For $k\ge2$ the formulas of Kotesovec and Meya are, respectively,
$$C_2(-1,k)=[1+2^{k-1}(k-2)]\,(k-2)!=k!\sum_{r=0}^{k-2}\frac{\binom{k-2}{r}}{r+2}.$$
:::

::: {.proof #pf-negative-row}
Original Section 5. Multiply by $1-x$ to get $C_2(-1,k)=A(0,k)-kA(0,k-1)$, then substitute the row-zero formula. Alternatively take coefficients of $(1-x)\sum_{j\ge1}x^j/[j(1-x)^j]$; the $j=1$ term vanishes at $k\ge2$ and setting $r=j-2$ gives the binomial sum.
:::
