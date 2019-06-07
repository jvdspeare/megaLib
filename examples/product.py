import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login_token(input('Enter token: '))

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login successful')

    # Retrieve the service list using the megalib.product function
    services = megalib.product(auth.header)

    # Check if the product call was successful by observing the HTTP Status Code
    if services.status_code == 200:
        print('Services retrieved successfully')

        uid = input('Enter Uid: ')

        for P in services.json['data']:
            if P['productUid'] == uid:
                for A in P['associatedVxcs']:
                    print('Name: ' + A['productName'] + ' Service ID:' + A['productUid'][:8] + ' aEnd Service ID: ' +
                          A['aEnd']['productUid'][:8] + ' bEnd Service ID: ' + A['bEnd']['productUid'][:8])

    # Advise user if product call failed, print the status code & JSON
    else:
        print('Failed to retrieve services, status code: ' + str(services.status_code) + ', JSON: ' +
              str(services.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login failed, status code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
