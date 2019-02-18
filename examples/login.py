# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Print HTTP Status Code, Response Body & Header
    print(str(auth.status_code), '\n' + str(auth.json) + '\n' + str(auth.header))

else:
    print('login failed')
