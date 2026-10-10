
def password_checker(password):
    Special_char = ['&','$','@','#','!']
    has_Digit = False
    has_Upper = False
    has_Lower = False
    has_special = False
    for i in password:
        if i in Special_char:
            has_special = True
        if i.isupper():
            has_Upper = True
        if i.islower():
            has_Lower = True
        if i.isdigit():
            has_Digit = True
    
    score = 0 
    if len(password) > 8:
        score += 1
    if has_Digit:
        score += 1
    if has_Lower:
        score += 1
    if has_Upper:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        result = 'Weak'
    elif score <= 4:
        result = 'Medium'
    else:
        result = 'Strong'
    
    missing = []
    if len(password) < 8:
        missing.append('Your password is underlimit !')
    if not has_Digit:
        missing.append('Digit is missing !')
    if not has_Lower:
        missing.append('Lower is missing !')
    if not has_Upper:
        missing.append('Upper is missing !')
    if not has_special:
        missing.append('Special character is missing !')
    
    return result , missing 

user = input("Enter your password : ")
result , missing = password_checker(user)
print(result)
for m in missing:
    print(m)