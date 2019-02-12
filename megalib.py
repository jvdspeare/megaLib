import requests
import time

# urls
env_url = ['https://api.megaport.com', 'https://api-staging.megaport.com']
netdesign_url = {True: '/v2/networkdesign/validate', False: '/v2/networkdesign/buy'}


# select environment
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


# api put method template
def put(url, header=None, body=None):
    response = requests.put(url, header=header, json=body)
    return response.status_code, response


# extended response
def order_response(response, validate, obj):
    json = response[1].json()
    if validate is False and response[0] == 200:
        return response[0], response[1], json['data'][0][obj]
    elif validate is True and response[0] == 200:
        return response[0], response[1], json['data'][0]['price']['monthlyRate']
    else:
        return response


# price response
def price_response(response, obj, b_obj):
    json = response[1].json()
    if response[0] == 200:
        return response[0], response[1], json['data'][obj], json['data'][b_obj]
    else:
        return response


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
    return order_response(post(url, header, body), validate, 'technicalServiceUid')


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
    return order_response(post(url, header, body), validate, 'technicalServiceUid')


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
    return order_response(post(url, header, body), validate, 'technicalServiceUid')


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
    return order_response(post(url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#standard-api-orders-service-keys-get
def service_key_lookup(header, uid=None, prod=True):
    if uid is None:
        url = env(prod) + '/v2/service/key'
    else:
        url = env(prod) + '/v2/service/key/' + uid
    return get(url, header)


# https://dev.megaport.com/#standard-api-orders-service-keys-post
def service_key(header, uid, desc, vlan='null', single_use='true', max_speed='null', pre_approved='true',
                active='true', s_time='null', e_time='null', prod=True):
    url = env(prod) + '/v2/service/key'
    body = {'productUid': uid,
            'vlan': vlan,
            'singleUse': single_use,
            'maxSpeed': max_speed,
            'preApproved': pre_approved,
            'description': desc,
            'active': active,
            'validFor': {
                'start': s_time,
                'end': e_time
            }}
    return post(url, header, body)


# https://dev.megaport.com/#cloud-partner-api-orders-aws-buy
def aws(header, uid, b_uid, name, speed, asn, account_num, vlan='null', peering_type='private', auth_key='',
        cidr='', cust_ip='', aws_ip='', validate=False, prod=True):
    url = env(prod) + netdesign_url[validate]
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'partnerConfigs': {
                     'connectType': 'AWS',
                     'type': peering_type,
                     'asn': asn,
                     'ownerAccount': account_num,
                     'authKey': auth_key,
                     'prefixes': cidr,
                     'customerIpAddress': cust_ip,
                     'amazonIpAddress': aws_ip
                 },
                 'aEnd': {
                     'vlan': vlan
                 },
                 'bEnd': {
                     'productUid': b_uid
                 }}]}]
    return order_response(post(url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#cloud-partner-api-orders-azure-step-1-lookup
def azure_lookup(header, azure_key, prod=True):
    url = env(prod) + '/v2/secure/Azure/' + azure_key
    response = get(url, header)
    json = response[1].json()
    if response[0] == 200:
        return response[0], response[1], json['data'][0]['bandwidth'], \
               json['data'][0]['megaports'][0]['vxc'], json['data'][0]['megaports'][0]['productUid'], \
               json['data'][0]['megaports'][1]['vxc'], json['data'][0]['megaports'][1]['productUid'], \
               json['data'][0]['vlan']
    else:
        return response


# https://dev.megaport.com/#cloud-partner-api-orders-azure-step-2-buy
def azure(header, uid, b_uid, name, speed, b_vlan, azure_key, private=True, microsoft=True, vlan='null', validate=False,
          prod=True):
    url = env(prod) + netdesign_url[validate]
    peers = []
    if private is True:
        peers.append(dict({'type': 'private'}))
    elif microsoft is True:
        peers.append(dict({'type': 'microsoft'}))
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': {
                     'vlan': vlan,
                 },
                 'bEnd': {
                     'productUid': b_uid,
                     'vlan': b_vlan,
                     'partnerConfig': {
                         'connectType': 'AZURE',
                         'serviceKey': azure_key,
                         'peers': peers
                     }}}]}]
    return order_response(post(url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#price-new-port-price
def new_port_price(header, loc_id, speed, term=1, prod=True):
    url = env(prod) + '/v2/pricebook/megaport?locationId=' + str(loc_id) + '&speed=' + str(speed) + '&term=' + \
          str(term) + '&virtual=false'
    return price_response(get(url, header), 'monthlyRate', 'currency')


# https://dev.megaport.com/#price-new-mcr-price
def new_mcr_price(header, loc_id, speed, prod=True):
    url = env(prod) + '/v2/pricebook/megaport?locationId=' + str(loc_id) + '&speed=' + str(speed) + \
          '&virtual=true'
    return price_response(get(url, header), 'monthlyRate', 'currency')


# https://dev.megaport.com/#price-new-vxc-price
def new_vxc_price(header, loc_id, b_loc_id, speed, prod=True):
    url = env(prod) + '/v2/pricebook/vxc?aLocationId=' + str(loc_id) + '&speed=' + str(speed) + '&bLocationId=' + \
          str(b_loc_id)
    return price_response(get(url, header), 'monthlyRate', 'currency')


# https://dev.megaport.com/#price-new-ix-price
def new_ix_price(header, ix_name, loc_id, speed, prod=True):
    url = env(prod) + '/v2/pricebook/ix?ixType=' + ix_name + '&portLocationId=' + str(loc_id) + '&speed=' + str(speed)
    return price_response(get(url, header), 'monthlyRate', 'currency')


# https://dev.megaport.com/#price-speed-change-check-price
def speed_change_price(header, uid, year, month, new_speed, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/rating/' + str(year) + '/' + str(month) + '?newSpeed=' + str(new_speed)
    return price_response(get(url, header), 'longTermMonthly', 'delta')


# https://dev.megaport.com/#price-lifecycle-action-change-price-check
def lifecycle_change_price(header, uid, action, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/action/' + action + '/charges'
    return get(url, header)


# https://dev.megaport.com/#invoices-all-invoices
# https://dev.megaport.com/#invoices-single-invoice
# https://dev.megaport.com/#invoices-single-invoice-as-pdf
def invoice(header, invoice_id=None, pdf=False, prod=True):
    if invoice_id is None:
        url = env(prod) + '/v2/invoice'
    elif invoice_id is not None and pdf is False:
        url = env(prod) + '/v2/invoice/' + invoice_id
    else:
        url = env(prod) + '/v2/invoice/' + invoice_id + '/pdf'
    return get(url, header)


# https://dev.megaport.com/#general-get-product-list
# https://dev.megaport.com/#general-get-product-details
def product(header, uid=None, prod=True):
    if uid is None:
        url = env(prod) + '/v2/products'
    else:
        url = env(prod) + '/v2/products/' + uid
    return get(url, header)


# https://dev.megaport.com/#general-update-product-details-port
def update_port(header, uid, name=None, market_vis=None, speed=None, prod=True):
    url = env(prod) + '/v2/product/' + uid
    body = dict()
    if name is not None:
        body['name'] = name
    if market_vis is not None:
        body['marketplaceVisibility'] = market_vis
    if speed is not None:
        body['rateLimit'] = speed
    return put(url, header, body)


# https://dev.megaport.com/#general-update-product-details-vxc
def update_vxc(header, uid, name=None, speed=None, vlan=None, vlan_b=None, prod=True):
    url = env(prod) + '/v2/product/vxc/' + uid
    body = dict()
    if name is not None:
        body['name'] = name
    if speed is not None:
        body['rateLimit'] = speed
    if vlan is not None:
        body['aEndVlan'] = vlan
    if vlan_b is not None:
        body['bEndVlan'] = vlan_b
    return put(url, header, body)


# https://dev.megaport.com/#general-update-product-details-ix
def update_ix(header, uid, name=None, speed=None, vlan=None, vlan_b=None, prod=True):
    url = env(prod) + '/v2/product/vxc/' + uid
    body = dict()
    if name is not None:
        body['name'] = name
    if speed is not None:
        body['rateLimit'] = speed
    if vlan is not None:
        body['aEndVlan'] = vlan
    if vlan_b is not None:
        body['bEndVlan'] = vlan_b
    return put(url, header, body)
