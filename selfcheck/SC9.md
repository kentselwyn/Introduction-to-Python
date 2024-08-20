# Self Check 9

## 1. Definitions and Short Answers - functions

1. What is the equivalent lambda expression that computes the same as the following named function?
- Function a:
```python
def Double(n):
    return n + n
```

> ```python
> lambda n: (n + n)
> ```


- Function b:
```python
def Bigger(a, b):
    return a if a > b else b
```

> ```python
> lambda a, b: a if a > b else b
> ```

2. What lambda expression can you pass to a list's sort method's optional key plug-in function if you want to sort a list of strings by string length?  For example  

```python
>>> L = ['an', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away']
>>> L.sort(key=lambda ___ )
>>> L
['a', 'an', 'day', 'the', 'away', 'apple', 'keeps', 'doctor']
```
which orders the strings from shortest to the longest.  Fill in the yellow blank above.

> ```python
>  L.sort(key = lambda s: len(s))
> ```


3. If you want to sort a list of strings primarily by length and secondarily alphabetically (case-sensitive), what lambda would you pass to the key parameter of the list's sort method?  Fill in the yellow blank below.
```python
>>> L = ['a', 'glass', 'of', 'water', 'is', 'empty', 'or', 'full']
>>> L.sort(key=lambda ___ )
>>> L
['a', 'is', 'of', 'or', 'full', 'empty', 'glass', 'water']
```

> ```python
> L.sort(key = lambda s: (len(s), s))
> ```

4. Which of the following can properly sort a list of month names by month order, and why or why not?  Assuming the following global symbols have been defined.
```python3
ML = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MD = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
L = [ 'Apr', 'May', 'Nov', 'Mar', 'Jan', 'Feb', 'Oct','Jun', 'Jul', 'Aug', 'Sep', 'Dec']
```

- `L.sort(key=ML)`

> `TypeError: 'list' object is not callable`

- `L.sort(key=MD)`

> `TypeError: 'dict' object is not callable`

- `L.sort(key=lambda x: ML[x])`

> `TypeError: list indices must be integers or slices, not str`

- `L.sort(key=lambda x: MD[x])`

> `['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']`

- `L.sort(key=lambda x: ML.index(x))`

> `['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']`

- `L.sort(key=lambda x: MD.index(x))`

> `AttributeError: 'dict' object has no attribute 'index'`

5. If `chr(97)` evaluates to `'a'`, then what is the value of
```python
list(map(chr, [97, 98, 99, 100, 101]))
```
?

> `['a', 'b', 'c', 'd', 'e']`

6. What is the value of
```python
list(map(max, [1, 7, 2, 8], [5, 6, 3, 0]))
```
?

> `[5, 7, 3, 8]`

7. How do you use the built-in function `zip` to convert lists `[1, 7, 2, 8]` and `[5, 6, 3, 0]` into a list of tuples, as in `[(1, 5), (7, 6), (2, 3), (8, 0)]`
?

> `list(zip([1, 7, 2, 8], [5, 6, 3, 0]))`

8. How to you write the equivalent list-comprehension version of 
list(map(max, [1, 7, 2, 8], [5, 6, 3, 0]))
?

> `[max([1,7,2,8][i], [5,6,3,0][i]) for i in range(0, 4)]`

9. Suppose you want to do

```python
list(map(lambda x, y: x+y, [1, 7, 2, 8], [5, 6, 3, 0]))
```

but replace the lambda expression (underlined above) with an existing function that does the same.  What can you use instead?
(Hint: import from the operator module)

> ```python3
> import operator
> 
> list(map(operator.add, [1, 7, 2, 8], [5, 6, 3, 0]))
> ```

10. If you want to read and print lines from a file but skip all blank lines using the following code template

```python
 1  fh = open('myfile')
 2  for line in filter(lambda ____, fh.readlines()):
 3      print(line, end='') # no need to print extra newline
 4  fh.close()
```

What should you put as the lambda expression above?  Note that a blank line consists of a single newline character.

> ```python
> fh = open('mary.txt')
> for line in filter(lambda x: x != '\n', fh.readlines()):
>     print(line, end = '')
> fh.close()
> ```

11. In the stack interpreter example, several versions of the interpreter are given.
The if-elif version looks like this:

```python
 1  def StackInterpreter():
 2      L = []
 3      while True:
 4          line = input('command? ')
 5          words = line.split()
 6          if len(words) == 0:
 7              pass
 8          elif words[0] == 'show':
 9              print(L)
10          elif words[0] == 'push':
11              L.extend(words[1:])
19          elif words[0] == 'pop':
20              print(L.pop())
21          elif words[0] == 'quit':
22              break
23          else:
24              print('unknown command')
```

- How can lines 8-24 be replaced with a check for quit followed by using the command word (i.e., words[0]) to look up and execute the corresponding action?  That is,

```python
 8'         if words[0] == 'quit':
 9'             break
10'         D = {'show': ____,
11'          'push': ____,
12'          'pop':  ____,
13'         }
14'         f = D.get(words[0], ______)
15'         f()
```

