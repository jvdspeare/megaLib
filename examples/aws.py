import megalib
a = list()

l = megalib.login(input('username'), input('password'))

if l[0] == 200:

    y = megalib.port(l[2], 44, 'megaport', 1000, 'AU')

    if y[0] == 200:
        print('megaport deployed successfully')
        v = megalib.aws(l[2], y[2], 'df37ac05-0c21-4292-9729-695f5ea4645d', 'aws vxc', 1000, 123456, '684021030471')

        if v[0] == 200:
            print('vxc deployed successfully')
        else:
            print('error, here is what megaport says...' + v[1], v[1].json())

    else:
        print('failed to deploy megaport')

else:
    print('failed login')
