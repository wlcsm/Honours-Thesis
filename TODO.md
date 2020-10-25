# General
* Just mention that we can do constant time bit operations

* Mention what "linear time" is in the preliminaries
* Need to say that in the asymptotic analysis we have a normalised DFT
* In the FFT stuff, make sure I put the negative in the exponent in the forward DFT
* In FFT, be consistent in either using $n$ or $N$
* Algebraic complexity theory book has a good theorem for the Chinese remainder theorem
* Do I really need the rou-results lemma or can I just write the proofs when I need them?
* Maybe say that we will try to say "ring" operations
* I think we need to say something like "We will consider that ram model in Hanna's paper, and the Turing machine. However, for simplicity when working in arbitrary rings, we will often quantify the runtime as the number of "ring operations"
* I think multiplications are supposed to be time $M$ and convolutions are time $\M{M}$
* Mention in the preliminaries that rearranging things in the Turing model make take time 
* Ask Martin where he thinks the section on convolutions should go
* Talk about making the theorems in the asymptotic analysis section different from the ones in the paper
* I just realised why we need to have the definition of the root of unity, its because the DFT requires a ROU but the FFT requires a primitive ROU.
* Be consistent with x and X in the FFT stuff
* Be consistent when using R and K
* Solving systems of equations faster gives a good result for multivariate polynomial multiplication
* Mention in preliminaries if we were strictly considering the ram model then we could just convert everything into integer multiplication and then we could do dfts and convolutions in constant time. So we need to define a different RAM model
* Might need to say that in the RAM model, ring operations are also executed in constant time
* Martin says put in some metrics about nPoly, like the number of lines
* Include Bluesteins trick
* The equivalence between integer mult and polynomial mult, I think maybe we can actually find an equivalence now?
* Instead of writing sooooo many tildes, I want to say something like the "approximation space", and also for maps as well, ideally with one symbol
* For the asymptotic analysis section I want it to follow this outline
    + Overview of the major steps i.e. the theorems at the beginning of the sections and how they fit together
    + Formally proving theorems
    + Formally prove the main theorem using the rigorous definition.
* H-vdH use Kronecker substitution with log. What if we go even smaller? We can't do sqrt(n) because the coefficients become too big. Maybe we can also use that idea for showing equivalence with integer mult and polynomial mult.
* Finish off the Schonage and Strassen one
* Can we view Gaussian resampling as a heat diffusion
* Classical Algorithm still need to finish off Martin's comments
* Say what a twiddle factor is
* Why can't we apply the integer multiplication algorithm for multiplication in $\F_q[x]$. I think its because the coefficient size increase will be too much
* Probably have a note somewhere to say that we could actually just convert polynomial to integers and then multiply that way and then its free money in the RAM model. 
* Need to mention in the FFT that the field needs to have 2 is invertible
* In the finite fields one, should we include quotient rings? Maybe the interpretation that multiplication is a lattice operation
* How much precision is lost in the complex FFT
* Essentially-Optimal-Sparse-Poly.... intro has a nice summary of the space requirements for polynomials
- In the nlogn paper page 32 they mention that their algorithm may be good in practice to replace Rader's algorithm
* Toom-Cook algorithm?
- In nlogn paper page 31 they say that certain constraints are not necessary and that loosening one may actually be easier from a computational viewpoint 
* In the preliminaries maybe we should mention that polynomial addition is linear, and it is asymptotically optimal
- End of introduction
"This should be expanded to include references to the sections and likely some
citations to the relevant papers. A bit of historical discussion and context would also be good as well as comments about the use of various algorithms in different software packages etc."
* In kronecker-talk.pdf, they said that "the Magma computer algebra system uses Kronecker substitution to multiply polynomials in Z[x] in some cases [6], and Victor Shoup’s NTL library [5] uses Kronecker substitution to reduce multiplication in GF(pn)[x] to multiplication in GF(p)[x]"
* In "faster-poly-mult-kronecker-sub.pdf" Harvey just cites the original magma paper but the paper does mention kronecker substitution. 
* Feel like I am forgetting about the computation model in my thing

# Preliminaries
- Check the recursive relation for Karatsuba's algorithm for the "Recursive relation" subsection

# Classical Algorithms
- Need to find some resource that says all the complexity times when applying Kronecker substitution
- In the SS algorithm I haven't taken into account the fact that n might not be square and we also need to round n to the largest power of two.

# Evaluation and Interpolation Strategy
- My proof of the lemma at the beginning of nlogn need to be polished and check (can we do it simpler?)

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

# Secondary Thought
* Verifying the result is correct. Can just evaluate it, or use the Essentially optimal algorithms one. They actually say in Section 3 that a deterministic algorithm doesn't exist
* Does the algorithm in Essentially-optimal ... rely on the O(n log n) integer mult?
- Write up my algorithm for searching for a divisible monomial in a monomial ideal.
* Normal bases? Montgomery multiplication or Barry reduction?
- Do I need to cover Furer's algorithm? Or Harvery-van der Hoeven-Lecerf algorithm?
* Cover Winograd's generalised FFT algorithm?
