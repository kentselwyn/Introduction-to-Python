# Self Check 4

## 1. Definitions and Short Answers  

1. Given the command shown on the lecture slide
    ```
    $ uniq mary.txt
    ```
    What is
    - the prompt?  
    > `$`  
    - the program name?
    > `uniq`  
    - the command-line argument?  
    > `mary.txt`  

2. What does the uniq program do?  

> `uniq` outputs the given file without repeated lines.  

3. What does the cat program do?  

> `cat {file 1} {file 2} {file 3}` outputs the concatenation of the given file sequences.  

4. What does the grep program do?  

> `grep {pattern} {file}` outputs the lines in the given file that contains the given pattern.  

5. Is it possible that uniq and cat produce the same output? How?  

> Yes, when the given file contains no repeated line, the `uniq` and `cat` function calls output the same results.  

6. Given the command shown on the lecture slide
```
$ grep class myfile.py
```

    What is the purpose of:  
    - `class`  
    - `myfile.py`  

> `class` is a pattern string  
> `myfile.py` is the target file  

7. Given the command
```
$ cat *.py
```
What is the meaning of `*.py`?  

> `*.py` means any file that ends with `.py`

8. What does the following command do?
`$ python3 prog.py`  

> It runs `prog.py` using the Python interpreter.  

9. What is a shbang in a Python program? Where is it placed inside a Python program?  

> A **shebang** defines the type and path of the program that should execute the script. It is usually placed in the first line of a Python program.  

10. What does the command do:
`$ chmod +x prog.py`
> This allows `prog.py` to be executed immediately by turning on its 'executable' permission.  

11. What is the value of 
```
len([3, 7, 2, 0, 8])
len(['hello', 'world', 'goodbye'])
len('admin')
```
> ```
> 5  
> 3
> 5
> ```  

12. Suppose you run the command
```
$ python3 showargs.py  hello  world  goodbye
```
Inside the showargs.py program, suppose you have
```
import sys
```
- What is the value of sys.argv?  

> `['showargs.py', 'hello', 'world', 'goodbye']`  

- What is the value of len(sys.argv)?  

> `4`  

- What is the value of sys.argv[1:]?

> `['hello', 'world', 'goodbye']`  

13. If the command `$ python3 showargs.py hello world` is used to run the Python program, what is printed by the statement?
```
import sys
sys.stderr.write('cannot open input file %s\n' % sys.argv[1])
```
> `Cannot open input file hello`

14. If the file mary.txt contains the following lines
```
Mary had a little lamb
little lamb, little lamb
Mary had a little lamb
its fleece was white as snow
```
	what is the value of L after executing the following statements?
```
fh = open('mary.txt', 'r')
L = fh.readlines()
fh.close()
```
> ['Mary had a little lamb\n', 'little lamb, little lamb\n', 'Mary had a little lamb\n', 'its fleece was white as snow\n']  

15. What is the purpose of `end=''` in the statement?
```
print(line, end='')
```

> `end` is a character to be added at every end of every printed line.  

16. Explain why
```
'hello'.find('e')
```
results in the integer value of 1, while 
```
'hello'.find('a')
```
results in -1.

17. Rewrite the string literal `"hello, I'm John."` using
- single quotes  

> `'hello, I\'m John`  
- triple single quotes
> ```
>'''hello, I'm John.'''
> ```
	
- triple double quotes
 
> `"""hello, I'm John."""`
instead of double quotes.

18. Rewrite the string literal 'she says, "This is great!" and left' using
- double quotes
> `"'she says, \"This is great!\" and left'"`
- triple single quotes
> `'''\'she says, "This is great!" and left\''''`
- triple double quotes
> `"""'she says, "This is great!" and left'"""`
instead of single quotes.

19. Rewrite the string literal '\\n means newline' using a raw string.

> r'\\n means newline'

20. After executing the statement
```
t = 'hello' "world"
```
	What is the value of t?

> `'helloworld'`

21. What is the value of
```
len("hello")
len("I\tam\there")
len('McDonald\'s')
```
> `5`  
> `9`  
> `10`  

22. Rewrite the following triple-quoted string literal using a non-triple-quoted string literal
```
sourceCode = '''<html>
<body>Welcome</body>
<html>'''
```
- on one single line  

> `"sourceCode = '''<html>\n<body>Welcome</body>\n<html>'''"`

- on three separate lines  

