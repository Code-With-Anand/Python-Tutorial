import string
import secrets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
length = 10
password = secrets.token_urlsafe(length)
print(f'Password = {password}')