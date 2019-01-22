import megalib

# login to obtain token
x = megalib.login(input('enter username '), input('enter password '))

# check if login was successful
if x[0] == 200:
    print('successful login')
    # the third object returned in the tuple ('x[2]') is the header which can be used for subsequent calls
    print(x[2])
    # check the token is valid using the login_token function. the header was returned in the tuple from the login
    # function as the forth object ('x[3]')
    y = megalib.login_token(x[3])
    if y[0] == 200:
        print('token valid')
    else:
        print('token invalid')
else:
    print('login unsuccessful')
    # the second object returned in the tuple ('x[1]') is always the entirety of the response data which has a number of
    # objects, json is the response body
    print(x[1].json())
