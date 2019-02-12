import megalib

l = megalib.login(input('username'), input('password'), input('tfa'))

if l.status_code == 200:
    print(l.header)

else:
    print('login failed')
