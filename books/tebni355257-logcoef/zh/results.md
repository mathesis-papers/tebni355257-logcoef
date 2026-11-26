# 陈述与证明

设 $F_n(x)=(1-x)^{-n}L(x)$，沿用上一章的 $A,B_n,L$。记 $z^{\overline t}=\prod_{i=0}^{t-1}(z+i)$，空积为 $1$。

::: {.remark #sharp-arithmetic title="定理 1：整除与质数商" mathesis="collected:tebni355257-logcoef:2:s1"}
对所有 $n,k\ge0$，$A(n,k)$ 是整数。对任意质数 $p$，$A(n,p)\equiv-1\pmod p$。若 $k\ge1$ 且 $k\ne4$，则 $k\mid A(n,k)$ 当且仅当 $k$ 不是质数；第 $4$ 列恒有 $A(n,4)\equiv2\pmod4$。对 $p=2$ 或质数 $p\ge7$，任意行的商 $A(n,p)/(p-1)$ 都是整数；在 $p=3,5$，商为整数当且仅当 $n$ 为偶数。只要商为整数，就模 $p$ 余 $1$。
:::

::: {.proof #pf-sharp-arithmetic}
原文第 2、3 节。系数和式给出整数性，并将模 $k$ 的计算化为 $(k-1)!(2^k-1)$。Wilson 定理和 Fermat 小定理给出质数余数；下述阶乘引理处理合数，$1$ 直接成立，$k=4$ 时末项为 $90$。模 $p-1$ 时，仅倒数第二项可能不消失，故余数同 $p(p-2)!(2^{p-1}-1)n$。对 $p=2$ 除数为 $1$；对 $p\ge7$ 用阶乘引理；$p=3,5$ 时分别为模 $2$ 的 $n$ 和模 $4$ 的 $2n$。最后把整数商乘回 $p-1\equiv-1\pmod p$，推出商余 $1$。
:::

公开的冻结 Lean 定理覆盖整系数见证、质数余数、排除 $k=4$ 的整除判据、偶数行的商；最后三类剩余检查是第 $4$ 列的余数、$3,5$ 的奇数行反向条件和 $p\ge7$ 的奇数行。偶数行声明本身不涵盖这些情况。

::: {.remark #composite-factorial title="引理 2：合数与前一项阶乘" mathesis="collected:tebni355257-logcoef:2:s2"}
若 $m>1$ 为合数且 $m\ne4$，则 $m\mid(m-1)!$。写 $m=ab$，其中 $2\le a\le b<m$。若 $a<b$，两个因子都在阶乘中；若 $a=b$，则 $a\ge3$，阶乘中不同的 $a,2a$ 的积是 $2m$。冻结实现已有同一陈述的内部引理，并非公开可引用的接口。
:::

::: {.corollary #column-interpolation title="推论 3：插值确定整列" mathesis="collected:tebni355257-logcoef:2:s3" status="written-proof" proof="pf-column-interpolation" doi="10.5281/zenodo.24406609" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/586"}
对任意 $k\ge0$，点 $(n,A(n,k+1))$（$0\le n\le k$）的次数不超过 $k$ 的插值多项式等于 $P_{k+1}$，因而对所有 $n\ge0$ 都给出该列。这里对 $d\ge1$ 定义
$$P_d(z)=\sum_{j=1}^d\binom dj(j-1)!(2^j-1)z^{\overline{d-j}}.$$
:::

::: {.proof #pf-column-interpolation}
原文第 4 节。代入 $B_n(t)=n^{\overline t}/t!$ 得 $A(n,d)=P_d(n)$。只有 $j=1$ 项给出 $d-1$ 次项，系数是 $d$。取 $d=k+1$；两个次数不超过 $k$ 的多项式若在 $k+1$ 个不同点处取值相同，其差只能为零。这正是 A355259 的列插值。
:::

::: {.remark #six-rows title="推论 4：六条已知数列" mathesis="collected:tebni355257-logcoef:2:s4"}
第 $0,1,2,3,4,5$ 行依次对应 A029767、A103213、A355171、A355372、A355407、A355414；各自的生成函数就是对应的 $F_n$。因此它们满足定理 1 的质数余数和整除判据；$0,2,4$ 行的所有质数商为整数，$1,3,5$ 行只有质数 $3,5$ 不行。第 $0$ 行在 $k\ge1$ 时等于 $(k-1)!(2^k-1)$，因为和式只剩 $j=k$ 项。数列编号只是识别标签，不是新的证明义务。
:::

::: {.corollary #column-identities title="推论 5：另一种系数和式与列差分" mathesis="collected:tebni355257-logcoef:2:s5" status="written-proof" proof="pf-column-identities" doi="10.5281/zenodo.24406609" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/587"}
对 $n\ge0,k\ge1$，$A(n,k)=k!\sum_{j=1}^k\binom{n+k-1}{k-j}/j$。令 $P_0=0$。对 $k\ge1$ 有 $P_k(z+1)-P_k(z)=kP_{k-1}(z+1)$，且
$$\sum_{k\ge0}P_{k+1}(z)\frac{x^k}{k!}=\frac{zL(x)+(1-2x)^{-1}}{(1-x)^{z+1}}.$$
:::

::: {.proof #pf-column-identities}
原文第 4 节。把 $L$ 写成 $\sum_{j\ge1}x^j/[j(1-x)^j]$ 后取系数便得和式。再用 $F_{z+1}-F_z=xF_{z+1}$ 及 $L'=1/[(1-x)(1-2x)]$，由逐项比较及求导得差分和指数生成函数。先取非负整数 $z$，再由每个系数都是 $z$ 的多项式推广。
:::

::: {.corollary #row-recurrences title="推论 6：固定行递推" mathesis="collected:tebni355257-logcoef:2:s6" status="written-proof" proof="pf-row-recurrences" doi="10.5281/zenodo.24406609" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/588"}
固定 $n\ge0$，令 $a_k=A(n,k)$，则 $a_0=0,a_1=1$，且当 $k\ge2$ 时
$$a_k=(3(k-1)+n)a_{k-1}-2(k-1)(k-2+n)a_{k-2}+n^{\overline{k-1}}.$$
当 $r\ge0$ 时，
$$\begin{aligned}a_{r+3}={}&(4r+2n+7)a_{r+2}\\&-[5r^2+(6n+12)r+n^2+8n+7]a_{r+1}\\&+2(r+1)(r+n+1)(r+n)a_r.\end{aligned}$$
:::

::: {.proof #pf-row-recurrences}
原文第 5 节。微分恒等式 $(1-x)(1-2x)F_n'-n(1-2x)F_n=(1-x)^{-n}$，取 $x^{k-1}$ 项后乘 $(k-1)!$ 得第一个式子；再作用 $(1-x)d/dx-n$ 消去右侧，取 $x^{r+1}/(r+1)!$ 的系数得第二式。第 $0,1,3,5$ 行对应 Mathar、Israel、Tebni、Mathar 已记录的递推式。
:::

::: {.corollary #row-growth title="推论 7：固定行的增长率" mathesis="collected:tebni355257-logcoef:2:s7" status="written-proof" proof="pf-row-growth" doi="10.5281/zenodo.24406609" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/589"}
对每个固定的 $n\ge0$，$A(n,k)\sim 2^{k+n}(k-1)!$（$k\to\infty$）。也就是说，两边的比趋于 $1$；$n=1,2$ 的结论分别见 Alcover 与 Kotesovec 的 OEIS 公式。
:::

::: {.proof #pf-row-growth}
原文第 5 节。零行直接由闭式得出。$n\ge1$ 时，将系数和式除以 $2^k(k-1)!$，以 $r=k-j$ 重排，每项为 $\frac{k}{k-r}(2^{-r}-2^{-k})B_n(r)$。在 $r\le k/2$ 处由可求和的 $2^{1-r}B_n(r)$ 控制，逐项极限为 $2^{-r}B_n(r)$；另一半的总量不超过常数乘 $k^n\sum_{r>k/2}2^{-r}$，趋于零。极限是 $(1-1/2)^{-n}=2^n$。
:::

::: {.corollary #signed-parameters title="推论 8：整数参数扩张" mathesis="collected:tebni355257-logcoef:2:s8" status="written-proof" proof="pf-signed-parameters" doi="10.5281/zenodo.24406609" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/590"}
对 $b,n\in\mathbb Z$ 及 $k\ge0$，$C_b(n,k)=k![x^k]\,(1-x)^{-n}\log((1-x)/(1-bx))$ 为整数。当 $k\ge1$，$C_b(n,k)\equiv(k-1)!(b^k-1)\pmod k$；当 $p$ 为质数，$C_b(n,p)\equiv1-b\pmod p$。合数 $k\ne4$ 总整除该项；质数 $p$ 恰在 $p\mid b-1$ 时整除；$4$ 恰在 $b$ 为奇数时整除第 $4$ 列。若 $p=2$、$p\ge7$ 或 $b$ 为奇数，质数商 $C_b(n,p)/(p-1)$ 总为整数；若 $b$ 为偶数且 $p=3,5$，当且仅当 $n$ 为偶数。每个整数商都模 $p$ 余 $b-1$。
:::

::: {.proof #pf-signed-parameters}
原文第 5 节。$n<0$ 时 $B_n(r)=(-1)^r\binom{-n}{r}$ 仍为整数，且 $B_n(1)=n$。用 $b^j-1$ 替换和式中的 $2^j-1$。按模 $k$ 的末项及 Wilson、Fermat 定理推出整除，列 $4$ 的余数同 $6(b^4-1)$。模 $p-1$ 的倒数第二项在 $3,5$ 时分别同 $(b^2-1)n$ 和 $2(b^4-1)n$；$p=2$ 直接处理，$p\ge7$ 用阶乘引理。把整数商乘回 $p-1$ 即得余数。
:::

::: {.corollary #negative-row title="推论 9：负一行的两个公式" mathesis="collected:tebni355257-logcoef:2:s9" status="written-proof" proof="pf-negative-row" doi="10.5281/zenodo.24406609" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/591"}
A355258 是 $C_2(-1,k)$。对 $k\ge2$，Kotesovec 与 Meya 给出的两个公式分别为
$$C_2(-1,k)=[1+2^{k-1}(k-2)]\,(k-2)!=k!\sum_{r=0}^{k-2}\frac{\binom{k-2}{r}}{r+2}.$$
:::

::: {.proof #pf-negative-row}
原文第 5 节。乘以 $1-x$ 即得 $C_2(-1,k)=A(0,k)-kA(0,k-1)$，代入零行闭式。另一种方法是从 $(1-x)\sum_{j\ge1}x^j/[j(1-x)^j]$ 取系数；在 $k\ge2$ 时 $j=1$ 不贡献，令 $r=j-2$ 即得二项式和。
:::
