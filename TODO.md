# Last Position

Classical algorithms line 42

# General
- Do I need to cover Furer's algorithm? Or Harvery-van der Hoeven-Lecerf algorithm?
- In the nlogn paper page 32 they mention that their algorithm may be good in practice to replace Rader's algorithm
- In nlogn paper page 31 they say that certain constraints are not necessary and that loosening one may actually be easier from a computational viewpoint 
* In the preliminaries maybe we should mention that polynomial addition is linear, and it is asymptotically optimal
- Define the cyclic convolution property as it is mentioned in the beginning of 5.1, or I could reword Theorem 3 to not use that term
* It is hard to say that one algorithm beats another at precisely a certain degree because it is very much dependent on the implementation and the hardware as well, some algorithms lend themselves better to parallel or SIMD processing. But I suppose it should be all formulated in the perfect RAM model.
* One genuine problem is that integer multiplication schemes have the luxury of having the coefficients of the polynomial bounded. For this reason I will need to develop some technique for bounding them. Otherwise I can't really talk about SS and H-vdH in the Preliminaries and I also need to make the nlogn paper relevant
- Write up my algorithm for searching for a divisible monomial in a monomial ideal.
- Is the fact that the fftw paper is an "invited paper" mean anything?
- End of introduction
"This should be expanded to include references to the sections and likely some
citations to the relevant papers. A bit of historical discussion and context would also be good as well as comments about the use of various algorithms in different software packages etc."
* Bluestein's Trick: Converts a DFT problem to a convolution problem
* In FASTER POLYNOMIAL MULTIPLICATION VIA MULTIPOINT KRONECKER SUBSTITUTION, they said that "the Magma computer algebra system uses Kronecker substitution to multiply polynomials in Z[x] in some cases [6], and Victor Shoup’s NTL library [5] uses Kronecker substitution to reduce multiplication in GF(pn)[x] to multiplication in GF(p)[x]"

# Preliminaries
- Check the recursive relation for Karatsuba's algorithm for the "Recursive relation" subsection

# Classical Algorithms
- Chinese Remainder Theorem at the end to unify all the approaches
- Need to find some resource that says all the complexity times when applying Kronecker substitution
- In the SS algorithm I haven't taken into account the fact that n might not be square and we also need to round n to the largest power of two.

# Evaluation and Interpolation Strategy
- My proof of the lemma at the beginning of nlogn need to be polished and check (can we do it simpler?)

# Finite Fields

# Implementation Details

# Overview of nlogn
* Theorem 3.1 to perform the calculation on the t_1, \ldots, t_d
* Lemma 3.2 Can construct a numerical approximation to a synthetic DFT with inputs $R^t$ with $t$ a power of two
* Proposition 3.3 Can construct a numerical approximation of multi-dimensional DFT's where each dimension is $R^t$ with $t$ a power of two.
    + To distinguish $R^t$ and $\otimes_i R^{t_i}$. Think of the elements of $R^t$ being $R[x]/(x^t - 1)$ and elements in the other being in $R[x_1, \ldots, x_n]/(x_1^{t_1} - 1, \ldots, x_d^{t_d} - 1)$.
* Proposition 3.4 We may use the FFT given in Proposition 3.3 to evaluate the convolution in the normal way
* Proposition 3.5 Can prove the same thing as 3.4 but with complex DFTs (can reduce part of the problem to Prop 3.4)

* Theorem 4.1 to convert the s_1, \ldots, s_d to the power of twos t_1, \ldots, t_d
* Theorem 4.2 Resampling identity, Shows that the $\M{T}\M{P}_s\M{F} = \M{P}_t\M{F}_t\M{S}$, hence if we can solve the system $\M{T}x = y$ then we can find an expression for $\M{F_t}$ in terms of $\M{F_s}$. Indeed it is shown that $\M{D}\M{N}^{-1}\M{C}$ is the inverse where we can maybe explain what these terms are

* Proposition 5.2 combines 4.1 and 3.1 to give the total cost an error of a FFT
* Proposition 5.3 Uses the FFT in Proposition 5.2 to actually make the approximation of multiplication
* Proposition 5.4 Puts it all together to work for integer multiplication.

## Preliminaries

Audience?

* Introduce: Big O notation and some basic algorithms like schoolbook, Karatsuba, and show Chinese remainder theorem being included in Karatsuba, Toom-Cook and 
* This chapter should introduce the basic concepts of both math and the complexity side of things
* Introduce what a Turing machine is
