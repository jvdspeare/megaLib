# Import megalib & getpass
import megalib
import getpass

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Optional): '), prod=False)

# Observe the HTTP Status Code and advise user if login was successful
if auth.status_code == 200:
    print('Login Successful')

    # Retrieve invoice using the megalib.invoice function
    invoice = megalib.invoice(auth.header, prod=False)

    # Check if the invoice call was successful by observing the HTTP Status Code
    if invoice.status_code == 200:
        # Print the body of the response
        print(invoice.json)

    # Advise user if invoice call failed, print the status code & JSON
    else:
        print('Invoice Call Failed, Status Code: ' + str(invoice.status_code) + ', JSON: ' + str(invoice.json))

# Advise user if login failed, print the status code & JSON
else:
    print('Login Failed, Status Code: ' + str(auth.status_code) + ', JSON: ' + str(auth.json))
