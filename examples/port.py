# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '))

# Verify that authentication was successful before ordering the port
if auth.status_code == 200:

    # Order Megaport
    port = megalib.port(auth.header, input('location id: '), input('service name: '), input('speed (1000/10000): '),
                        'AU')

    # Advise user if port was ordered successfully
    if port.status_code == 200:
        print('Port ordered')

    # Advise user if port order failed
    else:
        print('Port order failed: ' + str(port.status_code))

# Advise user if the user authentication was unsuccessful
else:
    print('login failed')

