<!--==================-->
# Overview
<!--==================-->
- Notes will cover Algebra 1 & 2. It will not cover linear algebra

<!--==================-->
# Glossary
<!--==================-->
- Purpose: recognize patterns, follow procedures, become a logical thinker

## _NOUNS_
- `Algebra`: Language used to describe patterns found in math. Ruleset used to rearrange and generate new expressions/equations from existing ones
- `Constants`: Values that don't change. In math, only coefficients
- `Coefficients`: A num attached to and in front of a variable
- `Equations` = Statements of equality. Left side is equal to the right side.
  - `Simple`: Isolating a variable and getting rid of coefficients
- `Expressions` = No equal signs. Term(s) without an equal sign
- `Inequalities` = Statements of inequality
- `Monomial`: 1 name/term. A value `5a`
- `Polynomials` = Sums of algebraic terms. Sum of many terms
  - `Terms`: Number/expression chunk that is added
    - `Like Terms`: Equivalent bases and equivalent exponents
  - `Quadratic`: Named after an equation with a second degree polynomial. (2) is used to find the area which is a square. A square has 4 sides hence quadratic.
- `Discriminant`: Equation that provides insight into a polynomial.
- `Complex Numbers`: A mix of real/imaginary numbers

  ### Divisions
  - `dividend / divisor = quotient`

  - `Quotient`: Answer in fraction
  - `Dividend`: Numerator in fraction
  - `Divisor`: Denom in fraction
  - `Remainder`: Self explanatory

## _FUNCTIONS
- `Functions`: Relationship between inputs/outputs. Aka vending machine
  - Rectangular grid system
  - Visualize a function as a graph
  - `Even fns`: Fns are symmetric relative to the y-axis. Oppositef values of x will have equivalent values of y
  - `Odd fns`: Fns that are symmetric with respect to the origin. Opposite values of x will have oppositie values of y
  - `Composite`: Applying result of 1 fn to another fn `f(x) and g(x) or f(g(x))`
    - aka kinda like higher order fns
  - `Combo`: Performing an arithmetic operation (+,-,*,/) on 2 fns
  - `1 to 1`: A fn that passes the Horizontal Line Test. Each input corresponds to a unique output.
    - `Inverse Fn`: Only 1-1 fn has an inverse fn. It's a fn that undoes the original fn. It's symmetric to f(x) = x. If original fn has coordinate (x,y) then the inverse fn is (y,x).
      1. Replace all x with y and all y with x.
      2. Solve the equation for y.
      3. Double check hat the inverse are both true
      - Range of fn is the domain of the inverse fn
- `Fn Notation`: A way of writing an equation to show the relationship between input/output
 `Systems of Equations`: Given more than 1 equation, find the variable values that makes all equations in the system valid and true
  - 3 ways to solve systems of equation
    1. Substitution
    2. Elimination
    3. Graphing
  - `Disjunction`: "Or statement." 2 statements with "or"
  - `Conjunction`: "And statement." 2 statements with "and"

  ### 1-1 Fn
  - each elem in the domain maps to a unique element in the codomain. No 2 domains produce the same output
  - `Horizontal Line Test`
  - linear fns and exponential fns
  - One to one funs have an inverse fn

## _ ACTIONS_
- `Inverse Operations`: Opposite operations that undo each other. Subtraction is the inverse of subtraction. Multiplication and division. Exponents and roots (radicals).
- `Factoring`: Undoing polynomial exponents. Extracting a factor(s). Aka transforming a sum problem into 2 expression factors that multiply to get the polynomial
- `Distributing`: Undoing factoring. Distributing a factor to all terms

## _RULES_
  ### Properties
  - `Associative`: Move () freely
  - `Commutative`: Reorder freely
  - `Transitive`: Common var in systems of equations equal each other
  - `Distributive`: Expressions that's factored can be distributed to all the terms in the polynomial

  ### Theorem
  - `Zero Theorem`: Given AB = 0, we know that one of the terms is 0

```py
# Associative
(a + b) + c = a + (b + c)
(ab)c = a(bc)

# Commutative
a + b = b + a
ab = ba

# Transitive
a = b and b = c, then a = c

# Distributive
a(b + c) = ab + ac
```

