def is_palindrome(string):
    string = string.replace(" ", "")
    if string == string[::-1]:
        return True
    return False


print('Checking string for "palindromable"')
string = input('Enter your string: ')
print('Your string is ', 'palindrome' if is_palindrome(string) else 'not palindrome')