- on line 10' (i.e., revised line 10), what should go into the blank?  Will it work if you fill in the blank on line 10' with print(L)? Why or why not?  

> No, `print(L)` will be executed during the declaration of dictionary `D`.  

- on line 11', what should go into the blank?  
- on line 12', what should go into the blank?  
- what does the `D.get(key, altval)` method do?  How would it be rewritten without calling the `.get()` method?

> If `key` is in the dictionary, return its corresponding value. Else, return `altval`

- what goes into the blank on line 14'?  

> ```python
> def StackInterpreter():
>     L = []
>     while True:
>         line = input('Command: ')
>  
>         words = line.split()
>         
>         if len(words) == 0:
>             pass
>         
>         if(words[0] == 'quit'):
>             break
>         D = {'show': lambda: print(L),\
>              'push': lambda: L.extend(words[1:]),\
>              'pop' : lambda: L.pop()}
>         f = D.get(words[0], lambda: print('Unknown command'))
>         f()
> ```   

- can lines 10'-15' be rewritten without using temporary variables `D` and `f`?  How?

> ```python
> def StackInterpreter():
>     L = []
>     while True:
>         line = input('Command: ')
>  
>         words = line.split()
>         
>         if len(words) == 0:
>             pass
>         
>         if(words[0] == 'quit'):
>             break
>         {'show': lambda: print(L),\
         'push': lambda: L.extend(words[1:]),\
         'pop' : lambda: L.pop()}.get(words[0], lambda: print('Unknown command'))()
> ```   

12. One alternative to lambda in the lookup table above is to use inner functions, 

```python
 1  def StackInterpreter():
 2      L = []
 3      def show(): # inner function
 4          print(L)
 5      def push():
 6          L.extend(words[1:])
 7      def pop():
 8          print(L.pop())
 9      def unknown():
10          print('unknown command')
11      D = {'show': show, 'push': push, 'pop':  pop }
12      while True:
13          line = input('command? ')
14          ...
```

- What are the inner functions in this code fragment?  

> `show`, `push`, `pop`, and `unknown` are inner functions.  

- Why would it be preferable to using inner functions in this case (hint: line 11)?  

> Inner functions are much more tidier as they are referenced by name and it leaves out the implementation.  

- How would the lookup code `D.get(words[0], ______)` be written differently from the lambda version?  Fill in the blank.

> `D.get(words[0], unknown)`


13. How can you add the documentation string (docstring) to the StackInterpreter() function above so that you can do help(StackInterpreter) in interactive mode and get the help text?
```
$ python3 -i stack.py
>>> help(StackInterpreter)
    This is a stack interpreter. The commands are:
    show                   -- shows stack content
    push item1 item2 item3 -- pushes item1,... as str on stack
    pop                    -- pops and displays popped data
    quit                   -- exit interpreter
END
>>>
```

> Use a triple-quoted string immediately after `def` line.  

14. Does Python Style Guide recommend using camel case or snake case for function names?  

> Python Style Guide recommends using snake case instead of camel case for function names and most variable names.  

15. What are examples of recursive data types in Python?  Are the following data types recursive?
- `int` (NO)
- `list` (YES)
- `tuple` (YES)
- `dict` (YES)
- `set` (NO)
- `float` (NO)
- `bool` (NO)


16. What is a recursive function?  

> A recursive function is a function that can directly or indirectly call itself.  

17. What is a base case in a recursive function?  Should all recursive functions have at least one base case?  Why or why not?  

> A base case is where the function returns without recursive calls. All recursive functions must have at least one base case. Otherwise, the will be infinitely many recursive calls.  

18. If you want to count the number of integers in a list that may contain either integers or list of integers and other lists (of integers and other lists…),  
- Can you use a loop such as follows?  If not, for what cases will it fail?

```python
 1  def count_ints(L):
 2      n = 0
 3      for i in L:
 4          if type(i) == int:
 5              n += 1
 6      return n
```

> No, counterexample: `count_ints([1, [2], 3])` returns `2`  

- Can you use a loop such as follows?  If not, for what cases will it fail? 

```python
 1  def count_ints(L):
 2      n = 0
 3      for i in L:
 4          if type(i) == int:
 5              n += 1
 6          elif type(i) == list:
 7              for j in i:
 8                  n += 1
 9      return n
```

> No, counterexample: `count_ints([1, [2, [3, [4], 3], 2], 1])` returns `5`


- Fill in the code below for counting recursively. You may assume types of elements are either int or list.  Note that this version of the code is slightly differently from the slide.
```python
 1  def count_ints(L):
 2      if ________:  # base case
 3           return 1
 4      else:
 5          n = 0
 6          for i in L:
 7              n += ________
 8          return n
```

> ```python
> def count_ints(L):
>     if type(L) == int:  # base case
>            return 1
>     else:
>           n = 0
>         for i in L:
>               n += count_ints(i)
>         return n
> ```

- Rewrite lines 5-8 above to eliminate the for loop and replace it with a combination of sum() and map().

