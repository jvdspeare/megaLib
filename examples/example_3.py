import megalib

# login to obtain token
x = megalib.login(input('enter username '), input('enter password '))

# verify login was successful
if x[0] == 200:

    # order megaport
    y = megalib.port(x[2], 23, 'test_port', 1000, 'AU')

    # print Uid if successful
    if y[0] == 200:
        print('Uid: ' + y[2])
    else:
        print('failed')
else:
    print('login failed')
