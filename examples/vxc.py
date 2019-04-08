# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Order VXC using the megalib.vxc function
    vxc = megalib.vxc(auth.header, input('Port UID: '), input('Target Port UID: '), input('VXC Name: '),
                      input('Speed (Rate Limit): '), prod=False)

    # Advise user if VXC order was successful
    if vxc.status_code == 200:
        print('VXC Ordered Successfully')

    # Advise user if order failed, print the status code & JSON
    else:
        print('VXC Order Failed, Status Code: ' + str(vxc.status_code) + ', JSON: ' + str(vxc.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
