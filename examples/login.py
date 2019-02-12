# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')
else:
    print('login failed')

# HTTP Status Code
print(l.status_code)

# Response Body
print(l.json)

# Header
print(l.header)
