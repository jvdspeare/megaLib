# Import megalib
import megalib

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), input('Password: '), input('TFA (Leave black if not enabled): '), prod=False)
print(auth.status_code)
print(auth.json)
print(auth.header)

port = megalib.port(auth.header, 33, '''Jim's Test''', 10000, 'AU', lag_count=2)

megalib.port

print(port.status_code)
print(port.json)
