# Self Check 2

## 1. Definitions and Short Answers
1. What is a comment in a program and what is its purpose?
	> A **comment** is a human-readable explanation or annotation in the source code of a computer program, which is ignored by interpreter nor compiler. It serves the purpose of allowing a better method of describing or explaining the source code.
	
2. What is an operator?  Give some examples of arithmetic operators in Python.
	> An **operator** is a character that performs a specific mathematical or logical function. Example operators include `+`, `-`, `*`, `/`, `**`, `&`, `^`, `|`, `<`, `<=`, `==`, `>`, `>=`, `=`, etc. 
	
3. What is a comparison operator?  What are possible results of a comparison?
	> A **comparison operator** is an operator that compares the given values of two objects. It only returns either `True` or `False`.
	
4. What is a logical operator?  What are possible results of a logical operation?
	>  A **logical operator** is an operator that evaluates the given values of two objects logically. It only returns either `True` or `False`.
	
5. What is 20 in hexadecimal representation?  in octal representation?
	> 0x14 and 0o24, respectively

6. Why does Python support two division operators?  What is their difference?
	> Python supports `/` operator for **real division** and `//` for **integer division**.
	
7. What is the difference between `'12'` and `12` in Python?
	> `'12'` is a string literal, while `12` is an integer. 
	
8. What is the difference between `x = 3` and `x == 3` in Python?
	> 'x = 3' assigns `3` into the variable `x`, while `x == 3` compares the value stored in `x` and returns `True` if it is `3` and `False` otherwise. 
	
9. Assuming the variable y has been assigned the integer value of 4, which of the following are legal in Python and what do they do?  which are illegal in Python?
   - `y = 4` (Legal: `y` gets `4`)
   - `4 = y` (Illegal: l-value is a integer literal)
   - `y == 4` (Legal: compares the equality of `y` and `4`)
   - `4 == y` (Legal: compares the equality of `y` and `4`)
   - `'y' = y` (Illegal: l-value is a string literal)
   - `'y' == '4'` (Legal: compares the equality of `y` and `4`)
   - `'4' = y` (Illegal: l-value is a string literal)

10. Assume variable x has integer value 3, and variable y has integer value of 4.  What is the result of the following operator expressions, if they are legal in Python?  Which of the following are not legal?
    - `x * y` (Legal)
    - `'x' * y` (Legal)
    - `x * 'y'` (Legal)
    - `'x' * 'y'` (Illegal)
    - `x + y` (Legal)
    - `'x' + 'y'` (Legal)
    - `'x' + y` (Illegal)
    - `x + 'y'` (Illegal)

11. What is the data type of `['Sun','Mon','Tue','Wed','Thu','Fri','Sat']`?
	> List

12. If `L = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']`, then what are the values of the following expressions if they are legal Python?  Which are illegal?
    - `L[3]` (Legal)
    - `L[1:5]` (Legal)
    - `L[5:1]` (Legal)
    - `L(2:3)` (Illegal)
    - `L[1,2,3]` (Illegal)
    - `L{3}` (Illegal)
    - `L[1-5]` (Legal)
    - `L['3']` (Illegal)

13. Assume `T = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat')`, which of the following are allowed in Python, and what are their output or effect?  Which are not allowed, for what reasons?
    - `print(T[3])` (Legal: output `Wed`)
    - `print(T(3))` (Illegal: incorrect operator)
    - `print(T{3})` (Illegal: incorrect operator)
    - `T[3] = 'WED'` (Illegal: Tuple is immutable)
    - `T[3] == 'WED'` (Legal: ouput `False`)
    - `print(T[3:5])` (Legal: output `('Wed', 'Thu')`)
    - `print(T[3, 5])` (Illegal: accessing 2D tuple in a 1D tuple)
    - `print(T['3'])` (Illegal: incorrect operator)

14. Assume `S = {'Sun','Mon','Tue','Wed','Thu','Fri','Sat'}`, which of the following are allowed in Python, and what are its output or effect?  Which are not allowed, for what reasons?
    - `print(S[3])` (Illegal: Set is an unordered data set)
    - `print(S(3))` (Illegal: incorrect operator)
    - `print(S{3})` (Illegal: incorrect operator)
    - `S[3] = 'WED'` (Illegal: Set is an immutable data set)
    - `S[3] == 'WED'` (Illegal: Set is an unordered data set)
    - `print(S[3:5])` (Illegal: Set is an unordered data set)
    - `print(S[3, 5])` (Illegal: incorrect operator)
    - `print(S['3'])` (Illegal: Set is an unordered data set)

15. Assume `D = {'Sun':0, 'Mon':1, 'Tue':2, 'Wed':3, 'Thu':4, 'Fri':5, 'Sat':6}`, which of the following are legal in Python, and what are their values?
    - `D[3]`  (Illegal)
    - `D['Thu']` (Legal: `4`)
    - `D[0:3]` (Illegal)
    - `D[2, 6]` (Illegal)
    - `D{'Sun'}` (Illegal)
    - `D(0)` (Illegal)
    - `D{3}` (Illegal)
    - `D('Sun')` (Illegal)

