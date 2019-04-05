# Import megalib
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('username: '), getpass.getpass(), input('tfa (leave black if not enabled): '))

# Check if logging was successful by observing the HTTP Status Code
if auth.status_code == 200:
    print('login successful')

    # Retrieve invoice using the megalib.invoice function
    invoice = megalib.invoice(auth.header, csv=True)

    # Check if the invoice call was successful by observing the HTTP Status Code
    if invoice.status_code == 200:
        # Print the body of the response
        print(invoice.json)

    # Advise user if the call failed
    else:
        print('failed')

# Advise user if login failed
else:
    print('login failed')
