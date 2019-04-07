# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave blank if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve speed change price using the megalib.speed_change_price function
    price = megalib.speed_change_price(auth.header, input('uid: '), input('year: '), input('month: '),
                                       input('new_speed: '), prod=False)

    # Print monthly cost
    if price.status_code == 200:
        print(price.currency + ' ' + str(price.new_monthly_rate))
        print('the difference in cost is: ' + str(price.delta))

    # Advise user if lookup failed
    else:
        print('price lookup failed')

# Advise user if login failed
else:
    print('login failed')
