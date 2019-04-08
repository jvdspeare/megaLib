# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Change user password using the megalib.change_pasw function
    passw = megalib.change_pasw(auth.header, 'Old Password: ', 'New Password: ', prod=False)

    # Check if password change was successful by observing the HTTP Status Code
    if passw.status_code == 200:
        print('Password Changed Successfully')

    # Advise user if password change failed, print the status code & JSON
    else:
        print('Password Change Failed, Status Code: ' + str(passw.status_code) + ', JSON: ' + str(passw.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
