# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Retrieve speed change price using the megalib.speed_change_price function
    price = megalib.speed_change_price(auth.header, input('Service UID: '), input('Year: '), input('Month: '),
                                       input('New Speed: '), prod=False)

    # Print monthly cost
    if price.status_code == 200:
        print(price.currency + ' ' + str(price.new_monthly_rate))
        print('Cost Difference: ' + str(price.delta))

    # Advise user if failed, print the status code & JSON
    else:
        print('Failed To Retrieve Speed Change Price, Status Code: ' + str(price.status_code) + ', JSON: ' +
              str(price.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
