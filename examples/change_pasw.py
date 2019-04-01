# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass, input('tfa (leave black if not enabled): '), prod=False)

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Change user password using the megalib.change_pasw function
    passw = megalib.change_pasw(auth.header, 'old password: ', 'new password: ', prod=False)

    # Check if password change was successful by observing the HTTP Status Code
    if passw.status_code == 200:
        print('password changed')

    # Advise user if password change failed
    else:
        print('password change failed')

# Advise user if login failed
else:
    print('login failed')
