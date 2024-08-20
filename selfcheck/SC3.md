# Self Check 3

## 1. Definitions and Short Answers

1. When you call the function `ord('A')` it returns 65. What does it mean?
> The ASCII code for the character `'A'` is 65.

2. What is the value of chr(70)?  (based on the knowledge of the previous question)  
> `'E'`

3. What is the difference between ASCII character set and Unicode?  If a character is in ASCII, is it also in Unicode?  Are there characters in Unicode that are not in ASCII?
> Inside the ASCII character set is 128 characters (printable and unprintable) comprising of control characters, common symbols, as well as both uppercase and lowercase characters.  
	
4. How is newline (also known as a line feed) represented as a string literal?  In other words, how do you print a newline?
> '\n'  
>`print('\n')`

5. What is a carriage return? What is its string literal, and what effect does it have when printed?
> A **carriage return** is a control character that resets the position of the cursor to the beginning of the line.  
	
6. From the command line, what keys do you type to kill a running Python program?
> `Ctrl-C`

7. Give an example of a string literal for McDonald's 
> `'McDonald\'s'`
	
8. Give an example of an integer literal
> `12345`

9. Give an example of a floating point literal
> `123.45`

10. What is the difference between print(hello) and print("hello")?
> `print(hello)` prints the **content of a variable** called `hello`, while `print("hello") prints the **string literal** `"hello"`  
	
11. What is a numeral?  What is the difference between a numeral and a number?  
> A numeral is a notation for a number, while a number represents the quantity.  
	
12. What is the value of the integer literal 0b101?  Express your answer in base-10 or in English.
> `5`  
	
13. What is the octal literal for the integer value 10?
> `0o12`  
	
14. What is the value of the integer literal 0x12?  Express your answer in base-10 or in English.
> `18`
	
15. What is the return value of
- `int('20')`
> `20`
- `int('0x20')` 
> `ERROR`
- oct(16)
> `0o20`
- bin(16)
> `0b10000`

16. What is the value of
- `0b0101 & 0b1100`
> `0b0100` or `4`
- 0b0101 | 0b1100
> `0b1101` or `13`
- 0b0101 ^ 0b1100
> `0b1001` or `9`
- ~0b0011
> `0b1100` or `12`
- 0b1011 << 2
> `0b101100` or `44`
- 0b1011 >> 2
> `ob10` or `2`
	write your answers as binary literals  
	
17. What are two possible values of the bool class?
> `True` and `False`

18. What is the value of
- `True and False`
> `False`
- True or False
> `True`
- True and True
> `True`
- True or False
> `True`
- False and False
> `False`
- False or False
> `False`

19. What is the value of
- `bool(20)`
> `True`
- `bool(0)`
> `False`
- `bool(None)`
> `False`
- `bool([ ])`
> `False`
- `bool([])`
> `False`
- `bool(0.0)`
> `False`
- `bool('0')`
> `True`
- `bool('hello')`
> `True`
- `bool('zero')`
> `True`
- `bool('')`
> `False`
- `bool(' ')`
> `True`
- `bool("")`
> `False`
- `bool('''''')`
> `False`
- `bool("""""")`
> `False`
- bool('""')
> `True`
- bool("''")
> `True`

20. What is the value of
- `20 or False`
> `20`
- `20 and False`
> `False`
- `False and 20`
> `False`
- `False or 20`
> `20`
- `[ ] or 20`
> `20`
- `[ ] and 20`
> `[]`
- `20 or [ ]`
> `20`
- `20 and [ ]`
> `[]`
- `30 or 20`
> `30`
- `20 or 30`
> `20`

21. Assume x = 3 and y = 2, what is the value of
- `x == 3 and y > 2`
> `False`
- `x <= 3 and y >= 2`
> `True`
- `x != 3 or y >= 2`
> `True`
- `x != 3 and y == 2`
> `False`
- `x >= 3 >= y > 2`
> `False`
- `x >= 3 > y >= 2`
> `True`
- not (x != 3) and not (y < 2)
> `True`

22. What is the value of
- `"hello" > "Hello"`
> `True`
- `'hello' > 'world'`
> `False`
- `'hello' == 'HELLO'`
> `False`
- `'hello' == 'he11o'`
> `False`
- `'2000' == '2OOO'`
> `False`
- `'Abacus' < 'abacus'`
> `True`
- `'about' < 'abnormal'`
> `False`
- `'I' == '|'`
> `False`
- `'ZOO' != '200'`
> `True`
- `'uber' == 'über'`
> `False`
- `'naive' == 'naïve'`
> `False`
- `'Dijkstra' == 'Dĳkstra'`
> `False`

23. What is the meaning of lexicographical order?
> The ordering that follows the general dictionary order but with the ASCII code of each character instead.

24. What is the data type of 2+3j?  What is the meaning of 3j?
> 	`complex` data type