# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Order port using the megalib.port function
    port = megalib.port(auth.header, input('Location ID: '), input('Port Name: '), input('Speed (1000 or 10000): '),
                        prod=False)

    # Advise user if port order was successful
    if port.status_code == 200:
        print('Port Ordered Successfully')

    # Advise user if order failed, print the status code & JSON
    else:
        print('Port Order Failed, Status Code: ' + str(port.status_code) + ', JSON: ' + str(port.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))

