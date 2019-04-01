# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    g_key = input('google key: ')

    # lookup google key using the megalib.google_lookup
    key = megalib.google_lookup(auth.header, g_key, prod=True)

    # order VXC
    vxc = megalib.google(auth.header, input('port uid: '), key.uid, 'megaLib google demo', key.bandwidths[0], g_key)

    # Print response if call successful
    if vxc.status_code == 200:
        print('Great Success!')

    # Advise user if failed
    else:
        print('failed')

# Advise user if login failed
else:
    print('login failed')
