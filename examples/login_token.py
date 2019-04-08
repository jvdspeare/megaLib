# Import megalib
import megalib

# Authenticate user token using the megalib.login_token function
auth = megalib.login_token(input('Token: '), prod=False)

# Check if authentication was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('Token Valid')

# Advise user if authentication failed, print the status code & JSON
else:
    print('Authentication Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
