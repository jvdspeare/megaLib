# Import megalib
import megalib

# Authenticate user token using the megalib.login_token function
auth = megalib.login_token(input('token: '), prod=True)

# Check if authentication was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('Token valid')

# Advise user if authentication failed
else:
    print('Authentication failed')
