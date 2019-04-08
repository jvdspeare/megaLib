# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Retrieve new port price using the megalib.new_port_price function
    price = megalib.new_port_price(auth.header, input('Location ID: '), input('Speed: '), prod=False)

    # Print monthly cost
    if price.status_code == 200:
        print(str(price.monthly_rate) + ' ' + price.currency)

    # Advise user if lookup failed, print the status code & JSON
    else:
        print('Port Price Lookup Failed, Status Code: ' + str(price.status_code) + ', JSON: ' + str(price.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
