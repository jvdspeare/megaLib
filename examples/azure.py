import megalib
a = list()

l = megalib.login(input('username'), input('password'))

k = input('azure expressroute key')

if l[0] == 200:
    a = megalib.azure_lookup(l[2], k)

    if a[0] == 200:
        y = megalib.port(l[2], 44, 'megaport', 1000, 'AU')

        if y[0] == 200:
            print('megaport deployed successfully')
            v = megalib.azure(l[2], y[2], a[4], 'azure vxc', 1000, a[7], k)

            if v[0] == 200:
                print('vxc deployed successfully')
            else:
                print('error, here is what megaport says...' + v[1], v[1].json())

        else:
            print('failed to deploy megaport')

    else:
        print('failed azure expressroute key lookup')

else:
    print('failed login')
