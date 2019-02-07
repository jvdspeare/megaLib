import megalib
y = megalib.login(input('username'), input('password'))
if y[0] == 200:
    x = megalib.port(y[2], 29, 'megaport name', 1000, 'au', validate=True)
    if x[0] == 200:
        print('monthly cost ' + x[2])
        z = megalib.port(y[2], 29, 'megaport name', 1000, 'au')
        print('Uid' + z[2])
    else:
        print('failed validation')
else:
    print('failed login')
