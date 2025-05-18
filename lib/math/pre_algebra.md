<!--==================-->
# Number Sets
<!--==================-->
- There are `real` & `imaginary` numbers
- Imaginary numbers are used for specific use cases & can be ignored

## _IMAGINARY_
- Numbers that don't exist in real world
- Getting sqrt of a negative radicand

## _REAL_
  ### Irrational
  - Numbers that can't be fractions
  ```md ........................
  π,sqrt(2)
  ``````````````````````````````

  ### Rational
  Integers
    - Whole Numbers (0,1,2,3...)
    - Natural, Counting Numbers (1,2,3,4)

## _OTHER NUMBERS_
- `Digit`: A single symbol used to represent numbers. 99% of the time, it refers to integers
- `Negative`: aka signed numbers. Numbers less than 0.
- `Opposite`: A number that is opposite is the same distance away from 0
  - Ex: -4 and 4 are opposites. Both 4 units away from 0
  - Ex: 0 and 0 are opposites. Both 0 unit away from 0
- `Identity`: A number that doesn't change the value of the original value
  - Addition & Subtraction : 0
  - Multiplication & Division : 1
- `Prime`: Natural number > 1 whose only whole number factors are 1 and the number itself
- `Composite`: Has 3 or more factors. A number that's not prime

## _MORE TERMS_
- `Expressions`
- `Factorization`: Coming up with a collection of whole numbers that multiply together to give us the original number
  - Usually listed from smallest to largest with exponents for repeat factors
  - `Product of Primes`: Factorization where each factor is reduced to a prime
    - Also called `complete factorization` because each factor cannot be factorized any further

- When multiplying, each number/expression that gets multiplied is called a `factor`
- When adding, each number/expression that gets added is called a `term`

```math ..................
45 = 5 * 9
3^2 * 5

``````````````````````````

<!--==================-->
# Set Notation
<!--==================-->
∈ = Element of, *belongs to* or *in*
∪ = Union
∩ = Intersection

<!--==================-->
# Rules of Signed Numbers
<!--==================-->
## _ADDITION_
- + & + = +
- - & - = -
- + & - = the sign of the larger abs value

## _PRODUCT/DIVISION_
- same signs = +
- diff signs = -

```lua ........................
-- ADDITION
 1  +  2 =  3 -- Positive
-1  + -2 = -3 -- Negative
-1  +  2 =  1 -- Positive

-- PRODUCT/DIVISION
 1  *  2 =  2
-1  * -2 =  2
-1  *  2 = -2 -- Neg

 4  /  2 =  2
-4  / -2 =  2
-4  /  2 = -2 -- Neg
```````````````````````````````

<!--==================-->
# Multiples & Divisibility
<!--==================-->
- `Multiple`: Result of multiplying a number by an integer. Multiples of 3 is 3,6,9,12..
- `Common Multiple`: Given 2 numbers (a, b). The multiples that are in union or common
- `Least Common Multiple (LCM)`: The smallest common multiple
  - When numbers are larger, prime factorizations can be used to find LCM
    - Get prime factorizations of each number and get the largest unique factor of each number and that will get you the LCM
- `Greatest Common Factor (GCF)`: Found by getting the complete factorization of numbers and getting the union of the common factors.

```lua ..........................
10 48
Factorization:
  - 2 * 5
  - 6 * 8
     2^4 * 3

LCM = 2^4 * 3 * 5 = 240
`````````````````````````````````

```md .........................
- 3 multiple: 3,6,9,12,15,18,21,24,27,30
- 5 multiple: 5,10,15
- Common multiples: {15,30,45...}
- LCM: {15}
`````````````````````````````````

## _DIVISIBILITY RULES_
- 2: last digit is even {0 2 4 6 8}
- 3: sum of digits is divisible by 3
- 4: last 2 digits are divible by 4
- 5: last digit is 0,5
- 6: divisible by both 2 & 3
- 7: 5x last digit + rest of number is divisible by 7
- 8: last 3 digits are divisible by 8
- 9: sum of digits is divisible by 9
- 10: last digit is 0

<!--==================-->
# Place Values
<!--==================-->
- Count the periods to the left and right of decimal point and add them up
- Each triplet of significant digits is called a `period`
  - A trillion/trillionths has 4 periods
  - A billion/billionths has 3 periods
  - A million/millionths has 2 periods
  - A thousand/thousandths, hundred/hundredths has 1 period

