# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Create a service keys for a particular port using the megalib.service_key
    key = megalib.service_key(auth.header, input('Service UID: '), input('Description: '), prod=False)

    # Advise user if call successful
    if key.status_code == 200:
        print('key Created Successfully')

    # Advise user if failed to create key, print the status code & JSON
    else:
        print('Failed To Create Key, Status Code: ' + str(key.status_code) + ', JSON: ' + str(key.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