<!--==================-->
# Order of Operations
<!--==================-->
- Parenthesis+: Grouping symbols
- Exponents
- Multiplication/Division
- Addition/Subtraction

<!--==================-->
# Inequalities
<!--==================-->
- `Law of Trichotomy`: An expression with 2terms can have one of 3 relationships
  - `a == b`
  - `a > b`
  - `a < b`
- `Law of Negative Numbers`: When multiplying/dividing both sides of an inequality, reverse the inequality sign
- `Number line notation`: Similar to the fn notation. Open circle is exclusive. Closed circle is inclusive.

<!--==================-->
# Factoring
<!--==================-->
## _OVERVIEW_
- `Root`: Polynomial is a solution where the polynomial equals zero. Or due to the rational root theorem, find the factor(s) that equal 0
- There are a lot of factoring techniques specifically for quadratics and one for cubes
- Google keywords for specifics on factoring techniques

## _GENERAL STEPS_
1. Grouping (GCF)
2. Special Patterns
  - General
  - Specific
    - Quadratics
    - Cubes (Diff/Sum)
3. Manipulation of equation to look like special pattern
  - Completing the square
4. Long Division by rational root
  - Use the `rational root theorem` to help identify potential rational roots
  - Then use long division

## _PATTERNS_
  ### General Polynomials
  1. Diff of squares (even exponents binomial )
     - `a^2 - b^2 = (a + b)(a - b)`

  ### Quadratics (`x^2`)
  1. Perfect Squares (Trinomial) `a^2 +/- 2ab + b^2`
    - `(a +/- b)^2`
  2. Simple Product/Sum (Trinomial) `ax^2 + bx + c` (a == 1)
    - For 2 nums m & n
      - if `mn == ac` AND `m+n=b`
        - then `(a + m)(a + n)`
  3. Lead Coefficient Product/Sum (Trinomial) `Ax^2 + bx + C`
    - Look at A and C
    - Use A to determine `m,n` the first term of each expression `(m + x)(n + y)`
    - Get all factors of C and by process of elimination, find what works by using the FOIL method to see what will work for

  4. Quadratic Formula `-b +/- rad[b^2 - 4ac] / 2a`

## _MANIPULATION TO PATTERN_
- `Completing the Square`: Factoring when trinomial (product) doesn't work with `ax^2 + bx + c`. Manipulate equation to transform equation into a perfect square trinomial.
  1. Confirm a = 1
  2. Add (b/2)^2 to both sides (this creates the perfect square)
  3. Factor the perfect square
  4. Solve for x

  ### Cubes (`x^3`)
  - `a^3 + b^3 = (a + b)(a^2 - ab + b^2)`
  - `a^3 - b^3 = (a - b)(a^2 + ab + b^2)`

## _POSSIBLE VAR ALUES_
- Zero Theorem: AB = 0
- Can get some possible values of x after factoring a quadratic

<!--==================-->
# Exponents and Radicals
<!--==================-->
## _POWER OF 0_
- Anything to the power of 0 is 1
  - `x^0 = 1`

## _NEGATIVE EXPONENTS_
- Negative exponents --> 1/pos exponent `a^-2 = -1 / a^2 `
  - Get Reciprocal of neg exponent

## _RADICALS: FRACTIONAL EXPONENTS_
- Fractional exponents --> Radicals
  - `x^a/b` = `b(rad)[x^a]`
- Rationalize the denominator: Remove the radical in the denominator
  - Use the `conjugate method` to rationalize
    - `Conjugate`: Same terms with the opposite sign in between
      `[5 - rad(3)][5 + rad(3)]`

<!--==================-->
# Ratios and Proportions
<!--==================-->
## _RATIOS REPRESENTATIONS_
- Fractions
  - `Complex Fraction`: An expression with fraction(s) in either the numerator or denominator or both
- Decimals
- Percents

  ### Ratio Problems
  - Chemical compound
  - Conversions of ratio representations
  - Percent markup `New Price = Og Price + Markup`
  - Percent markdown `Discount Price = Og Price - Discount`
  - Commission `Commission = Sell Price * Commission Percent`
  - Simple Interest `I = Prt`
  - Total account balance

