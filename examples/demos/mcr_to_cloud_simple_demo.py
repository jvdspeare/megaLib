# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), input('Password: '), input('TFA (Leave black if not enabled): '), prod=False)

# Order MCR
mcr = megalib.mcr(auth.header, loc_id, 'megaLib MCR', 100, 'AU')

# Order AWS VXC
vxc = megalib.aws(auth.header, mcr.uid, b_uid, 'megaLib VXC', 100, 7224, account_num)

# Check for 'Great Success!'
if mcr.status_code and vxc.status_code == 200:
    print('Great Success!')
