# Import megalib
from megaLib import megalib
import getpass

# Authenticate user credentials
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Leave black if not required): '))

# Check if logging was successful
if auth.status_code == 200:
    print('Login successful')

    # Get locations and partner locations
    loc = megalib.locations(auth.header)
    partner_loc = megalib.partner(auth.header)

    # Check if locations where retrieved successful
    if loc.status_code and partner_loc.status_code == 200:
        print('Locations retrieved successfully')
        loc_data = loc.json['data']
        partner_loc_data = partner_loc.json['data']

        # MCR locations list
        loc_id_list = []
        x = 0
        for L in loc_data:
            if L['vRouterAvailable'] is True:
                loc_id_list.append(L['id'])
                print('[' + str(x) + '] ' + str(L['name']))
                x += 1

        # Select MCR
        loc_id = loc_id_list[int(input('Select MCR: '))]

        # Order MCR
        mcr = megalib.mcr(auth.header, loc_id, '''Jim's MCR''', 100)

        # Check if locations where retrieved successful
        if mcr.status_code == 200:
            print('MCR ordered successfully')

            # Region list
            menu_market_list = []
            x = 0
            for P in loc_data:
                for L in partner_loc_data:
                    if L['connectType'] == 'AWS':
                        if L['locationId'] == P['id']:
                            menu_create_market = P['market']
                            menu_market_list.append(menu_create_market)
            menu_market_set = set(menu_market_list)
            menu_market_list_unique = list(menu_market_set)
            count_down = len(menu_market_list_unique)
            while count_down > 0:
                print('[' + str(x) + '] ' + menu_market_list_unique[x])
                x += 1
                count_down -= 1

            # Select region
            vxc_loc_id = menu_market_list_unique[int(input('Select Region: '))]

            # Cloud target list
            mega_target_loc_id_list = []
            mega_vxc_uuid_list = []
            x = 0
            for P in loc_data:
                for L in partner_loc_data:
                    if L['connectType'] == 'AWS':
                        if L['locationId'] == P['id']:
                            if P['market'] == vxc_loc_id:
                                if L['vxcPermitted'] is True:
                                    mega_target_loc_id = L['locationId']
                                    mega_target_loc_id_list.append(mega_target_loc_id)
                                    mega_create_vxc_uuid = L['productUid']
                                    mega_vxc_uuid_list.append(mega_create_vxc_uuid)
                                    print('[' + str(x) + '] #' + str(mega_create_vxc_uuid[0:8])
                                          + ' ' + str(P['name']) + ' ' + str(L['title']))
                                    x += 1

            # Select cloud target
            b_uid = mega_vxc_uuid_list[int(input('Select Cloud Target: '))]

            # Input AWS account number
            account_num = input('AWS Account Number: ')

            # Order VXC to AWS using the megalib.aws function
            vxc = megalib.aws(auth.header, mcr.uid, b_uid, '''Jim's AWS VXC''', 100, 7224, account_num)

            if vxc.status_code == 200:
                print('VXC ordered successfully')

            # Advise user if VXC order failed
            else:
                print('VXC order failed')

        # Advise user if MCR order failed
        else:
            print('MCR order failed')

        # Advise user if unable to retrieve locations and/or partner locations data
    else:
        print('Unable to retrieve locations and/or partner locations data')

# Advise user if login failed
else:
    print('Login failed')
