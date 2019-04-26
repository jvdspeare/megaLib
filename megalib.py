# import
import requests
import time

# urls
env_url = ['https://api.megaport.com', 'https://api-staging.megaport.com']
net_design_url = {True: '/v2/networkdesign/validate', False: '/v2/networkdesign/buy'}


# select environment
def env(prod):
    if prod is True:
        url = env_url[0]
    else:
        url = env_url[1]
    return url


# vxcs attached to an mcr require additional configuration
def mcr_attached(mcr_connect, vlan, aws_auto='false', azure_auto='false', google_auto=False):
    if mcr_connect is True:
        if aws_auto or azure_auto == 'true':
            ab_end = {'vlan': vlan,
                      'partnerConfig': {'connectType': 'VROUTER',
                                        'awsAuto': aws_auto,
                                        'azureAuto': azure_auto,
                                        'complete': 'true',
                                        'error': 'false'}}
        elif google_auto is True:
            ab_end = {'vlan': vlan,
                      'partnerConfig': {'connectType': 'VROUTER',
                                        'interfaces': 'null',
                                        'complete': 'true',
                                        'error': 'false'}}
        else:
            ab_end = {'vlan': vlan,
                      'partnerConfig': {'connectType': 'VROUTER',
                                        'interfaces': [{'ipAddresses': [''],
                                                        'bgpConnections': [],
                                                        'ipRoutes': [],
                                                        'natIpAddresses': []}],
                                        'complete': 'true',
                                        'error': 'false'}}
    else:
        ab_end = {'vlan': vlan}
    return ab_end


# price response class
class GetPriceResponse(object):
    def __init__(self, x):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if x.status_code == 200:
            self.monthly_rate = x.json['data']['monthlyRate']
            self.currency = x.json['data']['currency']
        else:
            self.monthly_rate = 0
            self.currency = ''


# speed change class
class GetSpeedChangeResponse(object):
    def __init__(self, x):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if x.status_code == 200:
            self.new_monthly_rate = x.json['data']['longTermMonthly']
            self.currency = x.json['data']['currency']
            self.delta = x.json['data']['delta']
        else:
            self.new_monthly_rate = 0
            self.currency = ''
            self.delta = 0


# Azure, Oracle & Nutanix lookup class
class GetLookupResponse(object):
    def __init__(self, x):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if x.status_code == 200:
            self.bandwidth = x.json['data']['bandwidth']
            target_list = []
            uid_list = []
            for i in x.json['data']['megaports']:
                target_list.append(i['vxc'])
                uid_list.append(i['productUid'])
            self.target = target_list
            self.uid = uid_list
        else:
            self.bandwidth = 0
            self.target = ''
            self.uid = ''


# google lookup class
class GetGoogleLookupResponse(object):
    def __init__(self, x):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if x.status_code == 200:
            self.bandwidths = x.json['data']['bandwidths']
            target_list = []
            uid_list = []
            for i in x.json['data']['megaports']:
                target_list.append(i['vxc'])
                uid_list.append(i['productUid'])
            self.target = target_list
            self.uid = uid_list
        else:
            self.bandwidths = 0
            self.target = ''
            self.uid = ''


# speed change class
class GetBandwidthResponse(object):
    def __init__(self, x):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if x.status_code == 200:
            self.ingress_mbps = x.json['data']['in_mbps']
            self.egress_mbps = x.json['data']['out_mbps']
        else:
            self.ingress_mbps = [0]
            self.egress_mbps = [0]


# post login response
class PostLoginResponse(object):
    def __init__(self, x):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if x.status_code == 200:
            self.header = {'X-Auth-Token': x.json['data']['token'], 'Content-Type': 'application/json'}
        else:
            self.header = ''


# post order response
class PostOrderResponse(object):
    def __init__(self, x, validate, obj, lag_count='null'):
        self.request_body = x.request_body
        self.status_code = x.status_code
        self.json = x.json
        if lag_count is 'null':
            if validate is False and x.status_code == 200:
                self.uid = x.json['data'][0][obj]
                self.monthly_rate = 0
                self.currency = ''
            elif validate is True and x.status_code == 200:
                self.uid = ''
                self.monthly_rate = x.json['data'][0]['price']['monthlyRate']
                self.currency = x.json['data'][0]['price']['currency']
            else:
                self.uid = ''
                self.monthly_rate = 0
                self.currency = ''
        else:
            if validate is False and x.status_code == 200:
                uid_list = []
                for i in range(lag_count):
                    uid_list.append(x.json['data'][i][obj])
                self.uid = uid_list
                self.monthly_rate = 0
                self.currency = ''
            elif validate is True and x.status_code == 200:
                monthly_rate_list = []
                currency_list = []
                for i in range(lag_count):
                    monthly_rate_list.append(x.json['data'][i]['price']['monthlyRate'])
                    currency_list.append(x.json['data'][i]['price']['currency'])
                self.uid = ''
                self.monthly_rate = monthly_rate_list
                self.currency = currency_list
            else:
                self.uid = ''
                self.monthly_rate = 0
                self.currency = ''


