# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Order is using the megalib.ix function
    ix = megalib.ix(auth.header, input('Port UID: '), input('IX Service Name: '), input('IX Exchange Name: '),
                    input('ASN: '), input('MAC Address: '), input('Speed (Rate Limit): '), prod=False)

    # Advise user if ix order was successful
    if ix.status_code == 200:
        print('IX Ordered Successfully')

    # Advise user if order failed, print the status code & JSON
    else:
        print('IX Order Failed, Status Code: ' + str(ix.status_code) + ', JSON: ' + str(ix.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
