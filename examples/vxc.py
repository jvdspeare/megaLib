# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order vxc using the megalib.vxc function
    vxc = megalib.vxc(auth.header, input('a end port uid: '), input('b end port uid: '), input('name: '),
                      input('speed: '), input('a end vlan: '), input('b end vlan'), validate=False, prod=True)

    # Advise user if vxc order was successful
    if vxc.status_code == 200:
        print('vxc ordered successfully')

    # Advise user if vxc order failed
    else:
        print('vxc order failed')

# Advise user if login failed
else:
    print('login failed')
