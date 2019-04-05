# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '))

# Get locations and partner locations
loc = megalib.locations(auth.header)
partner_loc = megalib.partner(auth.header)

# Check if locations where retrieved successful
if loc.status_code and partner_loc.status_code == 200:
    print('Locations retrieved successfully')
    loc_data = loc.json['data']
    partner_loc_data = partner_loc.json['data']

    for P in loc_data:
        for L in partner_loc_data:
            if L['connectType'] == 'AWS' and L['vxcPermitted'] is True:
                if L['locationId'] == P['id']:
                    print(P['name'] + ' ' + L['title'] + ' productUid: ' + L['productUid'] + ' locationId: ' +
                          str(L['locationId']))

# Advise user if the partner ports call failed
else:
    print('failed')
