import megalib
y = megalib.login_token(input('username'), input('password'))
if y[0] == 200:
    x = megalib.change_pasw(y[2], input('old password'), input('new password'))
else:
    print('failed login')
