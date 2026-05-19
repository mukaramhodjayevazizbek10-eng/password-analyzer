
password = input("Enter password: ")

has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in "!@#$%^&*" for c in password)
is_long = len(password) >= 8
score = sum([has_upper, has_digit, has_symbol, is_long])
if score == 4:
    print("Strong password!")
elif score == 3:
    print("Medium password")
elif score <= 2:
    print("Weak password!")
if not has_upper:
    print("— Add uppercase letters")
if not has_digit:
    print("— Add numbers")
if not has_symbol:
    print("— Add symbols (!@#$...)")
if not is_long:
    print("— Make it at least 8 characters")
