import re
pattern = "[a-zA-z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input = input()
if(re.search(pattern, user_input)):
    print("Valid Email")

else:
    print("invalid email")
