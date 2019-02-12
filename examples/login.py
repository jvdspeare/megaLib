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
print(auth.status_code)

# Response Body
print(auth.json)

# Header
print(auth.header)
