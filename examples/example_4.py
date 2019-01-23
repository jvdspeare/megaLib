import megalib

x = megalib.login(input('enter username '), input('enter password '))

if x[0] == 200:
    y = megalib.port(x[2], 4, 'test port 1', 1000, 'AU')
    z = megalib.port(x[2], 4, 'test port 2', 1000, 'AU')
    if y[0] == 200 and z[0] == 200:
        v = megalib.vxc(x[2], y[2], z[2], 'test vxc', 1000)
        print(v[0])
        print(v[1].json())
    else:
        print('port &/or mcr failed')
else:
    print('login failed')
