# Self Check 8

## 1. Definitions and Short Answers - functions

1. Given a function definition  
```
def Double(n):
    return n + n
```
and given a call to the function
```
x = Double(20)
```
What is a formal parameter?  What is the actual parameter?

> The format parameter is `n` and the actual parameter is `20`.

2. If you call the above function as
```
y = Double( Double(40 + Double(3)) - Double(7))
```
what is the value of y?

> `156`

3. What is the difference between
```
d = Double
```
and
```
z = Double(20)
```
?  

> `d` is assigned to a **function object**, while `z` is assigned to an integer `40`.  

4. If you do 
```
print, input = input, print
z = input('enter a name: ')
```
What happens, and what is the value of z?

> `'enter a name: '` is printed onto `stdout`.  

5. Given the function
```
def DivMod(a, b):
    return a // b, a % b
```
What does this function return?  

> `DivMod` returns a tuple of two integers (integer division, integer remainder).  

6. Are the following pairs equivalent (in terms of parameters received by the open() function for opening files)?
- `fh = open('myfile.txt', 'r')`  and `fh = open(file='myfile.txt', mode='r')`  

> YES

- `fh = open('myfile.txt', 'r')` and `fh = open(mode = 'r', name = 'myfile.txt')`  

> YES

- `fh = open('myfile.txt', 'r')` and
`fh = open('r', 'myfile.txt')`  

> NO

- `fh = open(file='myfile.txt', mode='r')` and
`fh = open(mode='r', file='myfile.txt')`  

> YES

7. Consider the function declaration
```
 1  def withTax(price, rate=0.05):
 2      return price * (1 + rate)
```
Can you call this function in the following ways?  If so, what is the result?  If not, why not?
- `withTax(20)`  (YES: `21.0`)  
- `withTax(rate=0.08, price=30)`(YES: `32.4`)  
- `withTax(price=20, 0.08)` (NO: Positional argument is behind a keyword argument)  
- `withTax(price=20)`(YES: `21.0`)   
- `withTax(rate=0.08)` (NO: Missing required positional argument : `'price'`)  
- `withTax()` (NO: Missing required positional argument : `'price'`)  
- `withTax(20, 0.08)` (YES: `21.6`)  


8. Suppose you are given a function
```
 1  def withMoreTax(price, rate = 0.05):
 2      ans = price * (1 + rate)
 3      rate += 0.01
 4      return ans
```

What does the following code sequence print?
- `print(withMoreTax(20))`  
- `print(withMoreTax(20))`  
In other words, does the parameter rate's default value get changed on line 3 such that the next call gets the modified default value?

> Both prints `21.0`. 

9. Are you allowed to define default values with non-constant expressions such as the following?  If so, what does it do?

- Code A:  
```
 1  import sys
 2  def withNewTax(price, rate=input('enter a rate: ')):
 3      return price * (1 + float(rate))
```

> LEGAL. When the program starts (when `withNewTax` is defined, the user will be prompted with `'enter a rate: `)  

- Code B:  
```
 1  def withNewerTax(price, rates=[0.01, 0.02, 0.03]):
 2      ans = price * (1 + rates[-1])
 3      rates.pop()
 4      return ans
```  

> LEGAL, but buggy. When `rates` were popped three times, then `rates[-1]` is an illegal expression (out of bound access).  

- Code C:  
```
 1  def withNewestTax(price, rate=price):
 2      return price * (1 + rate)
```

> ILLEGAL. A declaration of formal parameter cannot involve another formal parameter.  

10. Suppose you have a function declared as
```
def totalTax(rate, *priceTags):
    ...
```
What is the value of rate and priceTags inside the function `totalTax` when you call it as  
- `totalTax(0.05, 10, 20, 23, 18)`  

> `rate` = `0.05`  
> `priceTags` = `(10, 20, 23, 18)`  

- `totalTax(0.05, (10, 20, 23, 18))`  

> `rate` = `0.05`  
> `priceTags` = `((10, 20, 23, 18))`  

- `totalTax(0.05, *(10, 20, 23, 18))`  

> `rate` = `0.05`  
> `priceTags` = `(10, 20, 23, 18)`  

- `totalTax(*(0.05, 10, 20, 23, 18))`  

> `rate` = `0.05`  
> `priceTags` = `(10, 20, 23, 18)`  

