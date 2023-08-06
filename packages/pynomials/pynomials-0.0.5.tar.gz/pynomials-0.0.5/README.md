# pynomials

This is a simple Mathematical Module which is extremely user-friendly. The module deals with mathematical **Polynomials** in one variable, namely "x". Using this module, the algebra of **Polynomials** can be easily performed in python. \
**Polynomial(an, ..., a2, a1, a0) -> anx^n + ... + a2x^2 + a1x^1 + a0x^0** \
A lot of help text is included in the class, and in the error messages, hence making the module easy to use.

## Attributes of Polynomial objects
Polynomials have the following attributes:
- self.degree = highest power of x
- self.coeffs = (an, ..., a2, a1, a0)
- self.a0, self.a1, self.a2, ... = a0, a1, a2, ...

Note: degree of Zero Polynomial is None as it is left exclusively undefined in Mathematics

## Methods

- add two Polynomials:
    > returns the Polynomial obtained by adding the Polynomials \
    > can be achieved through p1 + p2
- subtract two Polynomials:
    > returns the Polynomial obtained by subtracting the Polynomials \
    > can be achieved through p1 - p2
- multiply two Polynomials:
    > returns the Polynomial obtained by multiplying the Polynomials \
    > can be achieved through p1 * p2
- divide two Polynomials (/, //, %):
    > / : returns the Rational Function obtained by p1 / p2 as a python function \
    > //: returns the Quotient obtained by p1 // p2 if the result is a Polynomial else None \
    > % : returns the Remainder obtained by p1 % p2 if the result of p1 // p2 is a Polynomial else None
- raise Polynomials to integer powers:
    > returns the Polynomial obtained by raising a Polynomial to an integer power \
    > can be obtained through p ** n
- indexing a Polynomial:
    > p[n] -> returns the coefficient of x^n (i.e. coefficient at degree n)
- accessing Polynomial as a function:
    > p1(n) -> returns the value of the Polynomial function at x = n \
    > p1(p2) -> returns the Polynomial obtained by composition defined as P(Q(x)) where P, Q = p1, p2
- Polynomial.derivative(p)
    > returns the Polynomial obtained by differentiating p
- Polynomial.integral(p, c=0)
    > returns the Polynomial obtained by integrating p at value of integrating constant c

Alternate Polynomial constructors:
- Polynomial.FromRoots(root1, root2, ..., rootn)
    > creates a Polynomial of degree n whose roots are given as arguments, where n is the number of roots
- Polynomial.FromSequence(seq)
    > creates a Polynomial whose components are taken from the given list, tuple or generator \
    > the elements of the sequence are passed to the Polynomial() constructor in order

And many more... Each function contains help text that can be accessed through help() in python to know more about it. Users are advised to read help() on methods they want to use to ensure required results.

## Plotting a Polynomial
Two methods allow you to plot the Polynomial on a graph:
- Polynomial.plot(p1, limits=(-100, 100)):
    > plots single Polynomial
- Polynomial.plot_polynomials(p1, p2, p3, ..., pn, limits=(-100, 100), show_legend=True):
    > plots multiple Polynomials on the same grid \
    > show_legend is a boolean which displays legend on the plot if True

Note: limits should be a tuple containing the minimum and maximum values for x

## Updates (0.0.4)
Added two more methods to class Polynomial:
- Polynomial.definite_derivative(p, n)
    > returns the value of derivaitve of p at x = n
- Polynomial.definite_integral(p, a, b)
    > returns the value of integral of p from lower limit a to upper limit b

## Updates (0.0.5)
- Minor bug fixes
- Changes in division of Polynomials using // and % operators. Using these operators on Polynomials now strictly returns Polynomials, as they should.

## Reach out to me
Feel free to reach out to me if you notice any bugs or if you need any kind of help from me in understanding the usage of the module or the source code. My email: knightt1821@gmail.com