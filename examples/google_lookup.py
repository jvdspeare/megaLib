# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # lookup google key using the megalib.google_lookup
    key = megalib.google_lookup(auth.header, input('google key: '), prod=False)

    # Print response if call successful
    if key.status_code == 200:
        print(key.bandwidths)
        print(key.target)
        print(key.uid)

    # Advise user if lookup failed
    else:
        print('google key lookup failed')
        print(key.json)

# Advise user if login failed
else:
    print('login failed')
