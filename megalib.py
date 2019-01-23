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
def get(url, header=None):
    response = requests.get(url, headers=header)
    return response.status_code, response


# api post method template
def post(url, header=None, body=None):
    response = requests.post(url, headers=header, json=body)
    return response.status_code, response


# https://dev.megaport.com/#security-login-with-user-details
def login(user, pasw, tfa=0, prod=True):
    url = env(prod) + '/v2/login' + '?username=' + user + '&password=' + pasw + '&oneTimePassword=' + str(tfa)
    response = post(url)
    if response[0] == 200:
        json = response[1].json()
        return response[0], response[1], {'X-Auth-Token': json['data']['token'], 'Content-Type': 'application/json'}, \
            json['data']['token']
    else:
        return response


# https://dev.megaport.com/#security-login-with-token
def login_token(token, prod=True):
    url = env(prod) + '/v2/login/' + token
    return post(url)


# https://dev.megaport.com/#security-logout
def logout(token, prod=True):
    url = env(prod) + '/v2/logout/' + token
    return get(url)


# https://dev.megaport.com/#security-change-password
def change_pasw(header, old_pasw, new_pasw, prod=True):
    url = env(prod) + '/v2/password/change?oldPassword=' + old_pasw + '&newPassword=' + new_pasw
    return post(url, header)


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
    json = response[1].json()
    if validate is False and response[0] == 200:
        return response[0], response[1], json['data'][0]['technicalServiceUid']
    elif validate is True and response[0] == 200:
        return response[0], response[1], json['data'][0]['price']['monthlyRate']
    else:
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
    response = post(url, header, body)
    json = response[1].json()
    if validate is False and response[0] == 200:
        return response[0], response[1], json['data'][0]['technicalServiceUid']
    elif validate is True and response[0] == 200:
        return response[0], response[1], json['data'][0]['price']['monthlyRate']
    else:
        return response


# https://dev.megaport.com/#standard-api-orders-validate-ix-order
# https://dev.megaport.com/#standard-api-orders-buy-ix
def ix(header, uid, name, ix_name, asn, mac, speed, vlan='null', validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'productUid': uid,
             'associatedIxs': [{
                 'productName': name,
                 'networkServiceType': ix_name,
                 'asn': asn,
                 'macAddress': mac,
                 'rateLimit': speed,
                 "vlan": vlan
             }]}]
    response = post(url, header, body)
    json = response[1].json()
    if validate is False and response[0] == 200:
        return response[0], response[1], json['data'][0]['technicalServiceUid']
    elif validate is True and response[0] == 200:
        return response[0], response[1], json['data'][0]['price']['monthlyRate']
    else:
        return response


# https://dev.megaport.com/#standard-api-orders-validate-vxc-order
# https://dev.megaport.com/#standard-api-orders-buy-vxc
def vxc(header, uid, b_uid, name, speed, vlan='null', b_vlan='null', validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': {
                     'vlan': vlan
                 },
                 'bEnd': {
                     'productUid': b_uid,
                     'vlan': b_vlan
                 }}]}]
    response = post(url, header, body)
    json = response[1].json()
    if validate is False and response[0] == 200:
        return response[0], response[1], json['data'][0]['vxcJTechnicalServiceUid']
    elif validate is True and response[0] == 200:
        return response[0], response[1], json['data'][0]['price']['monthlyRate']
    else:
        return response