## _INTEGERS_
  ### Trillions
  - 1   =   1,000,000,000,000
  - 10  =  10,000,000,000,000
  - 100 = 100,000,000,000,000

  ### Billions
  - 1   =   1,000,000,000
  - 10  =  10,000,000,000
  - 100 = 100,000,000,000

  ### Millions
  - 1   =   1,000,000
  - 10  =  10,000,000
  - 100 = 100,000,000

  ### Thousands
  - 1   =   1,000
  - 10  =  10,000
  - 100 = 100,000

  ### Primary
- 1 = Ones
- 10 = Tens
- 100 = Hundreds

## _DECIMALS_
- Always count the Leading 0 to the left of the decimal pt

  ### Primary
  - 0.1  = Tenths
  - 0.01 = Hundreths

  ### Thousandths
  - 0.001   = Thousandths
  - 0.0001  = 10-thousandths
  - 0.00001 = 100-thousandths

  ### Millionths
  - 0.000001   = Millionths
  - 0.0000001  = 10-millionths
  - 0.00000001 = 100-millionths

  ### Billionths
  - 0.000000001   = Billionths
  - 0.0000000001  = 10-billionths
  - 0.00000000001 = 100-billionths

  ### Trillionths
  - 0.000000000001   = Trillionths
  - 0.0000000000001  = 10-trillionths
  - 0.00000000000001 = 100-trillionths

<!--==================-->
# Conversions
<!--==================-->
## _US MEASUREMENTS_
- 1 foot = 12 inches
- 1 yard = 03 feet
- 1 lb   = 16 ounces
- 1 mile = 5280 feet
- 1 ton  = 2000 lbs

## _METRIC_
- use prefixes w/ starting point being the meter
- 1 meter = 3.28 feet

  ### Greater
  - deka  : 10
  - hecto : 100
  - kilo  : 1_000
  - mega  : 10_000
  - giga  : 100_000

  ### Less
  - deci  : 0.1
  - centi : 0.01
  - milli : 0.001

<!--==================-->
# Ratios/Proportions
<!--==================-->
- `Ratio`: describes relationship between 2 numbers
- `Proportion`: statement that 2 ratios are equal

<!--==================-->
# Exponents
<!--==================-->
## _RULES_
- `Product Rule` : x^a * x^b = x^a+b
- `Quotient Rule`: x^a / x^b = x^a-b
- `Power Rule`   : (x^a)^b = x^ab
- `Reciprocation`: x^-n = 1/x^n

<!--==================-->
# Fractions
<!--==================-->
- Ratios of 2 numbers
- Anatomy: Numerators (top), Denominators (bottom)
- `Reciprocal`: aka Multiplicative Inverse. For any nonzero real number a, the reciprocal is 1/a. Product of anynumber and its reciprocal is 1
  - 0 does not have a reciprocal b/c any number divided by 0 is undefined
  - a number multiplied by its reciprocal is 1
- Addition: Can add numerators when denominators are the same
- Mixed Numbers vs improper fractions
  - 1 1/2 == 3/2

## _SIGNS_
- A fraction has 3 signs
- You can change any 2 signs of a fraction without changing the fraction's identity

## _DENOM-NUMERATOR RULE_
- Multipying numerator and denominator of a fraction by 1 won't change the value of the fraction

```lua ....................
a/b = ac / bc
c/c = 1
```````````````````````````
<!--==================-->
# Radicals
<!--==================-->
- When rationalizing, you do not want a sq root in the denominator
  - "rationalizing the denominator"
- Radicals can be written as a number to a fraction exponent
- Opposite operations of an exponent
- `Principal Root`: Positive root. You can assume that the root value won't be negative
- √ = `radical`
- num = `radicand`
- `idx` = the degree of radical
  - square, cube, fourth, fifth.. root
- √16
  - 2 is index
  - 16 is radicand
  - √ is radical

## _PRODUCT RULE_
if m and n are nonnegative real numbers then:
  - √m√n = √mn and √mn = √m√n
if m and n are both negative real numbers
  - √m√n = -√mn

## _QUOTIENT RULE_
- √a / √b = √(a / b)

<!--==================-->
# Scientific Notation
<!--==================-->
- The power refers to the number of 0s
- Powers of 10
  - 10^1 = 10
  - 10^4 = 10000
