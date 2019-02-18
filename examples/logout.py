# Import megalib
import megalib

# logout an existing token using the megalib.logout function
auth = megalib.logout(input('token: '), prod=False)

# Check if logout was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('logout successful')

# Advise user if logout failed
else:
    print('logout failed')
