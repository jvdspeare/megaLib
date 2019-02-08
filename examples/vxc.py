import megalib
l = megalib.login(input('username'), input('password'))
a = megalib.port(l[2], 44, 'megaport 44', 1000, 'AU')
b = megalib.port(l[2], 144, 'megaport 144', 1000, 'AU')
v = megalib.vxc(l[2], a[2], b[2], 'vxc', 1000)
