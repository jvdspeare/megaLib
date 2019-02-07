import megalib
y = megalib.login(input('username'), input('password'))
if y[0] == 200:
    x = megalib.port(y[2], 32, 'megaport name', 1000, 'AU', validate=True)
    if x[0] == 200:
        print('monthly cost ' + str(x[2]))
        z = megalib.port(y[2], 32, 'megaport name', 1000, 'AU')
        print('Uid' + z[2])
        if z[0] == 200:
            a = megalib.ix(y[2], z[2], 'ix name', 'ix name name', 123456, 'b5:b4:b3:b2:b1:b0', 1000, validate=True)
            if a[0] == 200:
                print('monthly cost ' + str(a[2]))
                b = megalib.ix(y[2], z[2], 'ix name', 'ix name name', 123456, 'b5:b4:b3:b2:b1:b0', 1000)
                if b[0] == 200:
                    print('Uid' + b[2])
                else:
                    print('failed ix order')
            else:
                print('failed ix validation')
        else:
            print('failed port order')
    else:
        print('failed port validation')
else:
    print('failed login')