<!--==================-->
# Advanced Equations
<!--==================-->
- Equations with decimals, fractions, radicals, multivariables
- `Abstract Fractional Equation` = An equation that has at least 1 fraction with a var in its denominator

<!--==================-->
# Systems of Equations
<!--==================-->
- Systems of 3 equations
- Nonlinear equations

## _APPLICATION_
1. Uniform motion problems `Distance = Rate * Time`
2. Number word problems

<!--==================-->
# Exponents and Radicals
<!--==================-->
## _NEGATIVE BASES_
- `-3^2 = -9` vs `(-3)^2 = 9`
  - Exponents are done first
  - The `-` is applied after
  - `-a^b = -1(a^b)`
    - PEMDAS: Exponent is applied before multiplication

## _POWER TO THE POWER_
- (x^2)^3 = x^2*2*2 = x^8
- [(x^2) / (y^3)]^2
  - solve numerator and denomintor separtely

## _POWER OF 0_
- Anything to the power (including expressions) of 0 is 1
  - `x^0 = 1`

## _NEGATIVE EXPONENTS_
- Negative exponents --> 1/pos exponent `a^-2 = -1 / a^2 `
  - Get Reciprocal of neg exponent

## _RADICALS: FRACTIONAL EXPONENTS_
- Fractional exponents --> Radicals
  - `x^a/b` = `b(rad)[x^a]`
- Rationalize the denominator: Remove the radical in the denominator
  - Use the `conjugate method` to rationalize
    - `Conjugate`: Same terms with the opposite sign in between
      `[5 - rad(3)][5 + rad(3)]`
  -  Consecutive integers

<!--==================-->
# Graphing
<!--==================-->
- Parallel and perpendicular lines
- Parabola (`x^2`)
  - Vertex
- Distance between 2pts
- Midpt between 2pts

## _PARALLEL LINES_
- `b1 != b2`
- `y = mx + b1`
- `y = mx + b2`

## _PERPENDICULAR LINES_
- Slope is negative reciprocal
- `y = mx + b1`
- `y = -x/m + b2`

## _PARABOLAS_
- Vertex form `y = a(x-h)^2 + k`
  - `vertex` = (h,k) coordinates of base
  - to put into vertex/orm, you must omplete the square
- After being put on vertex form, the sign determines direction
  - Negative means parabola will point downwards
  - Positive means parabola will point upwards
- To find the y-intercept, set x to 0 and solve for y
- To find the x-intercept, set y to 0 and solve for x

## _CIRCLES_
- Standard/Center-Radius Form  `(x - h)^2 + (y - k)^2 = r^2`
  - center = (h,k)
  - radius = r
  - must complete the square to get to the center-radius form
    - for both x and y. So must complete the square 2x

## _DISTANCE OF 2 PTS_
- Given 2 pts (x1, y1) and (x1, x2)
- Just an application of the Pythagorean Thm
- `D = rad[(x2 - x1)^2 + (y2 - y1)^2]`

## _PIECEWISE FNS_
- Frankenstein graph
- Break down whole into pieces and solve/evaluate each piece

## _LINEAR LINE_
* Isolate the y in equation to go from pt-slope to slope-intercept form
- `Slope`: Steepness of the line. Slope = rise / run
  - `m = y2 - y1 / x2 - x1`
- Point-slope form `y2 - y1 = m(x2 - x1)` (x1,y1), (x2,y2)
  - Used when you have points (coordinates) and a slope (m)
- Slope-intercept form `y = mx + b`
  - Used when you have slope and an intercept (y-axis intercept)
- `Intercepts`: Points where the line crosses the major axes (x and y lines)
- `Domain`: Input values. All possible x values
- `Range`: Entire set of output values that can result from the inputs in a domain. All possible y values
- `Interval notation`: Using () or [] to show inclusivity in the range
- `Vertical Line Test`: Graph represents a fn in no perfectly vertical line crosses the graph more than once