# api call multi type
class Call(object):
    def __init__(self, call_type, url, header=None, body=None):
        response = getattr(requests, call_type)(url, headers=header, json=body)
        self.request_body = body
        self.status_code = response.status_code
        if response.status_code == 404:
            self.json = ''
        else:
            self.json = response.json()


# https://dev.megaport.com/#security-login-with-user-details
def login(user, pasw, tfa=0, prod=True):
    url = env(prod) + '/v2/login' + '?username=' + user + '&password=' + pasw + '&oneTimePassword=' + str(tfa)
    return PostLoginResponse(Call('post', url))


# https://dev.megaport.com/#security-login-with-token
def login_token(token, prod=True):
    url = env(prod) + '/v2/login/' + token
    return PostLoginResponse(Call('post', url))


# https://dev.megaport.com/#security-logout
def logout(token, prod=True):
    url = env(prod) + '/v2/logout/' + token
    return Call('get', url)


# https://dev.megaport.com/#security-change-password
def change_pasw(header, old_pasw, new_pasw, prod=True):
    url = env(prod) + '/v2/password/change?oldPassword=' + old_pasw + '&newPassword=' + new_pasw
    return Call('post', url, header)


# https://dev.megaport.com/#lists-used-for-ordering-locations
def locations(header, prod=True):
    url = env(prod) + '/v2/locations'
    return Call('get', url, header)


# https://dev.megaport.com/#lists-used-for-ordering-partner-megaports
def partner(header, prod=True):
    url = env(prod) + '/v2/dropdowns/partner/megaports'
    return Call('get', url, header)


# https://dev.megaport.com/#lists-used-for-ordering-internet-exchanges-ix
def ix_locations(header, loc_id, prod=True):
    url = env(prod) + '/v2/product/ix/types?locationId=' + str(loc_id)
    return Call('get', url, header)


# https://dev.megaport.com/#standard-api-orders-validate-port-order
# https://dev.megaport.com/#standard-api-orders-buy-port
# https://dev.megaport.com/#standard-api-orders-buy-port-post-1
# https://dev.megaport.com/#standard-api-orders-validate-lag-order
# https://dev.megaport.com/#standard-api-orders-buy-lag
def port(header, loc_id, name, speed, term=1, lag_count='null', lag_id='null', market='null', validate=False,
         prod=True):
    url = env(prod) + net_design_url[validate]
    body = [{'locationId': loc_id,
             'term': term,
             'locationUid': 'null',
             'productName': name,
             'productType': 'MEGAPORT',
             'createDate': int(time.time()),
             'portSpeed': speed,
             'virtual': 'false',
             'lagPortCount': lag_count,
             'aggregationId': lag_id,
             'market': market
             }]
    return PostOrderResponse(Call('post', url, header, body), validate, 'technicalServiceUid', lag_count)


