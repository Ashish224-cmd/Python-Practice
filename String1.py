# counting digits, letters, and spaces in a string.
import re 
name = "python is 1"
digit_count = re.sub("[^0-9]","",name)
letter_count = re.sub("[^a-zA-Z]","",name)
space_count = re.findall("[ \n]",name)

print(digit_count)
print(letter_count)
print(space_count)
  