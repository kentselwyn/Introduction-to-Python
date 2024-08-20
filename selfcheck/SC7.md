# Self Check 7

## 1. Definitions and Short Answers - exceptions  

1. If your program tries to print a variable that has not been defined, what kind of exception do you get?

> `NameError`  

2. What kind of exception do you get when you try `z = 10 / 0`?

> `ZeroDivisionError`  

3. What is the same between `ZeroDivisionError` and `OverflowError`?

> They are both under the superclass `ArithmeticError`.  

4. What kind of exception do you get when you run
```
L = "hello world"
print(L['5'])
```
?  Why?

> `TypeError` string indices must be integers.  

5. Consider the following interactive session:
```
>>> int('25')
25
>>> int('0x25')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '0x25'
```
Even though `0x25` is a valid hex literal in Python, why do you still get ValueError?  How do you correctly convert `'0x25'` into 37?  Hint: type help(int) to get documentation on different ways of using the int() function.

> Invalid base. `int('0x25', base = 16)`  

6. Which of the following expressions cause exceptions (and of what kind), assuming 
`L = "hello"`?  
- `L[4]`

> `'o'`  

- `L[0]`

> `'h'`

- `L[5]`

> `IndexError: string index out of range.`  

- `L[-2]`

> `'l'`  

- `L[-5]`

> `'h'`  

- `L[-7]`

> `IndexError: string index out of range.`  

7. Suppose `D = {'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3}`, which of the following expressions or assignment statements cause exceptions and of what kind?
- `D['Sun']`  

> `0`

- `D[2]`  

> `KeyError: 2`  

- `D['Thu']`  

> `KeyError: 'Thu'`  

- `D['Fri'] = 5`

> `None`


8. When you try to open a file by fh = open('filename', 'r') but cannot, what kind of exception do you get? 

> `FileNotFoundError: [Errno2] No such file or directory: 'filename'`  

9. When trying to open a file as in the previous question, how can your program check if an exception has occurred and inform the user by printing 
`'Cannot open file'` to the standard output and continue running the rest of the program as usual?

> ```
> try:
>	fh = open('filename', 'r')
> except:
> 	print('Oh no... ', end = '')
> print('Anyways...')
> ```

10. Suppose you are trying to execute the following sequence of statements  
```
 1  filenames = ['alpha', 'beta', 'gamma']
 2  filenum = input('select a file by typing 1, 2, or 3:')
 3  i = int(filenum)
 4  fh = open(filenames[i], 'r')
```
- On which lines can exceptions occur and what types?  

> line 3: `ValueError: invalid literal for int() with base 10.`  
> line 4: `IndexError: list index out of range.`  
> line 4: `FileNotFoundError: No such file or directory: 'beta'.`  
> line 4: `PermissionError: [Errno 13] Permission denied: 'beta'`  

- How do you rewrite the code to check and handle all types of exception the same way by printing 'An error has occurred'?  

> ```
> try:
> 	filenames = ['alpha', 'beta', 'gamma']
> 	filenum = input('select a file by typing 1, 2, or 3:')
> 	i = int(filenum)
> 	fh = open(filenames[i], 'r')
> except:
> 	print('An error has occurred')
```

- How do you rewrite the code to check each type of exception and print an error message for each specific exception?  

> ```
> try:
> 	filenames = ['alpha', 'beta', 'gamma']
> 	filenum = input('select a file by typing 1, 2, or 3:')
> 	i = int(filenum)
> 	fh = open(filenames[i], 'r')
> except ValueError as err:
> 	print('Error: %s' % str(err))
> except IndexError as err:
> 	print('Error: %s' % str(err))
> except (PermissionError, FileNotFoundError) as err:
> 	print('Error: %s' % str(err))
```

11. Given the following program 
```
 1  try:
 2      x = int(input('enter num1:'))
 3      y = int(input('enter num2:'))
 4      z = x / y
 5  except ValueError:
 6      z = 0
 7  except ZeroDivisionError:
 8      z = x
 9  print(z)
```
- If an exception occurs on line 2, what lines of code are executed next?  

> line 6 and line 9.  

- If an exception occurs on line 3, what lines of code are executed next?  

> line 6 and line 9.  

- If an exception occurs on line 4, what lines of code are executed next?  

> line 8 and line 9.  

- If line 6 is execute, is it possible that lines 7-8 are also executed immediately after?  

> No  

- If either line 6 or line 8 is executed, does line 9 also get executed next?

> Yes  


12. Given the following program
```
 1  greek = {'alpha': 0, 'beta': 1, 'gamma': 2}
 2  try:
 3      key = input('enter key alpha, beta, or gamma:')
 4      y = input('enter integer: ')
 5      z = greek[key] / int(y)
 6  except ValueError:
 7      print('invalid int')
 8  except ArithmeticError:
 9      print('arithmetic error')
10  except ZeroDivisionError:
11      print('zero division error')
12  else:
13      print('the value of z is', z)
14  finally:
15      print('last action before leaving try')
```
- Which line or lines can cause one or more exceptions, of which types, and under what conditions?  

