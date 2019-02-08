import megalib
x = megalib.login(input('username'), input('password'))

if x[2] == 200:
    y = megalib.service_key_lookup(x[2], 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
    print(y[1].json())
else:
    print('failed login')
