# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order port using the megalib.port function
    mcr = megalib.mcr(auth.header, input('location id: '), input('service name: '), input('speed: '),
                      input('market: '), input('asn: '), input('contract term: '), validate=False, prod=True)

    # Advise user if mcr order was successful
    if mcr.status_code == 200:
        print('port ordered successfully')

    # Advise user if mcr order failed
    else:
        print('port order failed')

# Advise user if login failed
else:
    print('login failed')
