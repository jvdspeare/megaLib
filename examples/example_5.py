import megalib

x = megalib.login(input('user'), input('pass'))

y = megalib.service_key(x[2], input('productUid'), 'test2')

print(y[0])
print(y[1].json())
