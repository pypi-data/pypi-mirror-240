# primeclassify

A library of functions to classify prime numbers

Each classification function takes an argument, `p`, which *is assumed
to be a prime number*. There also are optional arguments `tout` and
`store`. `tout` is the maximum processing time the function may take
and `store` is the maximum number of data values it can store. These
are self enforced. Some have additional optional arguments.

Generally, classifications that depend on a number base assume base 10.

Each returns one of:

* `False` (`p` not a member of that classification), or
* `None` (could not complete test), or
* something other than `False` or `None` (`p` a member of that classification) — usually `True`, but sometimes additional information (such as, for twin primes,
which primes it is a twin of)

A return value of `None` may mean it is literally unknown whether `p` is in that classification, or just that the function doesn't know and doesn't care to find out. For example, the largest known Mersenne prime is M<sub>82,589,933</sub> = 2<sup>82,589,933</sup> − 1, but the `mer` function will return 'None' for any 'p' larger than M<sub>127</sub>.

There are in addition a few utility functions.

# Classification functions

* `balanced (p, tout=0, stor=0)` [Balanced prime](https://en.wikipedia.org/wiki/Balanced_prime)
* `chen (p, tout=0, stor=0)` [Chen prime](https://en.wikipedia.org/wiki/Chen_prime)
* `circular (p, tout=0, stor=0)` [Circular prime](https://en.wikipedia.org/wiki/Circular_prime)
* `cluster(p, tout=0, stor=0)` [Cluster prime](https://en.wikipedia.org/wiki/Cluster_prime)
* `cousin(p, tout=0, stor=0)` [Cousin prime](https://en.wikipedia.org/wiki/Cousin_prime) (returns `False` or tuple of its cousins)
* `cuban(p, tout=0, stor=0)` [Cuban prime](https://en.wikipedia.org/wiki/Cuban_prime) (returns `False` or (1 or 2 indicating which series))
* `cullen(p, tout=0, stor=0)` [Cullen prime](https://en.wikipedia.org/wiki/Cullen_prime)
* `delicate(p, tout=0, stor=0)` [Delicate prime](https://en.wikipedia.org/wiki/Delicate_prime)
* `dihedral(p, tout=0, stor=0)` [Dihedral prime](https://en.wikipedia.org/wiki/Dihedral_prime)
* `dbmer(p, tout=0, stor=0)` [Double Mersenne prime](https://en.wikipedia.org/wiki/Double_Mersenne_prime)
* `emirp(p, tout=0, stor=0)` [Emirp](https://en.wikipedia.org/wiki/Emirp)
* `even(p, tout=0, stor=0)` Even prime
* `factorial(p, tout=0, stor=0)` [Factorial prime](https://en.wikipedia.org/wiki/Factorial_prime)
* `fermat(p, tout=0, stor=0)` [Fermat prime](https://en.wikipedia.org/wiki/Fermat_number)
* `fibo(p, tout=0, stor=0)` [Fibonacci prime](https://en.wikipedia.org/wiki/Fibonacci_prime)
* `fortunate(p, tout=0, stor=0)` [Fortunate prime](https://en.wikipedia.org/wiki/Fortunate_prime)
* `good(p, tout=0, stor=0)` [Good prime](https://en.wikipedia.org/wiki/Good_prime)
* `happy(p, tout=0, stor=0)` [Happy prime](https://en.wikipedia.org/wiki/Happy_prime)
* `higgs(p, expt=2, tout=0, stor=0)` [Higgs prime](https://en.wikipedia.org/wiki/Higgs_prime) with exponent `expt`
* `lartrunc(p, tout=0, stor=0)` [Left-and-right-truncatable prime](https://en.wikipedia.org/wiki/Left-and-right-truncatable_prime)
* `ltrunc(p, tout=0, stor=0)` [Left-truncatable prime](https://en.wikipedia.org/wiki/Left-truncatable_prime)
* `lucas(p, tout=0, stor=0)` [Lucas prime](https://en.wikipedia.org/wiki/Lucas_prime)
* `mer(p, tout=0, stor=0)` [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime)
* `mills(p, tout=0, stor=0)` [Mills prime](https://en.wikipedia.org/wiki/Mills_prime)
* `minimal(p, tout=0, stor=0)` [Minimal prime](https://en.wikipedia.org/wiki/Minimal_prime_(recreational_mathematics))
* `motzkin(p, tout=0, stor=0)` [Motzkin prime](https://en.wikipedia.org/wiki/Motzkin_prime)
* `nsw(p, tout=0, stor=0)` [Newman–Shanks–Williams prime](https://en.wikipedia.org/wiki/Newman%E2%80%93Shanks%E2%80%93Williams_prime)
* `pal(p, tout=0, stor=0)` [Palindromic prime](https://en.wikipedia.org/wiki/Palindromic_prime)
* `pell(p, tout=0, stor=0)` [Pell prime](https://en.wikipedia.org/wiki/Pell_prime)
* `pelllucas(p, tout=0, stor=0)` [Pell-Lucas prime](https://en.wikipedia.org/wiki/Pell-lucas_prime)
* `permutable(p, tout=0, stor=0)` [Permutable prime](https://en.wikipedia.org/wiki/Permutable_prime)
* `pierpont(p, tout=0, stor=0)` [Pierpont prime](https://en.wikipedia.org/wiki/Pierpont_prime)
* `pillai(p, tout=0, stor=0)` [Pillai prime](https://en.wikipedia.org/wiki/Pillai_prime)
* `primequadruplet(p, tout=0, stor=0)` [Prime quadruplet prime](https://en.wikipedia.org/wiki/Prime_quadruplet) (returns `False` or tuple of triples of other three members of quadruplets)
* `primetriplet(p, tout=0, stor=0)` [Prime triplet prime](https://en.wikipedia.org/wiki/Prime_triplet) (returns `False` or tuple of duples of other two members of triplets)
* `primorial(p, tout=0, stor=0)` [Primorial prime](https://en.wikipedia.org/wiki/Primorial_prime)
* `proth(p, tout=0, stor=0)` [Proth prime](https://en.wikipedia.org/wiki/Proth_prime)
* `pyth(p, tout=0, stor=0)` [Pythagorean prime](https://en.wikipedia.org/wiki/Pythagorean_prime)
* `quartan(p, tout=0, stor=0)` [Quartan prime](https://en.wikipedia.org/wiki/Quartan_prime)
* `repu(p, tout=0, stor=0)` [Repunit prime](https://en.wikipedia.org/wiki/Repunit_prime)
* `rtrunc(p, tout=0, stor=0)` [Right-truncatable prime](https://en.wikipedia.org/wiki/Right-truncatable_prime)
* `safe(p, tout=0, stor=0)` [Safe prime](https://en.wikipedia.org/wiki/Safe_prime)
* `sexy(p, tout=0, stor=0)` [Sexy prime](https://en.wikipedia.org/wiki/Sexy_prime) (returns `False` or tuple of its sexy partners. Yes, I said that.)
* `sophie(p, tout=0, stor=0)` [Sophie Germain prime](https://en.wikipedia.org/wiki/Sophie_Germain_prime)
* `strobe(p, tout=0, stor=0)` [Strobogrammatic prime](https://en.wikipedia.org/wiki/Strobogrammatic_number)
* `strong(p, tout=0, stor=0)` [Strong prime](https://en.wikipedia.org/wiki/Strong_prime)
* `superprime(p, tout=0, stor=0)` [Super-prime](https://en.wikipedia.org/wiki/Super-prime)
* `supersing(p, tout=0, stor=0)` [Supersingular prime](https://en.wikipedia.org/wiki/Supersingular_prime_(moonshine_theory)) (of moonshine theory)
* `twin(p, tout=0, stor=0)` [Twin prime](https://en.wikipedia.org/wiki/Twin_prime) (returns `False` or tuple of its twins.)
* `wagstaff(p, tout=0, stor=0)` [Wagstaff prime](https://en.wikipedia.org/wiki/Wagstaff_prime)
* `wief(p, tout=0, stor=0)` [Wieferich prime](https://en.wikipedia.org/wiki/Wieferich_prime)
* `williams(p, b=3, tout=0, stor=0)` [Williams prime](https://en.wikipedia.org/wiki/Williams_number) (returns `False` or `n`)
* `wilson(p, tout=0, stor=0)` [Wilson prime](https://en.wikipedia.org/wiki/Wilson_prime)
* `wolsten(p, tout=0, stor=0)` [Wolstenhome prime](https://en.wikipedia.org/wiki/Wolstenholme_prime)
* `woodall(p, tout=0, stor=0)` [Woodall prime](https://en.wikipedia.org/wiki/Woodall_prime)

# Utility functions

* `class_from_list (p, thelist, complete, limit=None)` Used internally
* `describe(p, tout=0, stor=0, extras={higgs: (2,), williams: (3, 10)})` Returns a list of classifications passed by `p`. Functions are called with `tout=tout, stor=stor`. `extras` give limits for additional arguments.
* `test_classify (fn, limit1, limit2=-1, tout=0, stor=0, extra=None)` Calls function `fn` for primes `p` in range [2, limit1] or [limit1, limit2], with `tout=tout, stor=stor`, and prints results. `extra` is extra argument for functions that take one.

# Classifications not included

These are not integer primes:

* [Eisenstein prime](https://en.wikipedia.org/wiki/Eisenstein_integer#Eisenstein_primes)
* [Gaussian prime](https://en.wikipedia.org/wiki/Gaussian_prime)

These are just too hard for me to code!

* [Full reptend prime](https://en.wikipedia.org/wiki/Full_reptend_prime)
* [Genocchi prime](https://en.wikipedia.org/wiki/Genocchi_prime)
* [Highly cototient prime](https://en.wikipedia.org/wiki/Highly_cototient_prime)
* [Lucky prime](https://en.wikipedia.org/wiki/Lucky_prime)
* [Ramanujan prime](https://en.wikipedia.org/wiki/Ramanujan_prime)
* [Regular (and irregular) prime](https://en.wikipedia.org/wiki/Regular_prime)
* [Supersingular prime](https://en.wikipedia.org/wiki/Supersingular_prime_(algebraic_number_theory)) (of algebraic number theory)
* [Wall-Sun-Sun prime](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime)

----

Author: Rich Holmes  
Source repository: https://gitlab.com/rsholmes/primeclasses
