# Import megalib
from megaLib import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve new vxc price using the megalib.new_vxc_price function
    price = megalib.new_vxc_price(auth.header, input('location id: '), input('b end location id: '), input('speed: '),
                                  prod=True)

    # Print monthly cost
    if price.status_code == 200:
        print(price.currency + ' ' + str(price.monthly_rate))

    # Advise user if lookup failed
    else:
        print('price lookup failed')

# Advise user if login failed
else:
    print('login failed')
