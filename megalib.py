import requests
import time

env_url = ['https://api.megaport.com', 'https://api-staging.megaport.com']
netdesign_url = {True: '/v2/networkdesign/validate', False: '/v2/networkdesign/buy'}


def env(prod):
    if prod is True:
        url = env_url[0]
    else:
        url = env_url[1]
    return url


# api get method template
def get(url, header):
    response = requests.get(url, headers=header)
    return response


# api post method template
def post(url, header, body):
    response = requests.post(url, headers=header, json=body)
    return response


# https://dev.megaport.com/#security-login-with-user-details
def login(user, pasw, tfa=None, prod=True):
    if tfa is None:
        response = requests.post(env(prod)
                                 + '/v2/login' + '?username=' + user + '&password=' + pasw)
    else:
        response = requests.post(env(prod)
                                 + '/v2/login' + '?username=' + user + '&password=' + pasw + '&oneTimePassword='
                                 + str(tfa))
    if response.status_code == 200:
        json = response.json()
        login.token = json['data']['token']
        login.header = {'X-Auth-Token': login.token, 'Content-Type': 'application/json'}
    return response


# https://dev.megaport.com/#security-login-with-token
def login_token(token, prod=True):
    return requests.post(env(prod) + '/v2/login/' + token)


# https://dev.megaport.com/#security-logout
def logout(token, prod=True):
    return requests.get(env(prod) + '/v2/logout/' + token)


# https://dev.megaport.com/#security-change-password
def change_pasw(header, old_pasw, new_pasw, prod=True):
    return requests.post(env(prod)
                         + '/v2/password/change?oldPassword=' + old_pasw + '&newPassword=' + new_pasw, headers=header)


# https://dev.megaport.com/#lists-used-for-ordering-locations
def locations(header, prod=True):
    url = env(prod) + '/v2/locations'
    return get(url, header)


# https://dev.megaport.com/#lists-used-for-ordering-partner-megaports
def partner(header, prod=True):
    url = env(prod) + '/v2/dropdowns/partner/megaports'
    return get(url, header)


# https://dev.megaport.com/#lists-used-for-ordering-internet-exchanges-ix
def ix_locations(header, loc_id, prod=True):
    url = env(prod) + '/v2/product/ix/types?locationId=' + str(loc_id)
    return get(url, header)


# https://dev.megaport.com/#standard-api-orders-validate-port-order
# https://dev.megaport.com/#standard-api-orders-buy-port
def port(header, loc_id, name, speed, market, term=1, validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'locationId': loc_id,
             'term': term,
             'locationUid': 'null',
             'productName': name,
             'productType': 'MEGAPORT',
             'createDate': int(time.time()),
             'portSpeed': speed,
             'virtual': 'false',
             'market': market
             }]
    response = post(url, header, body)
    if validate is False and x.status_code == 200:
        json = response.json()
        print(json)
        port.uid = json['data'][0]['technicalServiceUid']
    return response


# https://dev.megaport.com/#standard-api-orders-validate-mcr-order
# https://dev.megaport.com/#standard-api-orders-buy-mcr
def mcr(header, loc_id, name, speed, market, asn=133937, term=1, validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'locationId': loc_id,
             'term': term,
             'locationUid': 'null',
             'productName': name,
             'productType': 'MEGAPORT',
             'createDate': int(time.time()),
             'portSpeed': speed,
             'virtual': 'true',
             'market': market,
             'config': {
                 'mcrAsn': asn
             }}]
    return post(url, header, body)


# https://dev.megaport.com/#standard-api-orders-validate-ix-order
# https://dev.megaport.com/#standard-api-orders-buy-ix
def ix(header, loc_id, name, speed, market, asn=133937, term=1, validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'locationId': loc_id,
             'term': term,
             'locationUid': 'null',
             'productName': name,
             'productType': 'MEGAPORT',
             'createDate': int(time.time()),
             'portSpeed': speed,
             'virtual': 'true',
             'market': market,
             'config': {
                 'mcrAsn': asn
             }}]
    return post(url, header, body)


# https://dev.megaport.com/#standard-api-orders-validate-vxc-order
# https://dev.megaport.com/#standard-api-orders-buy-vxc
def vxc(header, prod_id, b_prod_id, name, speed, vlan='null', b_vlan='null', validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'productUid': prod_id,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': {
                     'vlan': vlan
                 },
                 'bEnd': {
                     'productUid': b_prod_id,
                     'vlan': b_vlan
                 }}]}]
    return post(url, header, body)