## _Quadratic Inequalities_
1. Standard Form `ax^2 + bx + c <= 0`
2. Critical pts (Factor for x)
  - And set it to zero to solve for 0 Thm
3. Draw/Divide the number line
  - Pick test pts in each section
4. Evaluate at test pts
5. Solution

<!--==================-->
# Logarithms
<!--==================-->
- Logarithms: No subscript and it's implied that you're dealing with the default log aka `common logarithm`
- Log₁Value = Exponent
  - Base^1 = Value

## _BASIS_
- Base cannot be negative, 0 or 1

## _RULES_
- General: `5¹ = y --> log₅(y) = 1`
- Product: `log₁ab = log₁a + log₁b`
- Quotient: `log₁(⅔) = log₁2 - log₁3`
- Power: `log₁x² = 2log₁x`
- Equation: `log₁x =log₁y -- x = y`
- Change of Base: `log₁b = log₈b / log₈1`
  - 1, 8, b are vars
  - It's good to change to ln or logِ base 10 b/c calc have these btns

## _SPECIAL LOGS_
- ln = natural logs -- e^x `e = 2.78..`
- if base is missing in log, it can be assumedto be 10

## _GRAPHING_
1. Convert logarithm to an exponential fn
2. Determine asymptote `y = log₁x`  (1 = b)
  - Vertical asymptote at x = 0 when b > 0
  - Domain is all + values from 0 to Infinity
  - Range is from -Infinity to Infinity
2. Get 3+ coordinates of exponential fn by plugging in values (-1,0,1)
  - Graph using coordinates

## _TRANSFORMATIONS_
  ### Shifts
  - `log₁(base) + d`: Shifts vertically by `d` unit
  - `log₁(base +  c)`: Shifts horizontally by `c` unit

  ### Stretches/Compressions
  - Vertical: `alog₁(x)` stretched/compressed by factor of `a`
  - Horizontal: `log₁(bx)` strethed/compressed by/actor of `b`

  ### Reflections
  - Along x-axis: `-log₁(base)`
  - Along y-axis: `-log₁(-base)`

<!--==================-->
# Exponential
<!--==================-->
- `Exponential Fns`: Fns in which the vars is the exponent
- Template: `f(x) = ab^x`
  - a = Initial value: Gives you the y-intercept
  - b = Growth factor: How fast it's growing
    - b > 1 --> Increasing towards infinity
    - 0 < b < 1 --> Decaying or decreasing
- Inverse of logarithm
  - On a graph, inverses are symmetrical via y = x
  - Inverse functions have their x and y values swapped. If a function has coordinate (x,y), its inverse fn will have (y,x)
- Domain: All Values
- Range:
  - a > 0 (0, Infinity)
  - a < 0 (-Infinity, 0)

## _ASYMPTOTE_
- `Asymptote`: An asymptote is a line that a graph of a function approaches but never actually touches or intersects as the input (or output) grows larger in magnitude.
- Look at domain/range to determine the asymptote
- By default, there is a horizontal asymptote at `y = 0`

## _TRANSFORMATIONS_
- Must be done in order of
  - Horizontal 1st, Vertical 2nd

1. (H) Stretch/compression
2. (H) Shifts
3. (H) Reflection
4. (V) Stretch/compression
5. (V) Reflection
6. (V) Shift

  ### Shifts
  - Vertical: y = 2^x + d
    - Look at `d` value for vertical shift
  - Horizontal: y = 2^x+e
    - Look at `e` value for horizontal shift.
    - Move in opposite sign of e

  ### Stretches/Compressions
  - Vertical shift, each y unit of a coordinate is multiplied by `I` factor
  - Horizontal shift, each x unit of a coordinate is multiplied by `k` factor
  - VERTICAL
    - Look at initial value (`I`)
    - If |I| > 0, then stretch by the factor of I
    - If 0 < |I| < 1, then compress by a/actor of I
  - HORIZONTAL
    - Look at `k` in exponents `f(x) = b^kx`
    - If |k| > 1, compression
    - If 0 < |k| < 1, stretch

  ### Reflections
  - Negative initial value: Reflected along x axis
  - Negative exponent: Reflected along y axis

