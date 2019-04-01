# Import megalib
from megaLib import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order VXC to Google using the megalib.google function
    google = megalib.google(auth.header, input('uid: '), input('google target uid: '), input('name: '),
                            input('speed: '), input('google key: '), validate=False, prod=True)

    # Advise user if order was successful
    if google.status_code == 200:
        print('google vxc ordered successfully')

    # Advise user if order failed
    else:
        print('google vxc order failed')

# Advise user if login failed
else:
    print('login failed')
