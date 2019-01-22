import megalib

# login to obtain token
x = megalib.login(input('enter username '), input('enter password '))

# get location and partner port information using the header obtained using the login function to authenticate the call
# when a login is successful the third object in the returned tuple contains the header ('x[2]')
if x[0] == 200:
    locations = megalib.locations(x[2])
    partner_ports = megalib.partner(x[2])

    # print the body of the response for both the locations and partner functions
    print(locations[1].json())
    print(partner_ports[1].json())
else:
    print('login failed')