> line 5  
> `KeyError`, when `key` is not a valid key.  
> `ZeroDivision`, when `y` is 0.  
> `ValueError`, when `y` is not an integer (of base 10).  

- In the case of zero division, is line 13 executed?  Why or why not? If not, is `ZeroDivisionError` handled and by which line(s)?

> No, it is handled in line 8~9. `ZeroDivisionError` is below `ArithmeticError` which already covers it.  

- If there is no exception by the end of line 5, which `print` statement or statements are executed next?

> lines 12~15.  

- If the user does not input `'alpha'`, `'beta'`, or `'gamma'` for the variable key on line 3, 
	- which statements are executed next?  
	> lines 14~15  

	- which statement causes an exception of which type?  
	> `z = greek[key] / int(y)` causes `KeyError`  

	- what statements are executed after the exception? 
	> `finally` suite.  
	
	- is the exception handled by any of the statements here?  
	> No
	
	- what happens to the exception after the entire code above is finished?
	> Reported to the above layer.  
	
- Suppose you want to modify the code above by handling both KeyError and ValueError exactly the same way by the same print('invalid input') statement, which lines do you modify into what code?

> Lines 6~7 are modified as below:  
> ```
> except (ValueError, KeyError):
> 	print('invalid int')
> ```

13. Failure to open a file causes an OSError, but how can you find out more information about the specific reason why the file cannot be opened?  

> `except OSError as err` will pass a string `err` that contains more information.  

14. Given the following code
```
 1  import sys
 2  try:
 3      try:
 4          fh = open('myfile')
 5          A = int(fh.read())
 6          B = int(fh.read())
 7          quotient = A / B
 8      except (OverflowError, ZeroDivisionError):
 9          quotient = 0.0
10      else:
11          quotient = 1.0
12      finally:
13          print('exiting inner try')
14      print('quotient = %f' % quotient)
15  except OSError as err:
16      sys.stderr.write(str(err))
```
If an `OSError` occurs on line 4,  do the following lines get executed?
- line 11? 
- line 13? (YES)
- line 14?
- line 16? (YES)

15. Suppose you are writing a rock, paper, scissors game as follows:
```
 1  import sys
 2  rps = input('rock, paper, scissors, or quit? [rpsq]')
 3  if rps == 'q':
 4      sys.exit(0)
 5  elif rps in 'rps':
 6      play_game(rps)
 7  else:
 8      # report error in the form of a ValueError exception
```
Rewrite the code so that 
- line 8 reports error in the form of a `ValueError` exception with an error message, 
- enclose lines 1-8 in a `try-except` construct to catch the exception, and 
- handle the exception by writing the error message to sys.stderr.

> ```
> import sys
>
> def play_game(rps):
>    print(rps)
>    
> try:
>     rps = input('rock, paper, scissors, or quit? [rpsq]')
> 
>     if rps == 'q':
>         sys.exit(0)
>     elif rps in 'rps':
>         play_game(rps)
>     else:
>         raise ValueError('Invalid input')
> 
> except ValueError as err:
>     sys.stderr.write(str(err))
> ```

16. Rewrite the code in the previous problem by using assertion instead. This means 
- replace lines 5-8 with an assert condition and the error message,
- enclose the code in a `try-except` construct but catch the assertion type of exception (what is it?) instead of `ValueError`.  Handle it by writing the error message to `sys.stderr` also.

> ```
> import sys
> 
> def play_game(rps):
>     print(rps)
>     
> try:
>     rps = input('rock, paper, scissors, or quit? [rpsq]')
> 
>     if rps == 'q':
>         sys.exit(0)
>    
>     assert (rps in 'rps'), 'Invalid input'
>     play_game(rps)
> 
> except AssertionError as err:
>    sys.stderr.write(str(err))
>```

## 2. Definitions and short answers - files

1. When opening a file using `fh = open('filename')`, why is it okay to omit the second parameter?

> The second parameter is by default `'r'`, read-only mode.  

2. What is the difference between opening a file with `'w'` mode vs `'a'` mode, as in 
`fh = open('filename', 'w')` vs. `fh = open('filename', 'a')`?  

> `'w'` mode overwrites the original file if it exists, while `'a'` mode appends the new content onto the back of the original file if it exists.  

3. Once you opened a file as file handle named `fh`, how do you   
- read one character at a time as a str

> `fh.read(1)`  

- read 10 characters as a str

> `fh.read(10)`

- read one line as a str

> `fh.readline()`  

- read all the lines as a list of str

