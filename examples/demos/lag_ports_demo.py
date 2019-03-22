# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), input('Password: '), input('TFA (Leave black if not enabled): '))

port = megalib.port(auth.header, 60, '''Jim's Test Lag''', 10000, lag_count=2)

print(port.status_code)
print(port.json)
print(port.uid)
