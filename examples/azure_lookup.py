import megalib

l = megalib.login(input('username'), input('password'))

if l[0] == 200:
    a = megalib.azure_lookup(l[2], input('azure expressroute key'))

    if a[0] == 200:
        print('key is valid')
    else:
        print('key is invalid')

else:
    print('failed login')
