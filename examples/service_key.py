# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave blank if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Create a service keys for a particular port using the megalib.service_key
    key = megalib.service_key(auth.header, input('port uid: '), input('description: '), input('vlan: '),
                              input('single use: '), input('max speed: '), input('pre-approved: '), input('active: '),
                              input('start time: '), input('end time: '), prod=False)

    # Advise user if call successful
    if key.status_code == 200:
        print('key created successfully')

    # Advise user if call failed
    else:
        print('failed to create service key')

# Advise user if login failed
else:
    print('login failed')
