import megalib
y = megalib.login(input('username'), input('password'))
if y[0] == 200:
    x = megalib.partner(y[2])
    print(x[1].json())
else:
    print('failed login')
