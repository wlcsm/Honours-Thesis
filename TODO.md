# General
- Do I need to cover Furer's algorithm? Or Harvery-van der Hoeven-Lecerf algorithm?
- Break up preliminaries into two parts, one which is the basic concept and algorithms (maybe just schoolbook and Karatsuba), and another chapter which gives motivation (shows the equivalence with integer multiplication), and the Chinese remainder theorem's role in Karatsuba, Toom-Cook and alluding the FFT one
- Clarify the $\Z/(x^{s_1, \ldots, x_n} - 1)\Z$ isomorphism.
- In the nlogn paper page 32 they mention that their algorithm may be good in practice to replace Rader's algorithm
- In nlogn paper pae 31 they say that certain contraints are not necessary and that loosening one may actually be easier from a computational viewpoint 
- In the code: When applying the division algorithm over a vector of polynomials, it might be more efficient to do the predictive algorithm in $F_4$ and perform all the subtractions at once, this may end up being more computationally efficient
- If I get a fast algorithm for seeing if a monomial is in an ideal then I should include that into the division algorithm
- There is a potential optimisation if we can guarentee that our polynomials are not zero, this avoids algorithms having to check all the time

# Preliminaries
- Big O notation
- Need to find some resource that says all the complexity times when applying Kronecker substitution
- Check the recursive relation for Karatsuba's algorithm for the "Recursive relation" subsection
- I haven't taken into account the fact that n might not be square and we also need to round n to the largest power of two.

# Evaluation and Interpolation Strategy
- My proof of the lemma at the beginning of nlogn need to be polished and check (can we do it simpler?)

# Finite Fields

# Implementation Details

# Rationale

## Preliminaries

Audience?

Introduce: Big O notation and some basic algorithms like schoolbook, Karatsuba, and show Chinese remainder theorem being included in Karatsuba, Toom-Cook and 

This chapter should introduce the basic concepts and 

# Summary of Algorithms/Techniques

* Rader's Algorithm: Very fast multiplication of polynomials of prime powers
* Bluestein's Trick: Converts a DFT problem to a convolution problem
