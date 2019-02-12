import megalib

l = megalib.login(input('username'), input('password'))

p = megalib.new_port_price(l[2], 44, 1000)

print(str(p.monthly_rate) + p.currency)
