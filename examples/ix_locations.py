# Import megalib
from megaLib import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve ix locations using the megalib.ix_locations function
    loc = megalib.ix_locations(auth.header, input('location id: '), prod=True)

    # Check if the ix locations call was successful by observing the HTTP Status Code
    if loc.status_code == 200:
        # Print the body of the response
        print(loc.json)

    # Advise user if the ix locations call failed
    else:
        print('failed')

# Advise user if login failed
else:
    print('login failed')
