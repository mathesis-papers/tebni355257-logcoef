# OEIS A355257, revision 37, Comments: divisibility and quotient conjectures

The note proves the four conjectures in that locator and the polynomial-column
statement in A355259. Its all-row prime congruence also follows from the
Lah-polynomial theorem of Benyattou and Mihoubi (published online November 8,
2017, Proposition 8), through the explicit factorial-weighted map and row identity
proved in the note. The note gives an alternative elementary proof and credits
Sela Fried's explicit row-three prime congruence
(Theorem 1, recorded in the A355372 history on December 17, 2025;
later Theorem 52 of arXiv:2607.24832v1).

## Files and build

- `note.tex`: complete proofs and embedded bibliography.
- `note.pdf`: the mathematical note, supplied alongside the source ZIP.
- `verify.py`: Python 3.10+ standard-library exact arithmetic checks.
- `verification.json`: expected deterministic checker output.
- `metadata.json`: scientific coverage, creators, license and source link.

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, with AMS, Latin Modern, geometry, booktabs, longtable and hyperref:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded; BibTeX is unnecessary. Reproduce the finite checks:

```sh
python3 verify.py > actual-verification.json
cmp verification.json actual-verification.json
```

## Mathematical coverage

For `A(n,k)=k![x^k](1-x)^(-n) log((1-x)/(1-2x))`, every prime
column has residue `-1`. At positive `k != 4`, `k | A(n,k)` holds exactly
when `k` is nonprime; column four always has residue two modulo four.
The prime quotient `A(n,p)/(p-1)` is integral for all rows at `p=2` or
`p>=7`, and exactly at even rows for `p=3,5`. Every integral quotient
has residue one modulo `p`. Column `k` is an integer polynomial of degree
`k-1`, proving the A355259 interpolation conjecture.

Corollaries give explicit fixed-row coverage, the alternate binomial formula,
finite differences, a column generating function, homogeneous and inhomogeneous
recurrences, and `A(n,k) ~ 2^(k+n)(k-1)!` for each fixed nonnegative row.
The recurrence specializations in A029767, A103213, A355372 and A355414 and the
A103213 and A355171 asymptotic formulas are credited to their recorded contributors.

The integer-parameter extension replaces `2` by any integer `b` and permits
integer rows. Its prime residue is `1-b`; integral prime quotients have residue
`b-1`. At `p=3,5` a quotient fails integrality exactly when `b` is even and the
row is odd. This extension and an odd-row converse are not posed in the source;
the coverage table distinguishes them from the actual conjectures.
At row `-1`, the extension gives the closed form and binomial sum in A355258,
credited to Kotesovec (2022) and Meya (2024).

## Verification scope

The universal statements have written proofs in the note. The two linked Lean
files at revision `3978330935ee256403f739686c6ae335ea620e68` concern natural
rows and columns:

- [TebniA355257Divisibility.lean](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean):
  `A_eq_Z` identifies the integer sum; `prime_residue` proves its prime residue;
  `result` proves the divisibility equivalence for `k>=1`, `k!=4`;
  `even_pred_divides` proves divisibility by `p-1` for even rows and prime `p`.
- [TebniA355257Quotient.lean](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Quotient.lean):
  `result` gives an integer quotient and its residue one for even rows and
  prime `p`. The additional corollaries have the written proofs in the note.

Finite checks cover 6,231 coefficient cells (`0<=n<=30`, `0<=k<=200`),
1,426 row/prime pairs, 372 polynomial evaluations, nine published A355259 rows,
6,200 alternate-sum cases, 6,138 homogeneous-recurrence cases, and 372 column
finite differences. The extension is checked independently against a
differential recurrence on 2,925 cells (`-3<=b<=5`, `-6<=n<=6`, `0<=k<=24`),
including 1,053 row/base/prime cases. These finite ranges are not universal proofs.
The A355258 formulas are checked at the 23 degrees from two through twenty-four.
The Lah identification is checked at 264 pairs (`0<=r<=5`, `0<=k<=43`), and
480 polynomial congruences are checked for the earlier theorem, at eight primes
through nineteen, two positive prime multiples and offsets zero through four.

## Sources

- https://oeis.org/A355257 (revision 37, April 13, 2025; Comments and Formula).
- https://oeis.org/A355259 (Comments, Example and Maple program).
- https://oeis.org/A355372/a355372_1.pdf (Fried, Theorem 1).
- https://oeis.org/history?seq=A355372&start=10 (December 17, 2025).
- https://arxiv.org/abs/2607.24832v1 (Fried, Section 3.9, pp. 52--53).
- https://doi.org/10.2989/16073606.2017.1391349 (Benyattou-Mihoubi,
  published online 2017; Proposition 8).
- https://doi.org/10.18514/MMN.2021.3601 (Benyattou-Mihoubi, 2021;
  Proposition 2, the r-Lah extension).
- The note also gives exact structural locators for Nyul-Racz (2015),
  Kargın-Can (2020) and Benyattou's 2018 thesis. The two coefficient sums
  used in its elementary proofs were recorded in A355257, Formula, in July 2022.
- The fixed-row entries A029767, A103213, A355171, A355372, A355407 and
  A355414 are linked in the note's bibliography and coverage table.

## Creators and license

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University
of Singapore; ChronoAI Pte Ltd, Singapore). CC BY 4.0:
https://creativecommons.org/licenses/by/4.0/.
