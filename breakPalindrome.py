"""
*Input:
    - Non Empty
    - Palindrome String
*Output:
    - Non-Palindrome String
    - The lexicographcally Smallest One

* Explanation: Given a palindrome string - say, string = 'abcddeddcba' - the
               the lexicographically smallest, non-palindrome version of string
               would be 'aacddeddcba'.
"""


VEREDICT = 'IMPOSSIBLE'

def palindrome(string):
    return string == string[::-1]

def breakPalindrome(palindromeStr):
    is_palindrome = palindrome(palindromeStr)
    if len(palindromeStr) < 1 or len(palindromeStr) > 1000 or is_palindrome == False:
        return VEREDICT

    palindromeStr = palindromeStr.lower()

    final_string = ''
    replaced = False

    for j, c in enumerate(palindromeStr):
        if not replaced:
            if len(palindromeStr) == 1:
                final_string += 'a'
            elif c > 'a' and (len(palindromeStr)/2 != j or (len(palindromeStr) % 2) == 0):
                final_string += 'a'
                replaced = True
            else:
                final_string += c
        else:
            final_string += c

    is_palindrome = palindrome(final_string)
    if final_string == palindromeStr or len(final_string) == 1 or is_palindrome == True:
        return VEREDICT

    return final_string

def main():
    """
    >>> palindromeStr = 'abccba'
    >>> result = breakPalindrome(palindromeStr)
    >>> result
    'aaccba'
    >>> palindrome = 'abcde' #not a palindrome
    >>> result = breakPalindrome(palindrome)
    >>> result
    'IMPOSSIBLE'
    """

if __name__ == '__main__':
    import doctest
    
    doctest.testmod()