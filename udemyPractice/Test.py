def palindrome(mystring):
    mystring=mystring.replace(" ","")

    return mystring==mystring[::-1]

print(palindrome('nurses run'))
