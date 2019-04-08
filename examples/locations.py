# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Retrieve locations using the megalib.locations function
    loc = megalib.locations(auth.header, prod=False)

    # Check if the locations call was successful by observing the HTTP Status Code
    if loc.status_code == 200:
        # Print the body of the response
        print(loc.json)

    # Advise user if locations call failed, print the status code & JSON
    else:
        print('Locations Call Failed, Status Code: ' + str(loc.status_code) + ', JSON: ' + str(loc.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
