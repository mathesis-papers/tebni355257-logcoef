# Sharp quotients and column polynomials: alternative proofs for OEIS A355257, revision 37, Comments, after Benyattou-Mihoubi (2017) and Fried (2025)

**Authors:** Haobo Ma, Wenlin Zhang

With alternative prime-residue proofs following Benyattou and Mihoubi (2017, Proposition 8) and Fried (2025, Theorem 1), we prove the four statements labelled Conjecture in Luschny and Tebni's OEIS entry A355257, revision 37, Comments, including its A355259 column-polynomial statement. For the logarithmic coefficient array A(n,k), every prime column has residue -1, and k divides A(n,k) holds exactly for nonprime k >= 1, apart from k = 4, whose residue is always 2. The quotient A(n,p)/(p-1) is integral and congruent to 1 modulo p for every even row; evenness is necessary only at p = 3,5. A factorial coefficient expansion also gives fixed-row recurrences, asymptotics, and an integer-parameter extension.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24406609](https://doi.org/10.5281/zenodo.24406609)
- Concept DOI: [https://doi.org/10.5281/zenodo.24406608](https://doi.org/10.5281/zenodo.24406608)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [tebni355257-logcoef](https://mathesis-omega-research.apps.chrono-ai.fun/papers/tebni355257-logcoef?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Sharp quotients and column polynomials: alternative proofs for OEIS A355257, revision 37, Comments, after Benyattou-Mihoubi (2017) and Fried (2025). Mathesis, version 2. https://doi.org/10.5281/zenodo.24406609

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/3978330935ee256403f739686c6ae335ea620e68/D5/S3/Arith/Congruence/TebniA355257Divisibility.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
