# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), input('password: '), input('tfa (leave black if not enabled): '), prod=True)

# Retrieve partner ports using the megalib.partner function
partner_loc = megalib.partner(auth.header, prod=True)

# Check if the partner ports call was successful by observing the HTTP Status Code
if partner_loc.status_code == 200:
    partner_loc_data = partner_loc.json['data']

    for L in partner_loc_data:
        if L['connectType'] == 'AWS' and L['vxcPermitted'] is True:
            print(L['productUid'] + ' ' + str(L['locationId']))

# Advise user if the partner ports call failed
else:
    print('failed')

