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

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/tebni355257-logcoef/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/tebni355257-logcoef/tebni355257-logcoef/zh/) · [Read in English](https://papers.trureturing.org/tebni355257-logcoef/tebni355257-logcoef/en/)

[Slides](https://papers.trureturing.org/tebni355257-logcoef/tebni355257-logcoef/slides/) ([sources](books/tebni355257-logcoef/slides/)) · [Videos](https://papers.trureturing.org/tebni355257-logcoef/tebni355257-logcoef/films/) ([sources](books/tebni355257-logcoef/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/tebni355257-logcoef/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `column-identities` | none | — |
| `column-interpolation` | none | — |
| `composite-factorial` | none | — |
| `negative-row` | none | — |
| `row-growth` | none | — |
| `row-recurrences` | none | — |
| `sharp-arithmetic` | special case | `D5/S3/Arith/Congruence/TebniA355257Quotient.result` |
| `signed-parameters` | special case | `D5/S3/Arith/Congruence/TebniA355257Divisibility.result` |
| `six-rows` | special case | `D5/S3/Arith/Congruence/TebniA355257Divisibility.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/tebni355257-logcoef/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