> ```python
> def count_ints(L):
>     if type(L) == int:  # base case
>            return 1
>     else:
>         return sum(map(count_ints, L))
> ```

19. Recursion can also replace a loop.  Rewrite the count_int by converting the loop into a recursive call with its own base case (i.e., loop's terminating condition) and another recursive case for "the rest of the loop".
```python
 1  def rec_count(L):
 2      if type(L) == int:  # first base case
 3          return ____
 4      if __ :  # 2nd base (L is list) so, what kind of list?
 5          return ____
 6      return rec_count(____) + rec_count(____)
 7          # one recursive call for current element, and 
 8          # 2nd recursive call for "the rest of the loop"
```

> ```python
> def rec_count(L):
>     if type(L) == int:
>         return 1
>     if len(L) == 1:
>         return 1
>     return rec_count(L[0]) + rec_count(L[1:])
> ```


20. Explain what the following functions do in terms of what the parameters are (if any) and what the return value is.
- `os.getcwd()`  

> `os.getcwd()` returns a Unicode string representing the current working directory  

- `os.listdir(d)`  

> `os.listdir()` returns a list containing the names of the files and directories in the directory `d`.  

- `os.path.isdir(d)`

> `os.path.isdir(d)` returns `True` if the `d` is an existing directory, and `False` otherwise.  


21. To count files recursively, consider the following version of code
```python
 1  def count_files(p = '.'):
 2      import os
 3      if _____: # p is the name of a file, not a directory
 4          return 1
 5      dir_content = ____ # get list of names (files & dir)
 6      return sum(_______) # sum recursive count of content
```

- What does '.' mean as the default value of parameter p?

> `'.'` refers to the current directory.  

- How do you call a function from os module to check if a path p is a file rather than a directory ("folder")?  Fill in the blank on line 3.
- If p a path is a directory, how do you obtain a list of names (of files and directories) in p?  Fill in the blank on line 5.
- How do you recursively count each path of the list so that the counts can be summed?  Fill in the blank on line 6.

> ```python
> def count_files(p = '.'):
>     import os
>     
>     if not os.path.isdir(p):
>         print(p)
>         return 1
>     
>     dir_content = [p + '/' + name for name in os.listdir(p)]
>     return sum(map(count_files, dir_content))
> ```

22. In the recursive-find example,
- Calling
```python
M = [1, 2, [3, [4, 23]]]
rec_find(M, 23)
```
results in the tuple value `(2, 1, 1)`.  What does it mean?  

> `23` is `M[2][1][1]`  

- Calling
```python
rec_find(43, 43)
```
results in True.  What does it mean?

> `43` is `43`  

- What would be the result of calling
`rec_find([1, 2, 3], [1, 2, 3])`
?

> `True`

- What would be the result of calling
`rec_find([[1, 2, 3]], [1, 2, 3])`
?

> `(0,)`  

23. The source code for the recursive-find function looks like this:
```python
 1  def rec_find(L, val):
 2      if type(L) in {list, tuple}: # look inside L
 3          for i, v in enumerate(L):
 4              p = rec_find(v, val) # recursively find item
 5              if p == True: # L[i] == val, so we return (i,)
 6                  return (i,)
 7              if p != False: # L[i] recursively found val,
 8                  return (i,)+p   # prepend i to its path p
 9      return L == val    # L not seq or for-loop didn't find
```

- What is the condition of the base case in this recursive function?  

> `type(L) not in {list, tuple}` or `p` is `False`  

- Is line 9 executed only if type(L) is not in {list, tuple}?  Or can it be executed even if type(L) is either list or tuple?  If so, describe how line 9 can still be reached after executing lines 3-8?

>Yes, when `p` is `False`

- Can line 9 compare only two ints, or can it be comparing two tuples or two lists?

> It can compare two ints, two tuples, or two lists.


- Line 5 tests
```python
 5              if p == True:
but why can't it be replaced with
 5              if p:
```
?

> If `p` is a non-empty tuple, then `bool(p)` returns `True`.

- Line 7 tests
```python
 7              if p != False:
``` 
but why isn't it redundant with line 5?  Doesn't 
p != False 
imply
p == True
?

> `p` can be tuples.

24. In the code for indenting list items by their level of nesting, 
```python
 1  def indent_list(L, level=0):
 2      if L == None:
 3          return
 4      if type(L) in {list, tuple}:
 5          for child in L:
 6              indent_list(child, level+1)
 7      else:
 8          print(f'{" "*4*level}{L}')
 9  if __name__ == '__main__':
10      L = ['F1', ['F4', 'F5', ['F8']], 'F2', 'F3', \
11          'D3', ['F6', 'F7']]
12      indent_list(L)
```
- By the time 'F8' is printed in the test case, how many copies of indent_list calls are active?  What are the values of the parameters L and level?

> 3 `indent_list` calls are active.  
> `L` is `'F8'` and `level` is `3`  

- Is line 2 ever executed when running the test case?  

> No

- How many times total is indent_list(L) called in the test case above?  How can you modify the code above to print your answer?

> `13`