# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=True)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Input the Azure Expressroute Key
    expressroute_key = input('Azure Expressroute Key: ')

    # Lookup the Azure Expressroute Key using the megalib.azure_lookup function
    key = megalib.azure_lookup(auth.header, expressroute_key, prod=True)

    # Observe the HTTP Status Code and advise user if azure lookup was successful
    if key.status_code == 200:
        print('Azure Expressroute Key Lookup Successful')

        # Order VXC to Azure using the megalib.azure function
        # Azure Expressroute Keys have two targets (primary and secondary), this example uses the primary target
        azure = megalib.azure(auth.header, input('Port UID: '), key.uid[0], input('VXC Name: '),
                              input('Speed (Rate Limit): '), expressroute_key, prod=True)

        # Advise user if order was successful
        if azure.status_code == 200:
            print('Azure VXC Ordered Successfully')

        # Advise user if order failed, print the status code & JSON
        else:
            print('Azure VXC Order Failed, Status Code: ' + str(azure.status_code) + ', JSON: ' + str(azure.json))

    # Advise user if Azure Expressroute Key lookup failed, print the status code & JSON
    else:
        print('Azure Expressroute Key Lookup Failed, Status Code: ' + str(key.status_code) + ', JSON: ' + str(key.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