# https://dev.megaport.com/#standard-api-orders-validate-mcr-order
# https://dev.megaport.com/#standard-api-orders-buy-mcr
def mcr(header, loc_id, name, speed, asn=133937, term=1, market='null', validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
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
    return PostOrderResponse(Call('post', url, header, body), validate, 'technicalServiceUid')


# https://dev.megaport.com/#standard-api-orders-validate-ix-order
# https://dev.megaport.com/#standard-api-orders-buy-ix
def ix(header, uid, name, ix_name, asn, mac, speed, vlan=0, validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
    body = [{'productUid': uid,
             'associatedIxs': [{
                 'productName': name,
                 'networkServiceType': ix_name,
                 'asn': asn,
                 'macAddress': mac,
                 'rateLimit': speed,
                 "vlan": vlan
             }]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'technicalServiceUid')


# https://dev.megaport.com/#standard-api-orders-validate-vxc-order
# https://dev.megaport.com/#standard-api-orders-buy-vxc
def vxc(header, uid, b_uid, name, speed, vlan=0, b_vlan='null', validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
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
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#standard-api-orders-service-keys-get
def service_key_lookup(header, uid=None, prod=True):
    if uid is None:
        url = env(prod) + '/v2/service/key'
    else:
        url = env(prod) + '/v2/service/key/' + uid
    return Call('get', url, header)


# https://dev.megaport.com/#standard-api-orders-service-keys-post
def service_key(header, uid, desc, vlan=0, single_use='true', max_speed='null', pre_approved='true', active='true',
                s_time='null', e_time='null', prod=True):
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
    return Call('post', url, header, body)


# https://dev.megaport.com/#cloud-partner-api-orders-aws-buy
def aws(header, uid, b_uid, name, aws_name, speed, account_num, aws_asn, asn='', mcr_connect=False,
        aws_auto='true', vlan=0, peering_type='private', auth_key='', cidr='', cust_ip='', aws_ip='', validate=False,
        prod=True):
    url = env(prod) + net_design_url[validate]
    a_end = mcr_attached(mcr_connect, vlan, aws_auto)
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'partnerConfigs': {
                     'connectType': 'AWS',
                     'type': peering_type,
                     'name': aws_name,
                     'asn': asn,
                     'ownerAccount': account_num,
                     'authKey': auth_key,
                     'prefixes': cidr,
                     'customerIpAddress': cust_ip,
                     'amazonIpAddress': aws_ip,
                     'amazonAsn': aws_asn
                 },
                 'aEnd': a_end,
                 'bEnd': {
                     'productUid': b_uid
                 }}]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#cloud-partner-api-orders-azure-step-1-lookup
def azure_lookup(header, azure_key, prod=True):
    url = env(prod) + '/v2/secure/azure/' + azure_key
    return GetLookupResponse(Call('get', url, header))


# https://dev.megaport.com/#cloud-partner-api-orders-azure-step-2-buy
def azure(header, uid, b_uid, name, speed, azure_key, mcr_connect=False, azure_auto='true', private=False,
          microsoft=False, vlan=0, validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
    peers = []
    if private is True:
        peers.append(dict({'type': 'private'}))
    if microsoft is True:
        peers.append(dict({'type': 'microsoft'}))
    a_end = mcr_attached(mcr_connect, vlan, azure_auto)
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': a_end,
                 'bEnd': {
                     'productUid': b_uid,
                     'vlan': 0,
                     'partnerConfig': {
                         'connectType': 'AZURE',
                         'serviceKey': azure_key,
                         'peers': peers
                     }}}]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#cloud-partner-api-orders-oracle-step-1-lookup
def oracle_lookup(header, oracle_key, prod=True):
    url = env(prod) + '/v2/secure/oracle/' + oracle_key
    return GetLookupResponse(Call('get', url, header))


# https://dev.megaport.com/#cloud-partner-api-orders-oracle-step-2-buy
def oracle(header, uid, b_uid, name, speed, oracle_key, mcr_connect=False, vlan=0, validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
    a_end = mcr_attached(mcr_connect, vlan)
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': a_end,
                 'bEnd': {
                     'productUid': b_uid,
                     'vlan': 0,
                     'partnerConfig': {
                         'connectType': 'ORACLE',
                         'virtualCircuitId': oracle_key
                     }}}]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#cloud-partner-api-orders-alibaba-buy
def alibaba(header, uid, b_uid, name, speed, owner_id, mcr_connect=False, vlan=0, validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
    a_end = mcr_attached(mcr_connect, vlan)
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': a_end,
                 'bEnd': {
                     'productUid': b_uid,
                     'partnerConfig': {
                         'vbrOwnerId': owner_id,
                         'connectType': 'ALIBABA'
                     }}}]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#cloud-partner-api-orders-google-step-1-lookup
def google_lookup(header, google_key, prod=True):
    url = env(prod) + '/v2/secure/google/' + google_key
    return GetGoogleLookupResponse(Call('get', url, header))


# https://dev.megaport.com/#cloud-partner-api-orders-google-step-2-buy
def google(header, uid, b_uid, name, speed, google_key, mcr_connect=False, google_auto=True, vlan=0, validate=False,
           prod=True):
    url = env(prod) + net_design_url[validate]
    a_end = mcr_attached(mcr_connect, vlan, google_auto)
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': a_end,
                 'bEnd': {
                     'productUid': b_uid,
                     'partnerConfig': {
                         'connectType': 'GOOGLE',
                         'pairingKey': google_key
                     }}}]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#cloud-partner-api-orders-nutanix-step-1-lookup
def nutanix_lookup(header, nutanix_key, prod=True):
    url = env(prod) + '/v2/secure/nutanix/' + nutanix_key
    return GetLookupResponse(Call('get', url, header))