- `totalTax(0.05)`  

> `rate` = `0.05`  
> `priceTags` = `()`  

- `totalTax(0.05, 10)`  

> `rate` = `0.05`  
> `priceTags` = `(10,)`  

11. Given the following function definition:
```
 1  def totalTax(rate, **priceDict):
 2      return sum(priceDict.values())* (1 + rate)
```
Are the following valid ways of calling the function?  If so, what are the values of parameters rate and priceDict while inside the totalTax function, and what is the corresponding return value?  If not valid, why not?
- `totalTax(0.05, apple=12, orange=8)`  

> `rate` = `0.05`  
> `priceDict` = `{'apple' : 12, 'orange' : 8}`  
> Result: `21`  

- `totalTax(0.05, 12, 8)`  

> TypeError, no parameter name were given.  

- `totalTax(0.05, 'apple'=12, 'orange'=8)`  

> SyntaxError, assigned an integer literal to a string literal.  

- `totalTax(0.05, 'apple':12, 'orange':8)`  

> SyntaxError, invalid syntax.  

- `totalTax(rate=0.05, priceDict={'apple':12, 'orange':8})`  

> `rate` = `0.05`  
> `priceDict` = `{'priceDict' : {'apple' : 12, 'orange' : 8}}`  
> Result: TypeError, cannot perform `int` and `dict` addition.  

- `totalTax(rate=0.05, **{'apple':12, 'orange':8})`  

> `rate` = `0.05`  
> `priceDict` = `{'apple' : 12, 'orange' : 8}`  
> Result: `21.0`  

- `totalTax(rate=0.05, **priceDict={'apple':12, 'orange':8})`  

> SyntaxError  

- `totalTax(rate=0.05, priceDict=(('apple', 12), ('orange', 8))`  

> `rate` = `0.05`  
> `priceDict` = `{'priceDict' : (('apple' , 12), ('orange', 8))`  
> Result: TypeError, cannot perform `int` and `tuple` addition.  

- `totalTax(rate=0.05, **priceDict=(('apple', 12), ('orange', 8))`  

> SyntaxError  

- `totalTax(apples=12, oranges=8, rates=0.05)`  

> TypeError, requires `rate` not `rates`.  


12. Given the following function definition
```
 1  def totalWithTax(rate, *items, **priceDict):
 2      d={'apple':12,'orange':8, 'mango':3}
 3      d.update(priceDict)
 4      total = 0
 5      for i in items:
 6          total += d[i]
 7      return total * (1 + rate)
```
Are the following valid ways of calling the function?  If so, what are the values of parameters `rate`, `items`, and `priceDict` while inside the `totalWithTax` function, and what is the corresponding return value?  If not valid, why not?

- Call A:
```
totalWithTax(0.05, 'apple', 'orange', 'mango') 
```

> `rate` = `0.05`  
> `items` = `('apple', 'orange', 'mango')`  
> `priceDicts` = `{}`
> Result: 23  

- Call B:
```
totalWithTax(0.05, 'apple', 'orange', 'mango', \
             'apple', 'apple') 
```

> `rate` = `0.05`  
> `items` = `('apple', 'orange', 'mango', 'apple', 'apple')`  
> `priceDicts` = `{}`  
> Result: 49.35  

- Code C:
```
totalWithTax(0.05, 'apple', 'orange', 'mango', \
             apple=3, orange=4, mango=5) 
```

> `rate` = `0.05`  
> `items` = `('apple', 'orange', 'mango')`  
> `priceDicts` = `{'apple' : 3, 'orange' : 4, 'mango' : 5}`  
> Result: 12.6  

- Code D:
```
totalWithTax(0.05, 'apple', 'orange', 'mango',\
             **{'apple':3, 'orange':4, 'mango':5}) 
```

> `rate` = `0.05`  
> `items` = `('apple', 'orange', 'mango')`  
> `priceDicts` = `{'apple':3, 'orange':4, 'mango':5}`  
> Result: 12.6  

- Code E:
```
totalWithTax(0.05, *('apple', 'orange', 'mango')) 
```

> `rate` = `0.05`  
> `items` = `('apple', 'orange', 'mango')`  
> `priceDicts` = `{}`  
> Result: 

- Code F:
```
totalWithTax(0.05)
```

> `rate` = `0.05`  
> `items` = `()`  
> `priceDicts` = `{}`  
> Result: 0

