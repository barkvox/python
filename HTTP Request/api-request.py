import requests as req

url = 'https://dev.uipath.vodafone.co.nz/api/Account/Authenticate?='
payload = {
    'tenancyName': 'PlatformsCOE', 
    'usernameOrEmailAddress': 'Joshua Barker',
    'password': 'X6SImF2SHJ^p',
    }
r = req.get(url=url, params=payload)

print(r.url)