# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '))

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Get locations
    loc = megalib.locations(auth.header).json

    loc_data = loc['data']

    loc_id_list = []

    x = 0

    for L in loc_data:
        if L['vRouterAvailable'] is True:
            loc_id_list.append(L['id'])
            print('[' + str(x) + '] ' + str(L['name']))
            x += 1

    # Order MCR using the megalib.mcr function
    mcr = megalib.mcr(auth.header, input('location id: '), input('service name: '), input('speed: '), input('market: '))

    # Advise user if mcr order was successful
    if mcr.status_code == 200:
        print('mcr ordered successfully')

        # Order VXC to AWS using the megalib.aws function
        vxc = megalib.aws(auth.header, mcr.uid, )

    # Advise user if mcr order failed
    else:
        print('mcr order failed')

# Advise user if login failed
else:
    print('login failed')