16. What is the value of `{ 2, 3, 4 } | { 3, 4, 5 }` ?
	> `{2, 3, 4, 5}`

17. What is the value of `{ 2, 3, 4 } & { 3, 4, 5 }`?
	> `{3, 4}`

18. Suppose you have the following sequence of Python statements:
	```
	x = 3
	y = 2
	if x > y:
	    print("x is bigger than y")
	elif x == y:
	    print("x and y are the same")
	else:
	    print("x is smaller than y")
	```
	What is printed?
	> `x is bigger than y`
	
19. What is wrong with the following code, which is supposed to compute the total of a list of numbers?
	```
	L = [3, 2, 6, 5]
	for i in L:
	    total = total + i
	print(total)
	```
	How can it be fixed?
	
	> total is unintialized, a proper initialization before the for-loop will fix it.

20. What is the difference between
```
x = 0
while x < 100:
    x = x + 1
```
and
```
x = 0
if x < 100:
    x = x + 1
```
	> The first code is a while-loop that performs `x = x + 1` until `x` becomes `100`.  On the other hand, the second code only does `x = x + 1` once.
	

21. What is an example of a function in Python?  How do you call a function?  What is a parameter?
	> `print` is a function in Python.  
	> A function can be invoked by `function_name(parameter_1, parameter_2, ...)`.  
	> A parameter is a variable that passed into a function.  
	
22. What is an example of calling a (built-in) function that returns a value?  
	- does input() return a value?
	> `input()` returns the data input by the user in a format interpeted by Python.  
	- does print() return a value?
	> `print()` does not return a value.  
	- what other built-in functions do you know that returns a value?

23. Python supports two kinds of loops. What are they?  
	> for-loops and while-loops.

24. What is a suite?  What is the pronunciation of "suite"?
	> A suite, pronounced like 'sweet', is the sequence of instructions inside a conditional branch or loop. 

25. What does `import math` do?   How do you call the `cos` function (cosine) defined in the `math` module in Python?
	> `import math` includes all code in the `math` module in another module. We can invoke `cos` function by calling `math.cos()`

26. To read a file, it is common to see `fh = open('filename')`.   What kind of data is `fh` called?  Give an example of using `fh` for accessing (e.g., reading or writing) a file.
	> `fh` is an instance of a file handle.  
	>```
	>fh = open('filename.txt', 'r') # Read only
	>for str in fh:  
	>	print(str)
	>
	>fh.close()
	>fh = open('filename.txt', 'w') # Write only
	>fh.write('hello file')
	>fh.close()
	> ```

27. If `s = 'hello'`, Python supports two styles of “calls” (or “invocation”): 
	- `len(s)` is an example of a function call
	- `s.upper()` is another form of call.  What kind of call is it?
	> It is called 'method invocation.'
	
28. How are class and instance related to each other? 
	> An instance is an object made based on the definition of its corresponding class.
		
29. Why is it incorrect to split the statement
```
f = a + b * 2 + c / 2 - 4 * d
```
onto two separate lines as the following
```
f = a + b * 2 + c / 2
    - 4 * d
```
How can it be fixed so Python will accept it?
> ```
> f = a + b * 2 + c / 2 \
> 	- 4 * d
> ```

30. If you want to swap the values of two variables x and y, why can't you just do the below?
	```
	x = y
	y = x
	```
	> The original value of `x` becomes lost after the first instruction.
	
Give two different ways you can swap their values correctly in Python.
> `(x, y) = (y, x)`  
> or  
> ```
> temp = x
> x = y
> y = temp
> ```
	
31. What is a keyword in Python?  Give some example keywords in Python.  
> A keyword is a word with reserved meaning in Python language. `True`,`False`, `if`, `elif`, `else`, `raise`, `return`, and `yield` are examples of keywords in Python.  

32. Which of the following are legal and illegal identifiers in Python?
	- `myname` (Legal)
	- `my_name` (Legal)
	- `_myname` (Legal)
	- `MyName` (Legal)
	- `myname_` (Legal)
	- `my-name` (Illegal)
	- `my11name` (Legal)
	- `myname11` (Legal)
	- `my_11Name` (Legal)
	- `_11myName` (Legal)
	- `@myname` (Illegal)
	- `my@name` (Illegal)
	- `myname@` (Illegal)
	- `in`(Illegal)
	- `out` (Legal)
	- `_in` (Legal)
	- `_out` (Legal)
	- `IN` (Legal)
	- `OUT` (Legal)
	- `and` (Illegal)
	- `or` (Illegal)
	- `but` (Legal)
	- `function` (Legal)
	- `integer` (Legal)
	- `number` (Legal)
	- `class` (Illegal)
	- `instance` (Legal)
	- `global` (Illegal)
	- `local` (Legal)
	- `you+me` (Illegal)
	- `I_love_$$` (Illegal)  

33. What is an example of a snake-case identifier?  a camel-case identifier?
> A snake-case identifier example:  
> `prefix_sum = [0] * 1000`
> A camel-case identifier example:  
> `prefixSum = [0] * 1000`