# https://dev.megaport.com/#cloud-partner-api-orders-nutanix-step-2-buy
def nutanix(header, uid, b_uid, name, speed, nutanix_key, mcr_connect=False, vlan=0, validate=False, prod=True):
    url = env(prod) + net_design_url[validate]
    a_end = mcr_attached(mcr_connect, vlan)
    body = [{'productUid': uid,
             'associatedVxcs': [{
                 'productName': name,
                 'rateLimit': speed,
                 'aEnd': a_end,
                 'bEnd': {
                     'productUid': b_uid,
                     'partnerConfig': {
                         'connectType': 'NUTANIX',
                         'serviceKey': nutanix_key
                     }}}]}]
    return PostOrderResponse(Call('post', url, header, body), validate, 'vxcJTechnicalServiceUid')


# https://dev.megaport.com/#price-new-port-price
def new_port_price(header, loc_id, speed, term=1, prod=True):
    url = env(prod) + '/v2/pricebook/megaport?locationId=' + str(loc_id) + '&speed=' + str(speed) + '&term=' + \
          str(term) + '&virtual=false'
    return GetPriceResponse(Call('get', url, header))


# https://dev.megaport.com/#price-new-mcr-price
def new_mcr_price(header, loc_id, speed, prod=True):
    url = env(prod) + '/v2/pricebook/megaport?locationId=' + str(loc_id) + '&speed=' + str(speed) + \
          '&virtual=true'
    return GetPriceResponse(Call('get', url, header))


# https://dev.megaport.com/#price-new-vxc-price
def new_vxc_price(header, loc_id, b_loc_id, speed, prod=True):
    url = env(prod) + '/v2/pricebook/vxc?aLocationId=' + str(loc_id) + '&speed=' + str(speed) + '&bLocationId=' + \
          str(b_loc_id)
    return GetPriceResponse(Call('get', url, header))


# https://dev.megaport.com/#price-new-ix-price
def new_ix_price(header, ix_name, loc_id, speed, prod=True):
    url = env(prod) + '/v2/pricebook/ix?ixType=' + ix_name + '&portLocationId=' + str(loc_id) + '&speed=' + str(speed)
    return GetPriceResponse(Call('get', url, header))


# https://dev.megaport.com/#price-speed-change-check-price
def speed_change_price(header, uid, year, month, new_speed, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/rating/' + str(year) + '/' + str(month) + '?newSpeed=' + str(new_speed)
    return GetSpeedChangeResponse(Call('get', url, header))


# https://dev.megaport.com/#price-lifecycle-action-change-price-check
def lifecycle_change_price(header, uid, action, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/action/' + action + '/charges'
    return Call('get', url, header)


# https://dev.megaport.com/#invoices-all-invoices
# https://dev.megaport.com/#invoices-single-invoice
# https://dev.megaport.com/#invoices-single-invoice-as-pdf
def invoice(header, invoice_id=None, pdf=False, csv=False, prod=True):
    if invoice_id is None:
        url = env(prod) + '/v2/invoice'
    elif csv is True:
        url = env(prod) + '/v2/invoice/csv'
    elif invoice_id is not None and pdf is False:
        url = env(prod) + '/v2/invoice/' + invoice_id
    else:
        url = env(prod) + '/v2/invoice/' + invoice_id + '/pdf'
    return Call('get', url, header)


# https://dev.megaport.com/#general-get-product-list
# https://dev.megaport.com/#general-get-product-details
def product(header, uid=None, prod=True):
    if uid is None:
        url = env(prod) + '/v2/products'
    else:
        url = env(prod) + '/v2/products/' + uid
    return Call('get', url, header)


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
    return Call('put', url, header, body)


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
    return Call('put', url, header, body)


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
    return Call('put', url, header, body)


# https://dev.megaport.com/#general-update-product-lifecycle-action
def lifecycle_action(header, uid, action, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/action/' + action
    return Call('post', url, header)


# https://dev.megaport.com/#general-lock-product-to-prevent-editing-post
# al-lock-product-to-prevent-editing-delete
def product_lock(header, uid, lock=True, prod=True):
    url = env(prod) + '/v2/product/lock' + uid
    if lock is True:
        return Call('post', url, header)
    else:
        return Call('delete', url, header)


# https://dev.megaport.com/#general-interface-logs
def logs(header, uid, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/logs'
    return Call('get', url, header)


# https://dev.megaport.com/#general-bandwidth-usage
def bandwidth_usage(header, uid, s_time, e_time, prod=True):
    url = env(prod) + '/v2/graph/mbps?productIdOrUid=' + uid + 'to=' + e_time + 'from=' + s_time
    return GetBandwidthResponse(Call('get', url, header))


# https://dev.megaport.com/#general-read-and-write-notification-settings
def notifications(header, prod=True):
    url = env(prod) + '/v2/notificationPreferences'
    return Call('get', url, header)


# https://dev.megaport.com/#general-regenerate-loa
def loa(header, uid, prod=True):
    url = env(prod) + '/v2/product/' + uid + '/loa'
    return Call('get', url, header)
