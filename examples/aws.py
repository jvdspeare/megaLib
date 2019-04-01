# Import megalib
from megaLib import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Order VXC to AWS using the megalib.aws function
    aws = megalib.aws(auth.header, input('uid: '), input('aws target uid: '), input('name: '), input('speed: '),
                      input('aws asn: '), input('aws account number: '), input('asn: '), input('mcr connect: '),
                      input('aws auto: '), input('vlan: '), input('peering type: '), input('bgp md5 auth key: '),
                      input('advertised routes: '), input('bgp peering ip address: '),
                      input('aws bgp peering ip address'), validate=False, prod=False)

    # Advise user if order was successful
    if aws.status_code == 200:
        print('aws vxc ordered successfully')

    # Advise user if order failed
    else:
        print('aws vxc order failed')

# Advise user if login failed
else:
    print('login failed')
