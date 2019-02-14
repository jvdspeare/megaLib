# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '))

# Verify that authentication was successful before attempting to retrieve locations
if auth.status_code == 200:
    print(megalib.locations(auth.header).json)

# Advise user if the user authentication was unsuccessful
else:
    print('login failed')
