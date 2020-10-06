string=input()
def reverse(string):
    if len(string)==1 or len(string)==0:
        return string
    small_string=string[1:]
    output=reverse(small_string)
    return output+string[0]
def check_palindrome(string):
    rev=reverse(string)
    if rev==string:
        return True
    else:
        return False
print(check_palindrome(string))
