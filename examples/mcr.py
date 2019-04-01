# Import megalib
from megaLib import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order mcr using the megalib.mcr function
    mcr = megalib.mcr(auth.header, input('location id: '), input('service name: '), input('speed: '),
                      input('market: '), input('asn: '), input('contract term: '), validate=False, prod=False)

    # Advise user if mcr order was successful
    if mcr.status_code == 200:
        print('mcr ordered successfully')

    # Advise user if mcr order failed
    else:
        print('mcr order failed')

# Advise user if login failed
else:
    print('login failed')
