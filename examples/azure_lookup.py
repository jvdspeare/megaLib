# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # lookup azure service key using the megalib.azure_lookup
    key = megalib.azure_lookup(auth.header, input('azure expressroute key: '), prod=True)

    # Print response if call successful
    if key.status_code == 200:
        print(key.json)

    # Advise user if lookup failed
    else:
        print('azure expressroute key lookup failed')

# Advise user if login failed
else:
    print('login failed')
