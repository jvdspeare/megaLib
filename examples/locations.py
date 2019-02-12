import megalib
y = megalib.login(input('username'), input('password'))
if y[0] == 200:
    x = megalib.locations(y[2])
    print(x.json)
else:
    print('failed login')
