# Import megalib
from megaLib import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve partner ports using the megalib.partner function
    pports = megalib.partner(auth.header, prod=True)

    # Check if the partner ports call was successful by observing the HTTP Status Code
    if pports.status_code == 200:
        # Print the body of the response
        print(pports.json)

    # Advise user if the partner ports call failed
    else:
        print('failed')

# Advise user if login failed
else:
    print('login failed')
