import requests
import getpass

session = requests.Session()

getLoginResult = session.get('https://account.t-mobile.com')

getLoginResult.raise_for_status()

# correctedLoginUrl = getResult.url

session.headers.update({
                           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'})

phoneNum = input('Enter phone number: ')
password = getpass.getpass('Enter password: ')

session.post('https://account.t-mobile.com/oauth2/v1/controller',
             data={
                 "requestCode": "1006",
                 "combination-email-msisdn-username": phoneNum,
                 "password": password})

getHomeResult = session.get('https://my.t-mobile.com/home.html')
print('getHomeResult: ' + getHomeResult.text)