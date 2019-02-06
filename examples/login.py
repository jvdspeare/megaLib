import megalib
x = megalib.login(input('username'), input('password'), input('tfa'), False)
if x[0] == 200:
    print(x[0], x[1], x[2])
else:
    print(x[0], x[1])
