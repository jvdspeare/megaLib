# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Order MCR using the megalib.mcr function
    mcr = megalib.mcr(auth.header, input('Location ID: '), input('MCR Name: '), input('Speed (Rate Limit): '),
                      prod=False)

    # Advise user if MCR order was successful
    if mcr.status_code == 200:
        print('MCR Ordered Successfully')

    # Advise user if order failed, print the status code & JSON
    else:
        print('MCR Order Failed, Status Code: ' + str(mcr.status_code) + ', JSON: ' + str(mcr.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
