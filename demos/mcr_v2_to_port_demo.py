# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Leave blank if not enabled): '))

# Order VXC - Replace 'uid', 'b_uid', 'name' & 'speed' with the desired values
# bfd, ip, routes, bgp & nat are all optional parameters
uid = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
b_uid = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
name = 'VXC Name'
speed = 100

# configure all of the things (IP, BGP + MED + MD5, BFD, Static Route, NAT)
#vxc = megalib.vxc(auth.header, uid, b_uid, name, speed, mcr_connect=True,
#                  bfd={'rxInterval': 300, 'txInterval': 300, 'multiplier': 3}, ip=['10.0.0.0/31'],
#                  routes=[{'description': 'Static', 'prefix': '192.168.0.0/24', 'nextHop': '10.0.0.1/31'}],
#                  bgp=[{'password': 'md5authkeygoeshere', 'peerIpAddress': '10.0.0.1', 'localIpAddress': '10.0.0.0',
#                        'shutdown': False, 'medIn': 100, 'peerAsn': 65333, 'bfdEnabled': True,
#                        'description': 'my bgp connection', 'medOut': 200}], nat=['10.0.0.0'])

# configure only an IP
# vxc = megalib.vxc(auth.header, uid, b_uid, name, speed, mcr_connect=True, ip=['192.168.0.0/31'])

# configure an IP & BGP
# vxc = megalib.vxc(auth.header, uid, b_uid, name, speed, mcr_connect=True, ip=['192.168.1.0/31'],
#                  bgp=[{'peerIpAddress': '192.168.1.1', 'localIpAddress': '192.168.1.0', 'shutdown': False,
#                        'peerAsn': 65333, 'bfdEnabled': False, 'description': 'my bgp connection'}])

# Check for 'Great Success!'
if vxc.status_code == 200:
    print('Great Success!')
else:
    print(vxc.json)
