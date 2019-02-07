import megalib
y = megalib.login(input('username'), input('password'))
if y[0] == 200:
    x = megalib.port(y[2], 32, 'megaport name', 1000, 'AU', validate=True)
    if x[0] == 200:
        print('monthly cost ' + str(x[2]))
        z = megalib.port(y[2], 32, 'megaport name', 1000, 'AU')
        print('Uid' + z[2])
    else:
        print('failed validation')
else:
    print('failed login')
