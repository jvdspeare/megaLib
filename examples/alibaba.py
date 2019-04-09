# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Order VXC to Alibaba using the megalib.aws function
    aws = megalib.alibaba(auth.header, input('Port UID: '), input('Alibaba Target Port UID: '), input('VXC Name: '),
                          input('Speed (Rate Limit): '), input('Alibaba Owner ID: '), prod=False)

    # Advise user if order was successful
    if aws.status_code == 200:
        print('Alibaba VXC Ordered Successfully')

    # Advise user if order failed, print the status code & JSON
    else:
        print('Alibaba Order Failed, Status Code: ' + str(aws.status_code) + ', JSON: ' + str(aws.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
