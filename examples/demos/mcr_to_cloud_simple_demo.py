# Import megalib
from megaLib import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Leave black if not enabled): '))

# Order MCR - Replace 'loc_id' with the desired location ID
mcr = megalib.mcr(auth.header, loc_id, 'megaLib MCR', 100)

# Order AWS VXC - Replace 'b_uid' with the desired AWS target UID and 'account_num' with the target AWS account number
vxc = megalib.aws(auth.header, mcr.uid, b_uid, 'megaLib VXC', 100, 7224, account_num)

# Check for 'Great Success!'
if mcr.status_code and vxc.status_code == 200:
    print('Great Success!')
