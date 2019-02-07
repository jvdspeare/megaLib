import megalib
y = megalib.login(input('username'), input('password'))
if y[0] == 200:
    x = megalib.ix_locations(y[2], 29)
    print(x[1].json())
else:
    print('failed login')
