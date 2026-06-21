password = input("Enter the password: ")



result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False

for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit


uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result['upper-case'] = uppercase


print("#########################")
print("Keys:", result['keys'])
print("Values:", result['values'])


if all(result):
    print("Strong password")
else:
    print("Weak password")




########################################################################

"a".isdigit() # false
"8".isdigit() # true
"a8".isdigit() # false