import requests
import time

env_url = ['https://api.megaport.com', 'https://api-staging.megaport.com']


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


# login and if successful return header to be used for subsequent api calls
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
        token = json["data"]["token"]
        header = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
        return header
    else:
        return response


# locations end point will return a list of data centre locations and information pertaining to each
def locations(header, prod=True):
    url = env(prod) + '/v2/locations'
    return get(url, header)


# partner end point will return a list of public partner megaports and information pertaining to each
def partner(header, prod=True):
    url = env(prod) + '/v2/dropdowns/partner/megaports'
    return get(url, header)


# ix end point will return a list of all available ix types for a given location
def ix(header, loc_id, prod=True):
    url = env(prod) + '/v2/product/ix/types?locationId=' + str(loc_id)
    return get(url, header)


# validate an order for a megaport
def port_validate(header, loc_id, name, speed, market, term=1, prod=True):
    url = env(prod) + '/v2/networkdesign/validate'
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
    return post(url, header, body)


# place an order for a megaport
def port_buy(header, loc_id, name, speed, market, term=1, prod=True):
    url = env(prod) + '/v2/networkdesign/buy'
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
    return post(url, header, body)


# validate an order for a mcr
def mcr_validate(header, loc_id, name, speed, market, asn=133937, term=1, prod=True):
    url = env(prod) + '/v2/networkdesign/validate'
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
             }
             }]
    return post(url, header, body)


# place an order for a mcr
def mcr_buy(header, loc_id, name, speed, market, asn=133937, term=1, prod=True):
    url = env(prod) + '/v2/networkdesign/buy'
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
             }
             }]
    return post(url, header, body)
