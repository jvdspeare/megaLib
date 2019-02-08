import megalib
x = megalib.login(input('username'), input('password'))

if x[0] == 200:
    y = megalib.service_key(x[2], 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'test service key')
    print(y[1].json())
else:
    print('failed login')