13. Suppose you have two tuples
```
A = (1, 3, 7)
B = (2, 4, 8)
```
and you want to use the built-in function max() to find the largest element in the two tuples.  Which of the following will correctly find the answer (which is 8)?  Choose all that apply and explain why or why not.
- `max(A, B)`   
- `max(*A, *B)` (YES)   
- `max(A + B)` (YES)  
- `max(*(A+B))` (YES)  
- `max(*A + *B)`  
- `max((A, B))`   
- `max(*(A, B))`   


14. Given the following code
```
 1  a = 3
 2  def F():
 3      print(a)
 4  F()
``` 
What is printed when you run this code?

> `3`  

15. Given the following code
```
 1  a = 3
 2  def F():
 3      a = 5
 4      print(a) 
 5  F()
 6  print(a)
```
What is printed when you run this code?

> `5`  
> `3`

16. Given the following code
```
 1  a = 3
 2  def F():
 3      print(a)
 4      a = 5
 5  F()
 6  print(a)
```
But it gives an `UnboundLocalError` when you try to run it.                   
- Why do you get this error?

> Because the variable `a` has already bound to the global variable `a` and by the time `a` is locally defined at line 4, it contradicts the binding.

- How do you fix it if you want the function F to use the identifier a as defined on line 1?

> Code:  
> ```
>  1  a = 3
>  2  def F():
>  3      global a
>  4      print(a)
>  5      a = 5
>  6  F()
>  7  print(a)
> ```

17. Given the source code
```
 1  D = { 'rate': 0.0 }
 2  def totalWithTax(*names, **kv):
 3      global D
 4      total = 0.0
 5      for name in names:
 6          total += D[name]
 7      for kw, val in kv.items():
 8          D[kw] = val # overwrite dict entry 
 9          if kw != 'rate':
10              total += val
11      return total * (1 + D['rate'])
```
Are the following valid ways of calling the function `totalWithTax`?  If so, what are the values of parameters `names`, and `kv` while inside the `totalWithTax` function, the values of the global variable `D`, and what is the corresponding return value?  If not valid, why not?  Assume you reload the code each time before executing the code below.
- `totalWithTax()`  

> `names` = `()`  
> `kv` = `{}`
> Result: `0.0`

- `totalWithTax('apple')`  

> `names` = `('apple',)`  
> `kv` = `{}`
> Result: `KeyError`  

- `totalWithTax(apple=20)+totalWithTax('apple')`  

> `names` = `()` then `('apple',)`  
> `kv` = `{'apple' : 20}` then `{}`
> Result: `40.0`  

- `totalWithTax('orange', orange=15)`  

> `names` = `('orange',)`  
> `kv` = `{'orange' : 15}`
> Result: `KeyError`  

- `totalWithTax(guava)`  

> `names` = `()`  
> `kv` = `{}`
> Result: `NameError`  

- `totalWithTax(rate=0.05, apple=10) + totalWithTax('apple', 'apple', 'apple')`  

> `names` = `()` then `('apple', 'apple', 'apple')`  
> `kv` = `{'rate' : 0.05, 'apple' : 10}` then `{}`  
> Result: `42.0`  

- `totalWithTax(apple=10, orange=15)+totalWithTax('apple',guava=12)`  

> `names` = `()` then ('apple',)  
> `kv` = `{'apple' : 10, 'orange': 15}` then `{'guava' : 12}`  
> Result: `47.0`

- `totalWithTax(apple=10, orange=15) + totalWithTax(rate=0.05, guava=12) + totalWithTax(rate=0.02, 'apple', 'orange', 'guava')`  

> `names` = `()` then `()` then `('apple', 'orange', 'guava')`  
> `kv` = `{'apple' : 10, 'orange' : 15}` then `{'rate' : 0.05, 'guava' : 12.0}` then `{'rate' : 0.02}`  
> Result: `SyntaxError: Positional argument follows keyword argument`  

18. How do you write test code at the end of a module to test functions defined in the module when it is run as a top-level module (hint: '__main__'), but don't run the test case when it is imported by another module?  Also, what construct should you use to check if a tested function returns the results as the correct answer?  

> ``` python3
> if __name__ == '__main__':
> 	assert function(a, b) == c
> 	assert function(d, e) == f
> ```
