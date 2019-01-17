import requests

env_url = ['https://api.megaport.com', 'https://api-staging.megaport.com']


def env(prod):
    if prod is True:
        url = env_url[0]
    else:
        url = env_url[1]
    return url


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
    else:
        header = None
    return header
