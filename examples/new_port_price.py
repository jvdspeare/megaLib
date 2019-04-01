# Import megalib
from megaLib import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve new port price using the megalib.new_port_price function
    price = megalib.new_port_price(auth.header, input('location id: '), input('speed: '), input('term: '), prod=False)

    # Print monthly cost
    if price.status_code == 200:
        print(price.currency + ' ' + str(price.monthly_rate))

    # Advise user if lookup failed
    else:
        print('price lookup failed')

# Advise user if login failed
else:
    print('login failed')
