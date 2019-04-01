# Import megalib
from megaLib import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve speed change price using the megalib.speed_change_price function
    price = megalib.lifecycle_change_price(auth.header, input('uid: '), input('action: '), input('month: '), prod=True)

    # Print json
    if price.status_code == 200:

    # Advise user if lookup failed
    else:
        print('price lookup failed')

# Advise user if login failed
else:
    print('login failed')
