<!--==================-->
# Built In Fns
<!--==================-->
- Golang is similar to Python in that it has many builtin fns
- to convert to strings use the `strconv` package
- Golang uses uppercase letters to export methods

## _TYPES (standard)
- use `strconv` pkg
```go .....................
bool()
int()
float()
string()
rune()

// RARELY USED
byte()
complex() // complex #
  - imag() // imaginary #
  - real() // real part of a complex #
``````````````````````````````

## _GENERAL_
```go ......................
len()
cap()
make()
new(Type) *Type
close()

// DEBUGGING
print(args ...Type) // prints result to STERR
println(args ..Type) // prints result to STERR
panic()
recover()
````````````````````````````
## _MATH_
```go .......................
max()
min()
`````````````````````````````

## _SLICES_
```go ......................
append(slice [Type, elems ...Type]) []Type
clear()
copy(dest, src [type]) int
````````````````````````````

## _MAPS_
```py ......................
delete(m map[Type]Type1, key Type)
````````````````````````````

<!--==================-->
# Strings
<!--==================-->
- import `strings` package
- s = `strings`

```go ........................
s.Clone(s string) string
s.Count(s, substring) int
``````````````````````````````

## _SEARCH_
```go ........................
// Inclusion
s.Contains(s, substr string) bool // subst in s?

// Anchored
s.HasPrefix(s, prefix string) bool
s.HasSuffix(s, prefix string) bool

// Index
s.Index(s, substr string) int // idx or -1
s.IndexAny(s, chars string) int
  s.IndexAny("chicken", "aeiou") // 2
s.LastIndex(...)
s.LastIndexAny(...)
``````````````````````````````

## _MANIPULATION_
```go .............................
import "strings"

len(s string)

// CASING
s.ToLower(s string) string
s.ToUpper(s string) string
s.Title(s string) string
s.EqualFold(s, t string) bool
```````````````````````````````````
  ### Removal
```go ............................
s.Replace(s, old, new string, n int) string
 // returns copy of str of old replaced by new
s.ReplaceAll(s, old, new string) string
 // returns a copy of the string s with old replaced by new
``````````````````````````````````

  ### Sizing
```go ...........................
s.Repeat(s string, count int) string
s.Trim(s, cutset string) string
  s.TrimPrefix(s, prefix string) string
  s.TrimSuffix(s, suffix string) string
  s.TrimSpace(s string) string
````````````````````````````````

  ### Transform
```go ........................
s.Split(s, sep string) []string
s.Fields(s string) []string
s.Join(elems []string, sep string) string
  // returns string from slices
s.Map(mapping func(rune) rune, s string) string
  // returns copy of str s with all chars modified
````````````````````````````

## _PARTITION CUT_
```go ...........................
s.Cut(s sep string) (before, after string, found bool)
s.CutPrefix(s, prefix string) (after string, found bool)
s.CutSuffix(s, suffix string) (before string, found bool)
`````````````````````````````````

<!--==================-->
# Slices
<!--==================-->
- import `slices` package
```go .......................
sl.Collect[E any](seq iter.Seq[E]) []E
sl.Concat(...) slice
sl.Contains(slice, item) bool
👺 sl.Delete() S
sl.Equal(s1, s2 S) bool
s1.IsSorted(x S) bool
s1.Max(x S) E
s1.Min(x S) E
s1.Repeat()
s1.Replace()
👺 s1.Reverse()
👺 s1.Sort()
s1.Sorted()
````````````````````````````

<!--==================-->
# Input/Output
<!--==================-->
- import `fmt`
- There are 3 variants
  1. Plain
  2. ln = line
  3. f = formatted

```go ......................
import "fmt"

fmt.Errorf(format string, a ...any) error
fmt.Scan(f,ln)(r io.Reader, a ...any) (n int, err error)
fmt.Print(f,ln)(a ...any)(n int, err error)
fmt.Sprint(f,ln)(a ...any) string
````````````````````````````

<!--==================-->
# Maps
<!--==================-->
- import `maps`
- maps is in `golang.org/x/exp/maps`

```go .......................
maps.Clone(m M) M
maps.Copy(dst M1, src M2)
maps.Collect(K, V) map[K]V
maps.Clear((m M))
maps.Equal(m1, m2) bool
`````````````````````````````

## _ARRAYIFICATION_
```go ........................
maps.Keys(m M) []K
maps.Values(m M) []K
``````````````````````````````

<!--==================-->
# Math
<!--==================-->
- import `math` pkg
- import `math/rand`

```go ......................
import "math"

x := "float"

math.Abs(x) float
math.Sqrt(x) float
math.Max(x) float
math.Min(x) float

// ROUNDING
math.Floor(x) float
math.Ceil(x) float
math.Round(x) float

// RANDOM
rand.Intn(int) int
rand.Float64() float64
````````````````````````````

<!--==================-->
# Time
<!--==================-->
- import `time` pkg

  ## _TIME TYPE_
```go .......................
time.Now() // return curr local time
time.UTC()
time.Date(yr, month, day, hour, min, sec) Time
time.Date(year int, month Month, day int)
time.Clock() (hour, min, sec int)

time.Year() int
time.Month() Month
time.Weekday() Weekday
time.Day() int
time.Hour() int
time.Minute() int
time.Second() int
`````````````````````````````

  ## _DURATION TYPE_
- time pkg has a `Duration` type
- these are the methods

```go ......................
time.Duration.Milliseconds()
time.Duration.Seconds()
time.Duration.Minutes()
time.Duration.Hours()
````````````````````````````

<!--==================-->
# Regexp
<!--==================-->
- `regexp` pkg
- must compile a regexp into a Regexp object 1st
  - if pattern isn't valid, it returns an error
  - Regexp object is the pattern
- after compilation, you can call methods on the Regexp object

```go ....................
import "regexp"

func main() {
  re, err := regexp.Compile("[a-z]+")
  re.MatchString(str) bool
  re.FindString(str) // 1st match
  re.FindAllString(str) []string
  re.ReplaceAll(src, repl [byte]) []byte
  re.Split(s string, n int) []string
}
``````````````````````````
