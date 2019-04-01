# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order port using the megalib.port function
    port = megalib.port(auth.header, input('location id: '), input('service name: '), input('speed: '),
                        input('market: '), input('contract term: '), validate=False, prod=False)

    # Advise user if port order was successful
    if port.status_code == 200:
        print('port ordered successfully')

    # Advise user if port order failed
    else:
        print('port order failed')

# Advise user if login failed
else:
    print('login failed')
