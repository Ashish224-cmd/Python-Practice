def is_palindrome(s):
    reversed_s = ""
    length = 0 
    for ch in s:
        length += 1
        
    print(length)
    
    i = length-1
    print(i)
    while i>=0:
        reversed_s += s[i] 
        i -= 1
    print(s)
    print(reversed_s)
    return s == reversed_s 

s = "level"
print(f"{is_palindrome(s)} is palindrome")
        