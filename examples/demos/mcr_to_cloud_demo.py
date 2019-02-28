# Import megalib
import megalib

# Authenticate user credentials
auth = megalib.login(input('Username: '), input('Password: '), input('TFA (Leave black if not required): '))

# Check if logging was successful
if auth.status_code == 200:
    print('Login successful')

    # Get locations
    loc = megalib.locations(auth.header)

    # Check if locations where retrieved successful
    if loc.status_code == 200:
        print('Locations retrieved successfully')
        loc_data = loc.json['data']
        loc_id_list = []
        x = 0

        # MCR locations list
        for L in loc_data:
            if L['vRouterAvailable'] is True:
                loc_id_list.append(L['id'])
                print('[' + str(x) + '] ' + str(L['name']))
                x += 1

        # Select MCR
        loc_id = loc_id_list[int(input('Select MCR: '))]

        # Order MCR
        mcr = megalib.mcr(auth.header, loc_id, '''Jim's MCR''', 100, 'AU')

        # Check if locations where retrieved successful
        if mcr.status_code == 200:
            print('MCR ordered successfully')

            # Order VXC to AWS using the megalib.aws function
            vxc = megalib.aws(auth.header, mcr.uid, )

    # Advise user if mcr order failed
    else:
        print('mcr order failed')

# Advise user if login failed
else:
    print('login failed')
