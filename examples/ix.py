# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave blank if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order is using the megalib.ix function
    ix = megalib.ix(auth.header, input('uid: '), input('service name: '), input('ix name: '),
                    input('asn: '), input('mac address: '), input('speed: '), input('vlan: '),
                    validate=False, prod=False)

    # Advise user if ix order was successful
    if ix.status_code == 200:
        print('ix ordered successfully')

    # Advise user if ix order failed
    else:
        print('ix order failed')

# Advise user if login failed
else:
    print('login failed')
