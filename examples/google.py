# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Input the Azure Expressroute Key
    google_key = input('Google Key: ')

    # Lookup the Google Key using the megalib.google_lookup function
    key = megalib.google_lookup(auth.header, google_key, prod=False)

    # Observe the HTTP Status Code and advise user if azure lookup was successful
    if key.status_code == 200:
        print('Google Key Lookup Successful, Valid Speeds: ', str(key.bandwidths))

        # Order VXC to Google using the megalib.google function
        google = megalib.google(auth.header, input('Port UID: '), key.uid, input('VXC Name: '),
                                input('Speed (Rate Limit): '), google_key, prod=False)

        # Advise user if order was successful
        if google.status_code == 200:
            print('Google VXC Ordered Successfully')

        # Advise user if order failed, print the status code & JSON
        else:
            print('Google VXC Order Failed, Status Code: ' + str(google.status_code) + ', JSON: ' + str(google.json))

    # Advise user if Google Key lookup failed, print the status code & JSON
    else:
        print('Google Key Lookup Failed, Status Code: ' + str(key.status_code) + ', JSON: ' + str(key.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