> `fh.readlines()`  

- read the entire file as one str

> `''.join(fh.readlines())`  


4. When reading a file either one line at a time or a number of characters at a time, when do you know you have reached the end of the file?

> the returned string is `''`  

5. To open a file named 'myfile' for writing (or overwrite it completely if already exists), how should you open the file?

> `fh = open('myfile', 'w')`  

6. Once a file has been opened as file handle `fh` for writing, how should you write a string 'hello' to it?

> fh.write('hello')

7. What is the difference between `print(s)` and `sys.stdout.write(s)`?

> `print(s)` automatically attaches a '\n' at the end of s, while `sys.stdout.write(s)` does not.  

8. When you are done with a file referenced by file handle `fh`, how do you close it?

> `fh.close()`

9. Convert the following code into one that uses the with construct.  What are some advantages?
```
 1  fh = open('filename', 'r')
 2  print('totally %d lines in file' % len(fh.readlines()))
 3  fh.close()
```

> ```
> with open('filename', 'r') as fh:
> 	print('totally %d lines in file' % len(fh.readlines()))
> ```
> No need to explicitly close the file after the suite, it is automatically done.  

10. If you finish reading a file (whose handle is fh) but want to start from beginning again, what should you do without closing and reopening the file?

> `fh.seek(0)`

11. After you have opened a file whose file handle is `fh` for reading or writing for a while, how do you find the current position in the file?

> `fh.tell()`

12. What is a difference between `input('')` and `sys.stdin.readline()`?  

> `input('')` does not include `'\n'` into the resulting string, while `sys.stdin.readline()` includes `'\n'` in the resulting string.  


13. In a Unix-like shell such as bash (not Python shell), what do the following do?
```
$ grep return *.py > result
$ grep return *.py >> resfile
```

> `grep return *.py > result` **overwrites** result with the occurrences of return of any `.py` files under the current working directory.  
> `grep return *.py > result` **appends** result with the occurrences of return of any `.py` files under the current working directory.  

14. In a Unix-like shell, what is the difference between the commands
`$ wc -w filename`
and
`$ wc -w < filename`
?  

> `wc -w filename` returns the word count of `filename` with a filename to the right.  
> `wc -w < filename` reads in the content of `filename`immediately and hence does not know the filename (that it does not output)  

15. What does the following Unix shell command do?
`$ grep return *.py | wc`

> `grep return *.py` return the output of all the occurrences of keyword `return` in any `.py` file under the current working directory. Next, `|` takes this output and feed it into the input of `wc` (word count) command, which outputs the (number of lines, number of words, number of characters) to the text terminal.  

16. Why should you write to `sys.stderr` instead of `sys.stdout` to display a text-based error message, even though both appear on the same text terminal?  

> `sys.stdout` can be redirected into files or piped, while `sys.stderr` remains shown into the text terminal.  
> On the other hand, it is convenient for programmers to maintain separate channels for error messages and normal output.  

17. If you open a text file `fh`, the data object returned by `fh.read()` and the parameter `s` passed to `fh.write(s)` are of `str` type.  If you open a binary file `bh`, what is the data type of the data object returned by `bh.read()` and parameter `s` passed to `bh.write(s)`?  

> `bytes` data type  

18. How do you express the literal for a `bytes` data object consisting of ASCII characters `'h', 'e', 'l', 'l', 'o'`?   

> `bytes(''.join(x), 'ASCII')` results in `b'hello'`  

19. If you want to convert a bytes literal `b'world'` into a `str` type object, why can't you just do `str(b'world')` even though that is how you would convert other types of objects into `str`, such as `str(23)`,`str(['a', 'b', 'c'])`?   
What is the proper way?  

> Because there might different encoding schemes like ASCII characters are encoded in 1 byte, European characters are encoded in 2 bytes, Asian characters are encoded in 3 or 4 bytes, etc. Hence, the function needs to know what encoding is used to correctly translate from bytes to string.  
> On the other hand, literals like `23` and `['a', 'b', 'c']` do not have different representations. Hence, they can be immediately converted to string.  
> `str(b'world', 'ASCII')` or `str(b'world', 'UTF8)`

20. How do you convert from a str object denoted by textstring into bytes type?  

> `bytes('Hello', 'ASCII')` or `bytes('Hello', 'UTF8')`  

21. What is the meaning of the bytes literal b'\xe4\xbd\xa0\xe5\xa5\xbd'?

> `'你好'` encoded in UTF-8  
> `str(b'\xe4\xbd\xa0\xe5\xa5\xbd', 'UTF8')`  

22. In Python, what module and what function can be called to get the path to the current working directory?  How would you write a short program to print it?

> We can import `os.path` and use its `abspath` method to obtain the path to current working directory.  
> ```
> import os.path
> print(os.path.abspath('')
> ```