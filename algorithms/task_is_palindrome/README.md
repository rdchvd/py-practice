# Task: is_palindrome

## Description
This function checks if the input string is a palindrome.

### Example:
- **Input**: `Some sentence`
- **Output**:  `False`


- **Input**: `A man, a plan, a canal – Panama`
- **Output**: `True`

### Solution
The function uses `.replace()` to remove all non-alphanumeric characters from the input string.
It makes the string lowercase using `.lower()`.
Then it compares the input string with its reverse.
If they are equal, the function returns True, otherwise False.
