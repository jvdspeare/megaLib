# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '))

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Get locations and partner locations
    loc = megalib.locations(auth.header)
    partner_loc = megalib.partner(auth.header)

    # Check if locations where retrieved successful
    if loc.status_code and partner_loc.status_code == 200:
        print('Locations retrieved successfully')

        # Define lists and select is True
        providers = ['AWS', 'AZURE', 'GOOGLE', 'ORACLE', 'Finish']
        connect_type = list()
        select = True

        # Menu
        while select is True:
            for idx, provider in enumerate(providers):
                print(idx, provider)

            x = int(input('Select the provider: '))
            if x == 4:
                select = False
            else:
                connect_type.append(providers[x])

        # Find results, format and print results
        for N in connect_type:
            for P in loc.json['data']:
                for L in partner_loc.json['data']:
                    if L['connectType'] == N:
                        if L['vxcPermitted'] is True:
                            if L['locationId'] == P['id']:
                                print(L['connectType'] + ' ' + P['name'] + ' ' + L['title'] + ' productUid: ' +
                                      L['productUid'] + ' locationId: ' + str(L['locationId']))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
