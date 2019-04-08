# Import megalib
import megalib

# logout an existing token using the megalib.logout function
auth = megalib.logout(input('Token: '), prod=False)

# Check if logout was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('Logout Successful')

# Advise user if logout failed, print the status code & JSON
else:
    print('Logout Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
