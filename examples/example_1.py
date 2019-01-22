import megalib

# login to obtain token
x = megalib.login(input('enter username '), input('enter password '))

# validate port order
y = megalib.port(x[1], 23, 'megaport', 1000, 'AU', validate=True)

# print
print(y[1].json())
print(y[2])
