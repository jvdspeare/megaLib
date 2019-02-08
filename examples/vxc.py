import megalib
a = list()

l = megalib.login(input('username'), input('password'))

for x in (44, 144):
    y = megalib.port(l[2], x, 'megaport ' + str(x), 1000, 'AU')
    if y[0] == 200:
        a.append(y[2])
        print('megaport ' +str(x) + ' deployed successfully')
    else:
        quit(print('failed to deploy megaport ' + str(x)))

v = megalib.vxc(l[2], a[1], a[2], 'vxc', 1000)
if v[0] == 200:
    print('vxc deployed successfully')
