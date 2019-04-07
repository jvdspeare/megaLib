# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave blank if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order VXC to Azure using the megalib.azure function
    azure = megalib.azure(auth.header, input('uid: '), input('azure target uid: '), input('name: '), input('speed: '),
                          input('azure end vlan: '), input('azure expressroute key: '), input('private peering: '),
                          input('microsoft peering: '), input('a end vlan: '), validate=False, prod=False)

    # Advise user if order was successful
    if azure.status_code == 200:
        print('azure vxc ordered successfully')

    # Advise user if order failed
    else:
        print('azure vxc order failed')

# Advise user if login failed
else:
    print('login failed')
