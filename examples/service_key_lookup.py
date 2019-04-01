# Import megalib
from megaLib import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # lookup service keys for a particular port using the megalib.service_key_function
    key = megalib.service_key_lookup(auth.header, input('port uid: '), prod=True)

    # Print response if call successful
    if key.status_code == 200:
        print(key.json)

    # Advise user if lookup failed
    else:
        print('service key lookup failed')

# Advise user if login failed
else:
    print('login failed')