> ```
> """sourceCode = '''<html>
> <body>Welcome</body>
> <html>'''"""
> ```

23. Assume  
```
month = 7
day = 4
year = 2019
```
	How do you format the date using % formatting so that it appears as strings (expressed as string literals)?  
- '7/4/2019'  

> "'%d/%d/%d'" % (month, day, year)
- '07/04/2019'  

> "'%02d/%02d/%04d'" % (month, day, year)

24. What is the value of
- '%9.2f' % 13.5  

> 
- '%9.2f' % 123456789.0193  

> 
25. What is the meaning of 5e2?  What is its data type?  

> `5e2` is equivalent to `500`. It is of `float` data type.  

26. What is the value of 5e-2?   

> `5e-2` is equivalent to `0.05`. It is of `float` data type.  

27. What is the value of '%c' % 100, given that ord('a') has the value of 97?

> `'d'`

28. What is the format string S such that S.format(month, day, year) is equivalent to the traditional formatting of `'%d/%d/%d' % (month, day, year)` ?  

> `S = '{}/{}/{}'` or `S = '{0}/{1}/{2}'`

29. What is the value of the expression?  
```
'one {0}, two {0}s, three {0}s'.format('apple')
```

> `'one apple, two apples, three apples'`  

30. What is the format string S such that `S.format(12)` evaluates to the string
`'12 decimal is 0c hex and 14 octal'`?

> `S = '{0} decimal is {0:02x} hex and {0:02o} octal'`

31. What is the value of the expression?  
`'lastname {1}, firstname {0}'.format('John', 'Smith')`

> `'lastname Smith, firstname John'`

32. Rewrite the following expressions as f-string:
- `'%d/%d/%d' % (month, day, year)`  
> `f'{month}/{day}/{year}'`
'{:02d}/{:02d}/{:04d}'.format(month, day, year)
> `f'{month:02d}/{day:02d}/{year:04d}'`

33. What is the value of the expression
- `'www.nthu.edu.tw'.split('.')`
> `['www', 'nthu', 'edu', 'tw']  `
- 'Mary had a\nlittle lamb'.split()
> `['Mary', 'had', 'a', 'little', 'lamb']  
`
34. Suppose you type the unix command wc (lightblue) and get the output (lightgreen) as shown below:
```
$ wc mult.py
       9      32     249  mult.py
```
	What are the meanings of 9, 32, and 249?  

> 9 newlines, 32 words, and 249 characters (or bytes).  

35. What is the value of the expression
- `'(' + ')('.join(['a', 'b', 'c', 'd']) + ')'`
> `'(a)(b)(c)(d)'`  
- `''.join('Mary had a little lamb'.split())'`
> `'Maryhadalittlelamb'`

36. Assume you have 
`import string`
What is the value of
- `string.punctuation`
> `'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'`
- `string.digits`  
> `'0123456789'`
- `string.ascii_lowercase`
> `abcdefghijklmnopqrstuvwxyz'`  
- `string.whitespace`
> `' \t\n\r\x0b\x0c'`
- `string.printable` 
> `'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'`

## 2. Programming Exercises
1. Write a program that prompts the user to input two strings and reports the two strings' lengths, by reporting the shorter string first. But if they are of the same length then keep them in the original order.  For example, (blue text = typed input, green highlight = program printout)
```
$ python3 compstr.py
Enter a string: Great
Enter another string: job
Shorter string: job (length 3)
Longer string: Great (length 5)
$ python3 compstr.py
Enter a string: Mary
Enter another string: lamb
First string: Mary (length 4)
Second string: lamb (length 4)
$ 
```
Note that in case the strings are of different lengths, the program says Shorter and Longer, but in case the strings are of equal length, the program says First and Second.  You don't actually print in color… the letters are colored for illustration purpose only.

2. Write a Python program named catn.py by modifying the template code to implement the unix utility command cat with -n option, which adds the line number in front of every line of a file.
- First version: support the command with optional -n flag and one file.  Note that the line number is formatted 
```
$ python3 catn.py mary.txt
Mary had a little lamb
little lamb, little lamb
Mary had a little lamb
its fleece was white as snow
$ python3 catn.py -n mary.txt
     1  Mary had a little lamb
     2  little lamb, little lamb
     3  Mary had a little lamb
     4  its fleece was white as snow
$ 
```

- Second version: handles one or more files with optional -n flag.  In case of multiple files, the line number restarts from 1.
